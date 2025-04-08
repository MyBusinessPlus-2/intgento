from odoo import models, fields

class CustomForm(models.Model):
    _name = 'custom.form'
    _description = 'Custom Form Submitted from Website'

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    message = fields.Text(string="Message")
