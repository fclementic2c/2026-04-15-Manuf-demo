# Design Document: Custom Report Header Layout

## 1. Overview
Enlarges the company logo to 300px width and aligns it to the left side of the PDF report header.

## 2. Technical Strategy
Inherits `web.external_layout_standard` and applies inline styles via XPath attributes to override default Odoo sizing constraints.
