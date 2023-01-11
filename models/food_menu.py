from odoo import fields,models

class FoodMenu(models.Model):
    _name="food.menu"
    _description="Menu Model"
    resturant_id=fields.Many2one("food.resturant")
    item_ids=fields.One2many("food.item","menu_id")
