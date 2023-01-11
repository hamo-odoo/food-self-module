from odoo import models,fields

class FoodResturant(models.Model):
    _name="food.resturant"
    _description="Resturant Model"
    name=fields.Char(required=True)
    description=fields.Text()
    address=fields.Char()
    city=fields.Char(required=True)
    pincode=fields.Integer(required=True)
    owner_id=fields.Many2one("res.users")
    staff_ids=fields.Many2many("res.users")
    tag_ids=fields.Many2many("food.resturant.tag")