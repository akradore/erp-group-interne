# -*- coding: utf-8 -*-

from odoo import fields, models


class PurchaseReport(models.Model):
    _inherit = 'purchase.report'

    operating_unit_id = fields.Many2one('operating.unit', 'Operating Unit')

    def _select(self):
        return super(PurchaseReport, self)._select() + ', po.operating_unit_id'

    def _group_by(self):
        return super(PurchaseReport, self)._group_by() + ", po.operating_unit_id"
