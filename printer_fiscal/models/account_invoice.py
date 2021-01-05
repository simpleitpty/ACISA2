# -*- coding: utf-8 -*-
from odoo import fields, models, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    num_doc_fiscal = fields.Char(string='Numero Fiscal')
    is_print = fields.Boolean('Ha sido impresa')
    number_integer = fields.Char('Numero', compute='_numeracion', store=True)

    @api.depends('number')
    def _numeracion(self):
        i = 0
        n = "0123456789"
        for record in self:
            num = record.number
            if num:
                for letra in num:
                    i += 1
                    if letra not in n:
                        long = i
                record.number_integer = num[long:]
            else:
                record.number_integer = 0
