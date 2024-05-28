from odoo import models, fields

class Supplier(models.Model):
    _name = 'supplier'
    _description = 'Supplier'

    name = fields.Char(string='Name', required=True)
