# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

import odoo.addons.decimal_precision as dp
from odoo import api, fields, models, _


class stock_location_product(models.Model):
    _name = 'stock.location.product'

    stock_location_id = fields.Many2one('stock.location', string="Location")
    on_hand_qty = fields.Float('On hand Quantity')
    custom_product_id = fields.Many2one('product.product')
    custom_template_id = fields.Many2one('product.template')
    forcasted_qty = fields.Float('Forcasted Quantity')
    incoming_qty = fields.Float('Incoming Quantity')
    out_qty = fields.Float('Out Quantity')
