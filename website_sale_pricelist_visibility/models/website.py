# © 2017 Nedas Žilinskas <nedas.zilinskas@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class Website(models.Model):

    _inherit = 'website'

    def get_pricelist_available(self, show_visible=False):
        res = super(Website, self).get_pricelist_available(show_visible=False)

        partner = self.env.user.partner_id
        allowed_ids = partner.allowed_pricelists.ids

        pricelists = self.env['product.pricelist']
        for prslst in res:
            if prslst.id not in allowed_ids:
                continue
            pricelists += prslst

        return pricelists
