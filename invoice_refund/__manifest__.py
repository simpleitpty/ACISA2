# -*- coding: utf-8 -*-
{
    'name': "Facturacion de Retificativa",
    'summary': """Facturacion de Retificativa""",
    'description': """
       Enlaza una factura con su factura retificativa """,
    'author': "Intelitecsa(Francisco Trejo)",
    'website': "http://www.intelitecsa.com",
    'price': 100.00,
    'currency': 'USD',
    'license': 'GPL-3',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Contabilidad',
    'version': '0.2',
    # any module necessary for this one to work correctly
    'depends': ['base' ,'account'],
    # always loaded
    'data': [
        'views/account_invoice_view.xml',
        'wizard/account_invoice_refund.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    #'demo.xml',
    'installable': True,
    'application': False,
    'auto_install': False,
    'post_init_hook': 'invoices_refunds',
}
