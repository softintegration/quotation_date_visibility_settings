# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_sale_order_date_order_from_quotation_date = fields.Boolean("Use the Quotation date as the date order")
