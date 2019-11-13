# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _

class res_users(models.Model):
    _inherit = 'res.users'

    is_allow_payments = fields.Boolean('Allow Payments',default=False)
    is_allow_discount = fields.Boolean('Allow Discount',default=False)
    is_allow_qty = fields.Boolean('Allow Qty',default=False)
    is_edit_price = fields.Boolean('Allow Edit Price',default=False)
    is_allow_remove_orderline = fields.Boolean('Allow Remove Order Line',default=False)


class pos_order(models.Model):
    _inherit = 'pos.order'

    def get_cashier_value(self):
        user = self.env['res.users'].browse(self.id)
        lst = [user.is_allow_payments,user.is_allow_qty,user.is_allow_discount,user.is_edit_price,user.is_allow_remove_orderline]   
        return lst