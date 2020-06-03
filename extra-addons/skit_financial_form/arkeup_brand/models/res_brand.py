# Copyright (C) 2020 ArkeUp SAS
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResBrand(models.Model):
    _inherit = 'res.brand'

    team_id = fields.Many2one('crm.team', 'Sales Team', domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    analytic_account_id = fields.Many2one('account.analytic.account', 'Analytic Account', index=True)
