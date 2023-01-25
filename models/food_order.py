from odoo import fields,models,api,_
from odoo.exceptions import UserError,ValidationError
class FoodOrder(models.Model):
    _name="food.order"
    _description="Food Description"
    customer_id=fields.Many2one("res.partner")
    resturant_id=fields.Many2one("food.resturant")
    order_line_ids=fields.One2many("food.order.line","order_id")
    state=fields.Selection([('new','New'),('accepted','Accepted'),('dp_assigned','Delivery Partner Assigned'),('picked','Picked'),('delivered','Delivered'),('canceled','Canceled')],default='new',compute="_onchange_delivery_id",readonly=False,store=True)
    delivery_partner_id=fields.Many2one("food.delivery.partner",)
    total_price=fields.Float(compute="_compute_total_price",default=0)
    def name_get(self):
        res=[]
        for record in self:
            res.append((record.id,'Food order id:%s'%record.id))
        return res
    @api.depends("order_line_ids")
    def _compute_total_price(self):
        for record in self:
            net_prices=record.order_line_ids.mapped("net_price")
            record.total_price=sum(net_prices)
    def action_state_accepted(self):
        for record in self:
            record.state='accepted'
            self.auto_search_partner()
    def action_state_canceled(self):
        for record in self:
            record.state='canceled'
    @api.depends("delivery_partner_id")
    def _onchange_delivery_id(self):
        for record in self:
            dp=record.delivery_partner_id
            dp.current_order_assigned=record.id
            record.state='dp_assigned'
    @api.constrains("delivery_partner_id")
    def _check_delivery_partner(self):
        for record in self:
            cao=record.delivery_partner_id.current_order_assigned
            if cao and cao!=record:
                raise ValidationError(_("Delivery partner cannot be assigned"))
    def auto_search_partner(self):
        for record in self:
            dp=self.env['food.delivery.partner'].search([('current_order_assigned','=',False)])
            if not dp:
                raise UserError(_("All delivery partner are busy please try after sometime!"))
            record.delivery_partner_id=dp[0].id
            dp[0].current_order_assigned=record.id
            record.state='dp_assigned'
