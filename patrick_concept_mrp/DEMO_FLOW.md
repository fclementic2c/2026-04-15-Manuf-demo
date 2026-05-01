# Démo Patrick Concept - Odoo 19 Job Costing

## Données de Base
- **Projet Analytique** : PC-2026-001 (lié au plan principal).
- **Articles** :
    - `EC-MACHINE-ULTRA` : Produit fini (Niveau 1).
    - `EC-SUB-L2` à `EC-SUB-L7` : Sous-ensembles fabriqués (7 niveaux au total).
    - `AC-MOTEUR-SPEC` : Composant acheté spécifique.
    - `DIN-VIS-M8` : Quincaillerie normée.
- **Valorisation** : Catégorie 'Affaire' configurée en FIFO / Temps Réel.

## Scénario de Démo
1. **Initialisation** : Le compte analytique `PC-2026-001` est créé automatiquement.
2. **Vente** : Créer un bon de commande pour `EC-MACHINE-ULTRA`. Assigner le compte analytique.
3. **Explosion de BOM** : Confirmer la vente génère les OF. Vérifier la hiérarchie des 7 niveaux dans le rapport de structure de nomenclature.
4. **Approvisionnement** : Acheter l'article `AC-MOTEUR-SPEC`. La réception valorise le stock instantanément (FIFO).
5. **Production** : Consommer les articles dans les OF. Les coûts sont poussés vers l'analytique.
6. **Marge** : Analyser le rapport de rentabilité du projet.

## Configurations Techniques Odoo 19
- **Analytique** : Utilisation obligatoire du `plan_id`.
- **Logistique** : `type="consu"` utilisé pour le suivi d'inventaire valorisé.
- **MRP** : Suppression du champ `capacity` dans les postes de travail.
