# © 2017 Nedas Žilinskas <nedas.zilinskas@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ResPartner(models.Model):

    _inherit = 'res.partner'

    allowed_pricelists = fields.Many2many(
        comodel_name='product.pricelist',
        compute='_compute_allowed_pricelists',
    )

    @api.depends('hcategory_id')
    def _compute_allowed_pricelists(self):
        default_pl_id = self.env.ref(
            'website_sale_pricelist_visibility.default_pricelist'
        ).id
        for rec in self:
            rec.allowed_pricelists = [
                (6, 0, [default_pl_id] + rec.hcategory_id.pricelist_ids.ids +
                    rec.hcategory_id.inherited_pricelist_ids.ids),
            ]

    @api.onchange('hcategory_id')
    def _onchange_pricelist(self):
        ids = self.allowed_pricelists.ids

        return {
            'value': {
                'property_product_pricelist': False,
            },
            'domain': {
                'property_product_pricelist': [('id', 'in', ids)],
            }
        }
