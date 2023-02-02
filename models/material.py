# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError

class CustomMaterial(models.Model):
    _name = "custom.material"
    _description = 'material information'

    currency_id = fields.Many2one('res.currency', string='Currency')
    supplier_id = fields.Many2one('custom.supplier', string='Supplier', required=True)

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    type = fields.Selection([('fabric','Fabric'),('jeans','Jeans'),('cotton','Cotton')],string='Type', required=True)
    price = fields.Float(string="Price",currency_id='currency_id', required=True)

    @api.onchange('price')
    def price_onchange(self):
        for rec in self:
            if rec.price and rec.price > 100:
                raise ValidationError('Price limit is 100')