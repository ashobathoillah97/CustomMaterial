# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

class WebsiteEventController(http.Controller):

    @http.route(['/material'], type='http', auth="user", website=True, multilang="True")
    def sale_data(self, **post):
        custom_material = request.env['custom.material'].sudo()
        values = {'records': custom_material}

        return request.render("custom_material.material_view", values)