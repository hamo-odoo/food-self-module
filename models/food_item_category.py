from odoo import fields,models
class FoodItemCategory(models.Model):
    _name="food.item.category"
    _description="Item Category"
    name=fields.Char(required=True)
    # resturant_id=fields.Many2one("food.resturant")