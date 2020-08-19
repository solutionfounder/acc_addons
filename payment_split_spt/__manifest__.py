# -*- coding: utf-8 -*-
# Part of SnepTech See LICENSE file for full copyright and licensing details.##
##################################################################################

{
    'name':"Payment Split",
    'summary':"Multiple Payments at One Time",
    'sequence':1,
    "price": '99.99',
    "currency": 'USD',
       
    'description':""" 
        Create Split Payment for invoice Payment in just one click. Pay single invoice by multiple payments easily.
        
    """,
    'live_test_url':"https://youtu.be/4ysiFl7zIMk",
    'category':'',
    'version':'13.0.0.1',
    'license':'AGPL-3',
    'author':'SnepTech',
    'website':'https://www.sneptech.com',

    'depends': ['account','base'],

    'data': [
        'security/ir.model.access.csv',
        'views/amount_view_spt.xml',
        'views/payment_split_view_spt.xml',
    ],

    'application':True,
    'installable':True,
    'auto_install':False,
    "images":['static/description/Banner.png'],
}
