# -*- coding: utf-8 -*-

from odoo import models


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    def _get_open_bills_to_pay_query(self):
        """
        Returns a tuple containing the SQL query used to gather the open bills
        data as its first element, and the arguments dictionary to use to run
        it as its second.
        """
        return ('''
            SELECT
                (CASE WHEN move.type IN ('out_refund', 'in_refund') THEN -1 ELSE 1 END) * move.amount_residual AS amount_total,
                move.currency_id AS currency,
                move.type,
                move.invoice_date,
                move.company_id,
                move.operating_unit_id
            FROM account_move move
            WHERE move.journal_id = %(journal_id)s
            AND move.state = 'posted'
            AND move.invoice_payment_state = 'not_paid'
            AND move.type IN ('out_invoice', 'out_refund', 'in_invoice', 'in_refund', 'out_receipt', 'in_receipt')
            AND move.operating_unit_id IN %(unit_ids)s;
        ''', {'journal_id': self.id, 'unit_ids': tuple(self.env.user.operating_unit_ids.ids)})

    def _get_draft_bills_query(self):
        """
        Returns a tuple containing as its first element the SQL query used to
        gather the bills in draft state data, and the arguments
        dictionary to use to run it as its second.
        """
        return ('''
            SELECT
                (CASE WHEN move.type IN ('out_refund', 'in_refund') THEN -1 ELSE 1 END) * move.amount_total AS amount_total,
                move.currency_id AS currency,
                move.type,
                move.invoice_date,
                move.company_id,
                move.operating_unit_id
            FROM account_move move
            WHERE move.journal_id = %(journal_id)s
            AND move.state = 'draft'
            AND move.invoice_payment_state = 'not_paid'
            AND move.type IN ('out_invoice', 'out_refund', 'in_invoice', 'in_refund', 'out_receipt', 'in_receipt')
            AND move.operating_unit_id IN %(unit_ids)s;
        ''', {'journal_id': self.id, 'unit_ids': tuple(self.env.user.operating_unit_ids.ids)})

    def _get_expenses_to_pay_query(self):
        """
        Returns a tuple containing as it's first element the SQL query used to
        gather the expenses in reported state data, and the arguments
        dictionary to use to run it as it's second.
        """
        query = """SELECT total_amount as amount_total, currency_id AS currency
                  FROM hr_expense_sheet
                  WHERE state IN ('approve', 'post')
                  AND journal_id = %(journal_id)s
                  AND operating_unit_id IN %(unit_ids)s;"""
        return query, {'journal_id': self.id, 'unit_ids': tuple(self.env.user.operating_unit_ids.ids)}
