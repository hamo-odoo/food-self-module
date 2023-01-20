from odoo import fields,models,api

class FoodOrder(models.Model):
    _name="food.order"
    _description="Food Description"
    customer_id=fields.Many2one("res.partner")
    resturant_id=fields.Many2one("food.resturant")
    order_line_ids=fields.One2many("food.order.line","order_id")
    state=fields.Selection([('new','New'),('accepted','Accepted'),('dp_assigned','Delivery Partner Assigned'),('picked','Picked'),('delivered','Delivered'),('canceled','Canceled')],default='new',compute="_onchange_delivery_partner",readonly=False,store=True)
    delivery_partner_id=fields.Many2one("res.users")
    total_price=fields.Float(compute="_compute_total_price",default=0)
    @api.depends("order_line_ids")
    def _compute_total_price(self):
        for record in self:
            net_prices=record.order_line_ids.mapped("net_price")
            record.total_price=sum(net_prices)
    def action_state_accepted(self):
        for record in self:
            record.state='accepted'
    def action_state_canceled(self):
        for record in self:
            record.state='canceled'
    @api.depends("delivery_partner_id")
    def _onchange_delivery_partner(self):
        for record in self:
            record.state='dp_assigned' if record.delivery_partner_id else record.state