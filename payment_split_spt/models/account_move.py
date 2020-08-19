# -*- coding: utf-8 -*-
# Part of SnepTech See LICENSE file for full copyright and licensing details.##
##################################################################################

from odoo import api, fields, models, _

class account_move(models.Model):
    _inherit = 'account.move'

    
    def action_invoice_register_payment(self):
        form_view = self.env.ref('payment_split_spt.payment_split_form_view_spt')
        for record in self:
            ctx = {
                'default_move_ids' : [(4,rec.id) for rec in self],
                'default_partner_id' : record.partner_id.id,
            }
            
        return {
        'name': _('Register Payment'),
        'view_type': 'form',
        'view_mode': 'form',
        'res_model': 'payment.split.spt',
        'views': [(form_view.id, 'form')],
        'type': 'ir.actions.act_window',
        'target': 'new',
        'context': ctx,

        }

