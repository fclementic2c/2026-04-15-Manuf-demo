{
    'name': 'Patrick Concept - Job Costing Odoo 19',
    'version': '19.0.1.0.0',
    'category': 'Manufacturing/Manufacturing',
    'summary': 'Module de démo pour machines uniques à 7 niveaux de BOM',
    'description': 'Gestion de production à l\'affaire avec valorisation FIFO et analytique strict.',
    'author': 'Expert Odoo 19',
    'depends': ['mrp', 'analytic', 'stock_account', 'purchase', 'sale_management'],
    'data': [
        'data/analytic_data.xml',
        'data/workcenter_data.xml',
        'data/product_data.xml',
        'data/bom_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'OEEL-1',
}
