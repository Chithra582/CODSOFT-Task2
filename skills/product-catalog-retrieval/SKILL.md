---
name: product-catalog-retrieval
description: Retrieves and displays dessert flavors, pricing, ingredients, and visual assets from the store catalog
---

# Product Catalog Retrieval Skill

## Purpose
Query and present available dessert menu items, unit prices, and descriptions.

## Capabilities
- Ingest flavor inventory from `CODSOFT Task2/landingpage.html`.
- Display high-resolution images, tasting notes, and prices ($6 - $10).
- Categorize treats into ice cream scoops, sundaes, and seasonal specials.

## Execution Guidelines
1. Ingest flavor identifier from customer query.
2. Lookup corresponding menu record.
3. Return structured product card with price and description.
