# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import _


class AccountPayment(models.Model):
    _inherit = "account.payment"
    _description = 'account.payment'
    
    signed_amount = fields.Monetary(
        string="Amount Signed",
        related='amount_signed',
    )