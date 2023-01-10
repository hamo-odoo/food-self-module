from odoo import fields,models

class FoodResturantTag(models.Model):
    _name="food.resturant.tag"
    _description="Resturant Tag"
    name=fields.Char(required=True)