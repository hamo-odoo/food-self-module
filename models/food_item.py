from odoo import fields,models

class FoodItem(models.Model):
    _name="food.item"
    _description="Food Item Model"
    name=fields.Char(required=True)
    price=fields.Integer(required=True)
    category_id=fields.Many2one("food.item.category")
    menu_id=fields.Many2one("food.menu")
    type=fields.Selection(selection=[('veg','Veg'),('nonveg','Non-Veg')],default="veg")