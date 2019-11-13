# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.


{
    "name" : "Allow/Disable POS Features",
    "version" : "12.0.0.3",
    "category" : "Point of Sale",
    'summary': 'This apps helps to Allow and Disable POS Features like Payment, Qty, Discount, Edit Price, Remove Orderline',
    "description": """

    Purpose :-
    Allow/Deny POS Features like Payment, Qty, Discount, Edit Price, Remove Orderline for Particular POS User...!!!
    """,
    "author": "BrowseInfo",
    "website" : "www.browseinfo.in",
    "price": 20,
    "currency": 'EUR',
    "depends" : ['base','sale','point_of_sale'],
    "data": [
        'views/custom_pos_view.xml',
            ],
    'qweb': [
        'static/src/xml/pos_disable_payments.xml',
            ],
    "auto_install": False,
    "installable": True,
    'live_test_url':'https://youtu.be/oOnU8LLLhwA',
    "images":['static/description/Banner.png'],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
