# -*- coding: utf-8 -*-

{
    'name': 'Quotation/Sale date order visibility',
    'version': '1.0.1.2',
    'author':'Soft-integration',
    'category': 'Sales',
    'summary': 'Quotation/Sale date order visibility',
    'description': "",
    'depends': [
        'sale_management',
    ],
    'data': [
        'security/sale_order_date_order_visibility_security.xml',
        'views/sale_views.xml',
        'views/res_config_settings_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
