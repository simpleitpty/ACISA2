from odoo import fields, models, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    num_doc_fiscal = fields.Char(string='Numero Fiscal')
    is_print = fields.Boolean('Ha sido impresa')