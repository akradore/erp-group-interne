# -*- coding: utf-8 -*-
{
    'name': 'ArkeUp Operating Unit',
    'summary': '',
    'version': '13.0.1',
    'author': 'ArkeUp',
    'website': 'https://arkeup.com',
    'category': 'Generic',
    'depends': ['purchase_operating_unit', 'account_operating_unit', 'hr_expense_operating_unit'],
    'license': 'LGPL-3',
    'data': [
        # security
        'security/ir_rule.xml',
        # views
        'view/purchase_order_view.xml',
    ],
    'demo': [],
    'application': False,
    'installable': True,
    'auto_install': False
}
