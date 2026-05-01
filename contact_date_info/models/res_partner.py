from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    contact_date = fields.Date(
        string="Contact Date",
        help="The specific date associated with this contact."
    )
