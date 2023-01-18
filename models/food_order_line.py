from odoo import fields,models,api

class FoodOrderLine(models.Model):
    _name="food.order.line"
    _description="Food Order line"
    order_id=fields.Many2one("food.order")
    item_id=fields.Many2one("food.item",domain="[('resturant_id','=',order_id.resturant_id)]")
    qty=fields.Integer()
    price=fields.Float(related="item_id.price")
    net_price=fields.Float(compute="_compute_net_price")

    @api.depends("qty","price")
    def _compute_net_price(self):
        for record in self:
            record.net_price=float(record.qty)*record.price