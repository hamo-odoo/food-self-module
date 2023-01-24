from odoo import fields,models

class FoodDeliveryPartner(models.Model):
    _name="food.delivery.partner"
    name=fields.Char(required=True)
    active=fields.Boolean(default=True)
    all_order_ids=fields.One2many("food.order","delivery_partner_id")
    pay_type=fields.Selection([('fixed','Fixed'),('per_km','Per Kilometer'),('per_delivery','Per Delivery')])
    current_order_assigned=fields.Many2one("food.order",readonly=True)
