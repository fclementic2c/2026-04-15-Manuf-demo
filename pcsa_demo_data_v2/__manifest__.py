# -*- coding: utf-8 -*-
{
    'name': 'PCSA Demo Data (Corrected)',
    'version': '1.2',
    'category': 'Manufacturing',
    'summary': 'Données de démo pour PCSA - Gestion à l\'affaire (Corrigé)',
    'description': """
        Module de démonstration pour Patrick Concept SA.
        Correction de l\'erreur mrp.workcenter (field capacity).
        Incorpore les conventions EC/AC/DIN et le suivi analytique.
    """,
    'author': 'Gemini for PCSA',
    'depends': ['mrp', 'analytic', 'stock_account'],
    'data': [
        'data/analytic_data.xml',
        'data/workcenter_data.xml',
        'data/product_data.xml',
        'data/bom_data.xml',
    ],
    'installable': True,
    'application': False,
}
