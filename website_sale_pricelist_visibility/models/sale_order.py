# © 2017 Nedas Žilinskas <nedas.zilinskas@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        ids = self.partner_id.allowed_pricelists.ids

        return {
            'value': {
                'pricelist_id': False,
            },
            'domain': {
                'pricelist_id': [('id', 'in', ids)],
            }
        }
