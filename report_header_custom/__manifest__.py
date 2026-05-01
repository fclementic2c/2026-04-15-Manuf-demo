{
    'name': 'Custom Report Header Layout',
    'version': '19.0.1.0.0',
    'category': 'Technical',
    'summary': 'Enlarge company logo to 300px and align left in PDF reports.',
    'description': """
        Custom Report Header Layout
        ===========================
        This module inherits the standard Odoo report layout to:
        - Enlarge the company logo to 300px.
        - Align the logo to the left.
        - Ensure company address alignment does not conflict.
    """,
    'author': 'Odoo Custom Module',
    'depends': ['web'],
    'data': [
        'views/report_templates.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
