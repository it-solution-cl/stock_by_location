# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

import odoo.addons.decimal_precision as dp
from odoo import api, fields, models, _


class product(models.Model):
    _inherit = 'product.product'

    start_date = fields.Datetime('Start Date')
    end_date = fields.Datetime('End Date')
    stock_location = fields.One2many('stock.location.product', 'custom_product_id', string="Stock Location")

    def remove_filter(self):
        dict_pro = self._product_available()
        product_details = dict_pro.get(self.id)

        s_date = self.start_date
        e_date = self.end_date

        loc = self.env['stock.location'].search([('usage', '=', 'internal')])
        result = []
        created_ids = []
        for pro in self:
            for a in loc:

                domain_quant = [('product_id', '=', pro.id), ('location_id', '=', a.id)]
                domain_move_in = [('product_id', '=', pro.id), ('location_dest_id', '=', a.id)]
                domain_move_out = [('product_id', '=', pro.id), ('location_id', '=', a.id)]
                Move = self.env['stock.move']
                Quant = self.env['stock.quant']
                domain_move_in_todo = [('state', 'not in', ('done', 'cancel', 'draft'))] + domain_move_in
                domain_move_out_todo = [('state', 'not in', ('done', 'cancel', 'draft'))] + domain_move_out

                incoming = dict((item['product_id'][0], item['product_qty']) for item in
                                Move.read_group(domain_move_in_todo, ['product_id', 'product_qty'], ['product_id']))
                outgoing = dict((item['product_id'][0], item['product_qty']) for item in
                                Move.read_group(domain_move_out_todo, ['product_id', 'product_qty'], ['product_id']))
                on_hand = dict((item['product_id'][0], item['quantity']) for item in
                               Quant.read_group(domain_quant, ['product_id', 'quantity'], ['product_id']))

                on_hand_qty = product_details.get('qty_available') or 0.0
                in_hand_qty = product_details.get('incoming_qty') or 0.0
                out_going_qty = product_details.get('outgoing_qty') or 0.0

                vals = {
                    'stock_location_id': a.id,
                    'on_hand_qty': on_hand.get(pro.id, 0.0),
                    'incoming_qty': incoming.get(pro.id, 0.0),
                    'out_qty': outgoing.get(pro.id, 0.0),
                    'custom_product_id': pro.id,
                    'forcasted_qty': (on_hand.get(pro.id, 0.0)) + (
                                incoming.get(pro.id, 0.0) - outgoing.get(pro.id, 0.0)),
                }

                search_record = self.env['stock.location.product'].search(
                    [('custom_product_id', '=', pro.id), ('stock_location_id', '=', a.id)])
                if search_record:
                    search_record = search_record[0]
                    search_record.write(vals)

                else:
                    res = self.env['stock.location.product'].create(vals)

    def update_the_stock_by_date(self):
        dict_pro = self._product_available()
        product_details = dict_pro.get(self.id)

        s_date = self.start_date
        e_date = self.end_date

        if (s_date and e_date) is False:
            self.remove_filter()
        else:
            loc = self.env['stock.location'].search([('usage', '=', 'internal')])
            result = []
            created_ids = []
            for pro in self:
                for a in loc:

                    domain_quant = [('product_id', '=', pro.id), ('location_id', '=', a.id), ('in_date', '<=', e_date),
                                    ('in_date', '>=', s_date)]
                    domain_move_in = [('product_id', '=', pro.id), ('location_dest_id', '=', a.id), ('date', '<=', e_date),
                                      ('date', '>=', s_date)]
                    domain_move_out = [('product_id', '=', pro.id), ('location_id', '=', a.id), ('date', '<=', e_date),
                                       ('date', '>=', s_date)]
                    Move = self.env['stock.move']
                    Quant = self.env['stock.quant']
                    domain_move_in_todo = [('state', 'not in', ('done', 'cancel', 'draft'))] + domain_move_in
                    domain_move_out_todo = [('state', 'not in', ('done', 'cancel', 'draft'))] + domain_move_out

                    incoming = dict((item['product_id'][0], item['product_qty']) for item in
                                    Move.read_group(domain_move_in_todo, ['product_id', 'product_qty'], ['product_id']))
                    outgoing = dict((item['product_id'][0], item['product_qty']) for item in
                                    Move.read_group(domain_move_out_todo, ['product_id', 'product_qty'], ['product_id']))
                    on_hand = dict((item['product_id'][0], item['quantity']) for item in
                                   Quant.read_group(domain_quant, ['product_id', 'quantity'], ['product_id']))

                    on_hand_qty = product_details.get('qty_available') or 0.0
                    in_hand_qty = product_details.get('incoming_qty') or 0.0
                    out_going_qty = product_details.get('outgoing_qty') or 0.0

                    vals = {
                        'stock_location_id': a.id,
                        'on_hand_qty': on_hand.get(pro.id, 0.0),
                        'incoming_qty': incoming.get(pro.id, 0.0),
                        'out_qty': outgoing.get(pro.id, 0.0),
                        'custom_product_id': pro.id,
                        'forcasted_qty': (on_hand.get(pro.id, 0.0)) + (
                                    incoming.get(pro.id, 0.0) - outgoing.get(pro.id, 0.0)),
                    }

                    search_record = self.env['stock.location.product'].search(
                        [('custom_product_id', '=', pro.id), ('stock_location_id', '=', a.id)])
                    if search_record:
                        search_record = search_record[0]
                        search_record.write(vals)

                    else:
                        res = self.env['stock.location.product'].create(vals)

