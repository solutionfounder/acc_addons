# coding: utf-8

from odoo import _, api, fields, models
from odoo.exceptions import UserError

class AccountPaymentInvoices(models.Model):
    _name = 'account.payment.invoice'

    invoice_id = fields.Many2one('account.invoice', string='Invoice')
    payment_id = fields.Many2one('account.payment', string='Payment')
    currency_id = fields.Many2one(related='invoice_id.currency_id')
    origin = fields.Char(related='invoice_id.origin')
    date_invoice = fields.Date(related='invoice_id.date_invoice')
    date_due = fields.Date(related='invoice_id.date_due')
    payment_state = fields.Selection(related='payment_id.state', store=True)
    reconcile_amount = fields.Monetary(string='Reconcile Amount')
    amount_total = fields.Monetary(related="invoice_id.amount_total")
    residual = fields.Monetary(related="invoice_id.residual")

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    payment_invoice_ids = fields.One2many('account.payment.invoice', 'payment_id',string="Customer Invoices")

    @api.onchange('payment_type', 'partner_type', 'partner_id', 'currency_id')
    def _onchange_to_get_vendor_invoices(self):
        if self.payment_type in ['inbound', 'outbound'] and self.partner_type and self.partner_id and self.currency_id:
            if self.payment_type == 'inbound' and self.partner_type == 'customer':
                invoice_type = 'out_invoice'
            elif self.payment_type == 'outbound' and self.partner_type == 'customer':
                invoice_type = 'out_refund'
            elif self.payment_type == 'outbound' and self.partner_type == 'supplier':
                invoice_type = 'in_invoice'
            else:
                invoice_type = 'in_refund'
            invoice_recs = self.env['account.invoice'].search([('partner_id', 'child_of', self.partner_id.id), ('type', '=', invoice_type), ('state', '=', 'open'), ('currency_id', '=', self.currency_id.id)])
            payment_invoice_values = []
            for invoice_rec in invoice_recs:
                payment_invoice_values.append([0, 0, {'invoice_id': invoice_rec.id}])
            self.payment_invoice_ids = payment_invoice_values

    @api.multi
    def post(self):
        if self.payment_invoice_ids:
            if self.amount < sum(self.payment_invoice_ids.mapped('reconcile_amount')):
                raise UserError(_("The sum of the reconcile amount of listed invoices are greater than payment's amount."))
        res = super(AccountPayment, self).post()
        return res

    def _create_payment_entry(self, amount):
        """ Create a journal entry corresponding to a payment, if the payment references invoice(s) they are reconciled.
            Return the journal entry.
        """
        aml_obj = self.env['account.move.line'].with_context(check_move_validity=False)
        debit, credit, amount_currency, currency_id = aml_obj.with_context(date=self.payment_date)._compute_amount_fields(amount, self.currency_id, self.company_id.currency_id)

        move = self.env['account.move'].create(self._get_move_vals())

        counterpart_aml_list = {}
        # Write line corresponding to invoice payment
        if self.payment_invoice_ids and self.payment_type == 'inbound':
            total_reconcile_amount = 0.00
            total_separate_amount_currency = 0.00
            for payment_invoice_id in self.payment_invoice_ids:
                if payment_invoice_id.reconcile_amount > 0:
                    separate_amount_currency = amount_currency
                    reconcile_amount = payment_invoice_id.reconcile_amount
                    if amount_currency and credit:
                        reconcile_amount = (payment_invoice_id.reconcile_amount * credit) / amount_currency
                        separate_amount_currency = -payment_invoice_id.reconcile_amount
                        reconcile_amount = -reconcile_amount
                    total_reconcile_amount += reconcile_amount
                    total_separate_amount_currency += separate_amount_currency
                    counterpart_aml_dict = self._get_shared_move_line_vals(debit, reconcile_amount, separate_amount_currency, move.id, False)
                    counterpart_aml_dict.update(self._get_counterpart_move_line_vals([payment_invoice_id.invoice_id]))
                    counterpart_aml_dict.update({'currency_id': currency_id})
                    counterpart_aml = aml_obj.create(counterpart_aml_dict)
                    counterpart_aml_list[payment_invoice_id.invoice_id.id] = counterpart_aml
            if credit > total_reconcile_amount:
                remaining_reconcile_amount = credit - total_reconcile_amount
                separate_amount_currency = amount_currency
                if amount_currency and credit:
                    separate_amount_currency = amount_currency - total_separate_amount_currency
                counterpart_aml_dict = self._get_shared_move_line_vals(debit, remaining_reconcile_amount, separate_amount_currency, move.id, False)
                counterpart_aml_dict.update(self._get_counterpart_move_line_vals(self.invoice_ids))
                counterpart_aml_dict.update({'currency_id': currency_id})
                counterpart_aml = aml_obj.create(counterpart_aml_dict)
        elif self.payment_invoice_ids and self.payment_type == 'outbound':
            total_reconcile_amount = 0.00
            total_separate_amount_currency = 0.00
            for payment_invoice_id in self.payment_invoice_ids:
                if payment_invoice_id.reconcile_amount > 0:
                    separate_amount_currency = amount_currency
                    reconcile_amount = payment_invoice_id.reconcile_amount
                    if amount_currency and debit:
                        reconcile_amount = (payment_invoice_id.reconcile_amount * debit) / amount_currency
                        separate_amount_currency = payment_invoice_id.reconcile_amount
                    total_reconcile_amount += reconcile_amount
                    total_separate_amount_currency += separate_amount_currency
                    counterpart_aml_dict = self._get_shared_move_line_vals(reconcile_amount, credit, separate_amount_currency, move.id, False)
                    counterpart_aml_dict.update(self._get_counterpart_move_line_vals([payment_invoice_id.invoice_id]))
                    counterpart_aml_dict.update({'currency_id': currency_id})
                    counterpart_aml = aml_obj.create(counterpart_aml_dict)
                    counterpart_aml_list[payment_invoice_id.invoice_id.id] = counterpart_aml
            if debit > total_reconcile_amount:
                remaining_reconcile_amount = debit - total_reconcile_amount
                separate_amount_currency = amount_currency
                if amount_currency and debit:
                    separate_amount_currency = amount_currency - total_separate_amount_currency
                counterpart_aml_dict = self._get_shared_move_line_vals(remaining_reconcile_amount, credit, separate_amount_currency, move.id, False)
                counterpart_aml_dict.update(self._get_counterpart_move_line_vals(self.invoice_ids))
                counterpart_aml_dict.update({'currency_id': currency_id})
                counterpart_aml = aml_obj.create(counterpart_aml_dict)
        else:
            counterpart_aml_dict = self._get_shared_move_line_vals(debit, credit, amount_currency, move.id, False)
            counterpart_aml_dict.update(self._get_counterpart_move_line_vals(self.invoice_ids))
            counterpart_aml_dict.update({'currency_id': currency_id})
            counterpart_aml = aml_obj.create(counterpart_aml_dict)

        #Reconcile with the invoices
        if self.payment_difference_handling == 'reconcile' and self.payment_difference and not self.payment_invoice_ids:
            writeoff_line = self._get_shared_move_line_vals(0, 0, 0, move.id, False)
            debit_wo, credit_wo, amount_currency_wo, currency_id = aml_obj.with_context(date=self.payment_date)._compute_amount_fields(self.payment_difference, self.currency_id, self.company_id.currency_id)
            writeoff_line['name'] = self.writeoff_label
            writeoff_line['account_id'] = self.writeoff_account_id.id
            writeoff_line['debit'] = debit_wo
            writeoff_line['credit'] = credit_wo
            writeoff_line['amount_currency'] = amount_currency_wo
            writeoff_line['currency_id'] = currency_id
            writeoff_line = aml_obj.create(writeoff_line)
            if counterpart_aml['debit'] or (writeoff_line['credit'] and not counterpart_aml['credit']):
                counterpart_aml['debit'] += credit_wo - debit_wo
            if counterpart_aml['credit'] or (writeoff_line['debit'] and not counterpart_aml['debit']):
                counterpart_aml['credit'] += debit_wo - credit_wo
            counterpart_aml['amount_currency'] -= amount_currency_wo

        #Write counterpart lines
        if not self.currency_id.is_zero(self.amount):
            if not self.currency_id != self.company_id.currency_id:
                amount_currency = 0
            liquidity_aml_dict = self._get_shared_move_line_vals(credit, debit, -amount_currency, move.id, False)
            liquidity_aml_dict.update(self._get_liquidity_move_line_vals(-amount))
            aml_obj.create(liquidity_aml_dict)

        #validate the payment
        if not self.journal_id.post_at_bank_rec:
            move.post()

        #reconcile the invoice receivable/payable line(s) with the payment
        if self.payment_invoice_ids and self.payment_type in ['inbound', 'outbound']:
            invoice_ids = []
            for counterpart_aml_list_itr in counterpart_aml_list.keys():
                invoice_obj = self.env['account.invoice'].browse([counterpart_aml_list_itr])
                invoice_ids.append(counterpart_aml_list_itr)
                invoice_obj.register_payment(counterpart_aml_list[counterpart_aml_list_itr])
            self.invoice_ids = [(6, 0, invoice_ids)]
        else:
            self.invoice_ids.register_payment(counterpart_aml)

        return move