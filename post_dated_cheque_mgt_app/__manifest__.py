# -*- coding: utf-8 -*-

{
    "name" : "Postdated Check Management (PDC) Odoo",
    "author": "Edge Technologies",
    "version" : "12.0.1.0",
    "live_test_url":'https://youtu.be/y5G6ehXbIgI',
    "images":["static/description/main_screenshot.png"],
    'summary': 'Apply PDC Payment, Generate PDC Payment Entries and Journal Entries With PDC Account',
    "description": """ This app help to user Apply PDC Payment, Generate PDC Payment Entries, Generate Journal Entries with Default Configured PDC Account, Also Re-Generate Journal Entries with Configured PDC Account when the Done Collect Cash from PDC Payment from Customer Invoice and Vendor Bill. Filter PDC Payments by Stages and Customers.


Post Dated Cheque Management
Odoo pDC cheque
Odoo pdc check
bank pdc check
Postdated Check  in Customer Invoice and Vendor Bill
Postdated Cheque pdc
Post-dated cheque
bill of exchange Post-dated
pdc bill of exchange
check payment
Check Management
pdc check payment
PDC Cheque pdc
bank pdc check pdc
account cheque flow account cheque cycle bank cheque flow bank cheque cycle
account check flow account check cycle bank cheque flow bank check cycle
Post-dated Check  in Customer Invoice and Vendor Bill
Post-dated Cheque pdc


     """,
    "license" : "OPL-1",
    "depends" : ['base','sale','purchase','sale_management','account'],
    "data": [
        'data/pdc_payment_data.xml',
        'security/pdc_payment_group.xml',
        'security/ir.model.access.csv',
        'wizard/pdc_payment_wizard_view.xml',
        'views/res_config_view.xml',
        'report/pdc_payment_template.xml',
        'report/pdc_payment_action.xml',
        'views/pdc_payment_view.xml',
        'views/invoice_inherit_view.xml',
    ],
    "auto_install": False,
    "installable": True,
    "price": 25,
    "currency": 'EUR',
    "category" : "Accounting",
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
