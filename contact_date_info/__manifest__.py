{
    'name': 'Contact Date Extension',
    'version': '19.0.1.0.0',
    'category': 'Contacts',
    'summary': 'Adds a contact date field to the partner form view.',
    'description': """
        Contact Date Extension
        ======================
        This module adds a new Date field to the Contact (res.partner) model
        and displays it right below the contact name.
    """,
    'author': 'Odoo Custom Module',
    'depends': ['base', 'contacts'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
