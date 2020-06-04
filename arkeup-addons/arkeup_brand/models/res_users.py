# Copyright (C) 2020 ArkeUp SAS
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    brand_ids = fields.Many2many('res.brand', string='Brands',
                                 domain="['|', ('company_id', '=', False), ('company_id', 'in', company_ids)]")

    def get_my_brands(self):
        self.ensure_one()
        return self.brand_ids.ids
