from odoo import models,fields

class EstateProperty(models.Model):
       _name = "estate.property"
       _description = "Real Estate Property"
    
       #Fields
       name = fields.Char(required=True, string="Property Name")
       description = fields.Text(string="Description")
       postcode = fields.Char(string="Postcode")
       date_availability = fields.Date(string="Availability Date")
       expected_price = fields.Float(required=True, string="Expected Price")
       bedrooms = fields.Integer(string="Bedrooms")
       living_area = fields.Integer(string="Living Area (m2)")
       garage = fields.Boolean(string="Has Garage")
       garden = fields.Boolean(string="Has Garden")
       state = fields.Selection(
              selection=[
              ('new', 'New'),
              ('sold', 'Sold'),
              ('canceled', 'Canceled'),
              ],
              string="Status",
              default='new'
       )