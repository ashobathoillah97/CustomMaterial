# -*- coding: utf-8 -*-

from odoo import fields, models, api

class CustomSupplier(models.Model):
    _name = "custom.supplier"
    _description = 'supplier'

    name = fields.Char(string='Name')