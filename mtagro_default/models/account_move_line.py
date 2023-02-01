# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools.translate import _


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"
    _description = 'account.move.line'

    commission = fields.Float(
        string="Commission",
        default=0.0
    )