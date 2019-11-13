# © 2017 Nedas Žilinskas <nedas.zilinskas@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResPartnerHCategory(models.Model):

    _inherit = 'res.partner.hcategory'

    pricelist_ids = fields.Many2many(
        comodel_name='product.pricelist',
        string='Allowed Pricelists',
    )

    inherited_pricelist_ids = fields.Many2many(
        comodel_name='product.pricelist',
        string='Inherited Pricelists',
        compute='_compute_inherited_pricelist_ids',
    )

    def _compute_inherited_pricelist_ids(self):
        for rec in self:
            allowed_pricelist_ids = []
            hparent_id = rec.parent_id
            while hparent_id:
                allowed_pricelist_ids += hparent_id.pricelist_ids.ids
                hparent_id = hparent_id.parent_id
            rec.inherited_pricelist_ids = [(6, 0, allowed_pricelist_ids)]
