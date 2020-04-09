# Copyright (C) 2020 ArkeUp SAS
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    brand_id = fields.Many2one('res.brand', 'Brand', index=True)

    def get_my_brand(self):
        self.ensure_one()
        return self.brand_id.id

    def get_my_analytic_account(self):
        self.ensure_one()
        return self.env.ref('arkeup_brand.analytic_account_reunion', raise_if_not_found=False).id
