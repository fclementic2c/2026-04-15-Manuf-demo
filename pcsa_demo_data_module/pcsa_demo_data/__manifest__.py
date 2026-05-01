# -*- coding: utf-8 -*-
{
    'name': 'PCSA Demo Data (Gestion à l\'Affaire)',
    'version': '1.0',
    'category': 'Manufacturing',
    'summary': 'Données de démo pour Patrick Concept SA - Gestion à l\'affaire',
    'description': """
        Ce module charge des données de test respectant les spécifications PCSA :
        - Articles avec nomenclature multi-niveaux (7 niveaux théoriques)
        - Conventions de nommage EC/AC/DIN
        - Postes de travail pour opérations manuelles
        - Comptes analytiques pour suivi financier
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
