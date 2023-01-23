from odoo import fields,models

class FoodDeliveryPartner(models.Model):
    _inherits={"res.users":"user_id"}
    _name="food.delivery.partner"
    user_id=fields.Many2one("res.users")
    pay_type=fields.Selection([('fixed','Fixed'),('per_km','Per Kilometer'),('per_delivery','Per Delivery')])