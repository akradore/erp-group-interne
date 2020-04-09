# Copyright (C) 2020 ArkeUp SAS
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
	'name': 'ArkeUp Brand',
	'summary': '',
	'version': '13.0.1.0',
	'category': 'Sales Management',
	'website': 'https://arkeup.com/',
	'author': 'ArkeUp',
	'license': 'AGPL-3',
	'depends': [
		'crm',
		'account',
		'sale_brand',
	],
	'data': [
		# data
		'data/crm_team_data.xml',
		'data/res_brand_data.xml',
		'data/analytic_account_data.xml',
		# security
		'security/res_groups.xml',
		'security/ir_rule.xml',
		# views
		'views/res_brand_view.xml',
		'views/res_users_view.xml',
	],
	'application': True,
	'installable': True,
	'auto_install': False,
}
