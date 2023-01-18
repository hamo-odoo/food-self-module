from odoo import fields,models

class FoodOrder(models.Model):
    _name="food.order"
    _description="Food Description"
    customer_id=fields.Many2one("res.partner")
    resturant_id=fields.Many2one("food.resturant")
    order_line_ids=fields.One2many("food.order.line","order_id")