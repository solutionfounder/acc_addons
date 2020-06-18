# -*- coding: utf-8 -*-

{
    'name': 'Dynamic Financial Reports',
    'version': '12.0.1.0.0',
    'category': 'Accounting',
    'summary': """Dynamic Balance Sheet & Profit & Loss Report with drill down – Community Edition""",
    'description': "This module creates dynamic Balance Sheet and P & L Dynamic financial report, financial report"
                   "reports"
                   "Balance Sheet & Profit and Loss Reports, Financial report,"
                   " Dynamic Report, Odoo Accounting",
    'author': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'depends': ['web', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'data/account_financial_report_data.xml',
        'views/templates.xml',
        'views/account_view.xml',
        'wizard/report_form.xml',
            ],
    'qweb': [
        'static/src/xml/*.xml'],
    'license': 'OPL-1',
    'price': 19,
    'currency': 'EUR',
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    'application': False,
}    
