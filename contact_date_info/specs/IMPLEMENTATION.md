# Implementation Plan - Contact Date Extension

This document outlines the phased approach for scaffolding and implementing the `contact_date_info` module for Odoo 19.0.

## Phase 1: Module Skeleton & Metadata
- [ ] Create the module root directory: `contact_date_info`.
- [ ] Create the standard Odoo directory structure:
    - `models/`
    - `views/`
    - `security/`
    - `data/`
    - `wizards/`
    - `controllers/`
    - `static/src/js/`, `static/src/css/`, `static/src/xml/`
    - `static/description/`
    - `reports/`
    - `tests/`
- [ ] Generate empty `__init__.py` files in:
    - Root directory
    - `models/`
- [ ] Generate the `__manifest__.py` file:
    - Name: "Contact Date Extension"
    - Version: "19.0.1.0.0"
    - Category: "Contacts"
    - Depends: `['base', 'contacts']`
    - Data order: `security/ir.model.access.csv` (if needed), `views/res_partner_views.xml`
    - Include `assets` and `demo` keys.
- [ ] Generate a standard `pyproject.toml` configured for `whool`.
- [ ] Initialize git (if not present) and commit the skeleton.
- [ ] **Post-Phase Check:** Update Journal, check formatting, and verify XML IDs.

## Phase 2: Data Model Implementation
- [x] Create `models/res_partner.py`.
- [x] Implement `_inherit = 'res.partner'`.
- [x] Add `contact_date = fields.Date(string="Contact Date")`.
- [x] Update `models/__init__.py` to import `res_partner`.
- [ ] **Post-Phase Check:** Ensure `self.ensure_one()` in any methods (if added later), "One File = One Model", update Journal, and request commit approval.

## Phase 3: UI/UX Implementation
- [ ] Create `views/res_partner_views.xml`.
- [ ] Inherit `base.view_partner_form`.
- [ ] XPath the `name` field to add `contact_date` after it.
- [ ] **Post-Phase Check:** Validate XML structure, update Journal, and request commit approval.

## Phase 4: Finalization & Documentation
- [ ] Create `README.md` following OCA standards.
- [ ] Perform a final audit of the code structure.
- [ ] **Post-Phase Check:** Update Journal and request final user inspection.

---

## Journal
| Date | Phase | Notes | Deviations / Surprises |
| :--- | :--- | :--- | :--- |
| 2026-05-01 | Setup | Initialized Implementation Plan | N/A |
| 2026-05-01 | Phase 2 | Implemented res.partner inheritance and added contact_date field. | None. |\n