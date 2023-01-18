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
    tag_ids=fields.Many2many("food.resturant.tag","resturant_tag_rel","resturant_id","tag_id")
    item_ids=fields.One2many("food.item","resturant_id")
    #category_ids=fields.One2many(realted="item_ids.category_id")