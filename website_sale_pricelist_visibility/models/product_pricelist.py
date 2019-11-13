# © 2017 Nedas Žilinskas <nedas.zilinskas@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models
from odoo.tools.translate import _
from odoo.exceptions import ValidationError


class ProductPricelist(models.Model):

    _inherit = 'product.pricelist'

    @api.multi
    def write(self, vals):
        for rec in self:
            if rec.id == self.env.ref(
                'website_sale_pricelist_visibility.default_pricelist'
            ).id and 'sequence' in vals and vals['sequence'] != 0:
                raise ValidationError(
                    _('You can not change sequence of default pricelist!')
                )

        return super(ProductPricelist, self).write(vals)

    @api.multi
    def unlink(self):
        default_pl_id = self.env.ref(
            'website_sale_pricelist_visibility.default_pricelist'
        ).id
        for rec in self:
            if rec.id == default_pl_id:
                raise ValidationError(
                    _('You can not delete default pricelist!')
                )
        return super(ProductPricelist, self).unlink()

    def _get_partner_pricelist(self, partner_id, company_id=None):
        pl = super(ProductPricelist, self)._get_partner_pricelist(
            partner_id=partner_id,
            company_id=company_id,
        )

        partner = self.env['res.partner'].browse(partner_id)
        if not pl or pl not in partner.allowed_pricelists.ids:
            pl = self.env.ref(
                'website_sale_pricelist_visibility.default_pricelist'
            ).id

        return pl
