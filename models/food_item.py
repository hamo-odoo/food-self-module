from odoo import fields,models

class FoodItem(models.Model):
    _name="food.item"
    _description="Food Item Model"
    name=fields.Char(required=True)
    price=fields.Float(required=True)
    category_id=fields.Many2one("food.item.category")
    resturant_id=fields.Many2one("food.resturant")
    type=fields.Selection(selection=[('veg','Veg'),('nonveg','Non-Veg')])