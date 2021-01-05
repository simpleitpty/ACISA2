# -*- coding: utf-8 -*-
from odoo import fields, models, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    num_doc_fiscal = fields.Char(string='Numero Fiscal')
    is_print = fields.Boolean('Ha sido impresa')
    number_integer = fields.Char('Numero', compute='numeracion', store=True)

    @api.one
    def numeracion(self):
        i = 0
        n = "0123456789"
        num = self.number
        for letra in num:
            i += 1
            if letra not in n:
                long = i
        number = num[long:]
        return number
