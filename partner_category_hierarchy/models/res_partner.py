# © 2017 Nedas Žilinskas <nedas.zilinskas@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ResPartner(models.Model):

    _inherit = 'res.partner'

    hcategory_id = fields.Many2one(
        comodel_name='res.partner.hcategory',
        string='Category',
    )

    @api.multi
    def open_partner_category(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'res.partner.hcategory',
            'view_mode': 'form',
            'res_id': self.hcategory_id.id,
            'target': 'current',
            'flags': {'form': {'action_buttons': True}}
        }
