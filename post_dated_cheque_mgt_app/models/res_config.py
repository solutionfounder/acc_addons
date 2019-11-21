# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ResConfigSettings(models.TransientModel):
	_inherit = 'res.config.settings'

	pdc_account_id = fields.Many2one('account.account',string="PDC Account")

	# set default pdc account
	@api.model
	def default_get(self, fields):
		res = super(ResConfigSettings, self).default_get(fields)
		pdc_account = self.env['account.account'].search([('code','=','100502')], limit=1)
		res.update({'pdc_account_id':pdc_account.id})
		return res

	@api.model
	def get_values(self):
		res = super(ResConfigSettings, self).get_values()
		ICPSudo = self.env['ir.config_parameter'].sudo()
		pdc_account_id = ICPSudo.get_param('post_dated_cheque_mgt_app.pdc_account_id')
		res.update(pdc_account_id = int(pdc_account_id)or False)
		return res

	@api.multi
	def set_values(self):
		res = super(ResConfigSettings, self).set_values()
		self.env['ir.config_parameter'].sudo().set_param('post_dated_cheque_mgt_app.pdc_account_id', self.pdc_account_id.id)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: