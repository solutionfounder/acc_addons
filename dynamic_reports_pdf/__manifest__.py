# -*- coding: utf-8 -*-
{
    'name': 'Print Dynamic Financial Reports',
    'version': '12.0.1.0.0',
    'category': 'Accounting',
    'summary': """Pdf report of the dynamic financial reports.
                It facilitates Printing out the dynamic financial reports of balance sheet and profit 'n' loss to Xlsx or PDF files.""",
    'description': "This module is an extension of the "
                   "accounting_dynamic_reports module",
    'author': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'depends': [
        'web',
        'base',
        'accounting_dynamic_reports',
        'report_xlsx',
    ],
    'data': [
        'views/templates.xml',
        'report/report_action.xml',
        'report/report_financial.xml'
    ],
    'qweb': [
        'static/src/xml/*.xml'
    ],
    'images': ['static/description/banner.png'],
    'license': 'OPL-1',
    'price': 10,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False,
}
