# Copyright (C) 2020 Odoo Community Association (OCA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Brand',
    'summary': """
        This is a base addon for brand modules. It adds the brand object and
        its menu and define an abstract model to be inherited from branded
        objects""",
    'version': '13.0.1.0',
    'license': 'AGPL-3',
    'author': 'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/brand',
    'depends': ['base_setup'],
    'data': [
        'views/res_config_settings.xml',
        'security/res_brand.xml',
        'views/res_brand.xml',
        'views/res_company_view.xml',
        'views/menu.xml',
    ],
}
