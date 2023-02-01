from odoo import http

class FoodController(http.Controller):
    @http.route('/food')
    def index(self,**kwargs):
        return http.request.render('food-self-module.a',{'resturants':http.request.env['food.resturant'].search([])})