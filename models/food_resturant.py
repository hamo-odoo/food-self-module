from odoo import models,fields,api

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
    order_ids=fields.One2many("food.order","resturant_id")
    total_order=fields.Integer(compute="_compute_total_order")
    @api.depends("order_ids")
    def _compute_total_order(self):
        for record in self:
            record.total_order=len(record.order_ids)
    