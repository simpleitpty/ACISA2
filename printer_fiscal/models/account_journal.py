from odoo import fields, models, api


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    serial_printer = fields.Char('Serial de Impresora')

