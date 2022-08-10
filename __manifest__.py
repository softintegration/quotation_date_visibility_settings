# -*- coding: utf-8 -*-

{
    'name': 'Quotation date visibility settings',
    'version': '1.0.1',
    'author':'Soft-integration',
    'category': 'Sales',
    'summary': 'Configure the visibility of quotation order date',
    'description': "",
    'depends': [
        'sale',
    ],
    'data': [
        'security/quotation_date_visibility_settings_security.xml',
        'views/sale_views.xml',
        'views/res_config_settings_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
