# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

import odoo.addons.decimal_precision as dp
from odoo import api, fields, models, _


class Template(models.Model):
    _inherit = 'product.template'

    stock_location_template = fields.One2many('stock.location.product', 'custom_template_id', string="Stock Location", )

    def upate_compute_stock_location(self):

        loc = self.env['stock.location'].search([('usage', '=', 'internal')])
        for product_tmpl in self:
            variant_ids = []
            for product in product_tmpl.product_variant_ids:
                product.remove_filter()
                variant_ids.append(product.id)

            for l in loc:

                search_product_records = self.env['stock.location.product'].search(
                    [('custom_product_id', 'in', variant_ids), ('stock_location_id', '=', l.id)])
                total_on_hand_qty = 0.0
                total_forcasted_qty = 0.0
                total_incoming_qty = 0.0
                total_out_qty = 0.0
                for location_product in search_product_records:
                    total_on_hand_qty = total_on_hand_qty + location_product.on_hand_qty
                    total_forcasted_qty = total_forcasted_qty + location_product.forcasted_qty
                    total_incoming_qty = total_incoming_qty + location_product.incoming_qty
                    total_out_qty = total_out_qty + location_product.out_qty

                vals = {
                    'stock_location_id': l.id,
                    'on_hand_qty': total_on_hand_qty,
                    'incoming_qty': total_incoming_qty,
                    'out_qty': total_out_qty,
                    'custom_template_id': product_tmpl.id,
                    'forcasted_qty': total_forcasted_qty,

                }

                search_product_records = self.env['stock.location.product'].search(
                    [('custom_template_id', '=', product_tmpl.id), ('stock_location_id', '=', l.id)])
                if search_product_records:
                    search_product_records = search_product_records[0]
                    search_product_records.write(vals)
                else:
                    res = self.env['stock.location.product'].create(vals)
