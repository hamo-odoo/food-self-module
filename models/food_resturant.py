from odoo import models,fields

class FoodResturant(models.Model):
    _name="food.resturant"
    _description="Resturant Model"
    name=fields.Char(required=True)
    description=fields.Text()
    address=fields.Char()
    city=fields.Char()
    pincode=fields.Integer()
    owner_id=fields.Many2one("res.users")
    staff_ids=fields.Many2many("res.users")