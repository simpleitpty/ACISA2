# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, exceptions


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    inv_refund_id = fields.Many2one('account.invoice', 'Factura Relacionada', copy=False, track_visibility='onchange')

    state_refund = fields.Selection([
        ('refund', 'Retificada'),
        ('no_refund', 'No Retificada'),
    ], string="Retificada", index=True, readonly=True, default='no_refund',
        track_visibility='onchange', copy=False)
    inv_refund_number = fields.Char('Numero', related='inv_refund_id.number_integer')
