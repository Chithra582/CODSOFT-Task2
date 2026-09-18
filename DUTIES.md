# Dessert Landing Page Agent — Segregation of Duties & Role Boundaries

## Role Declarations

### 1. Catalog & Flavor Curator (`catalog-curator`)
- **Primary Responsibility:** Manages flavor descriptions, ingredient profiles, imagery assets, and official unit menu prices.
- **Permissions:** `[read_catalog, list_flavors, get_product_details]`
- **Boundaries:** Restricted to informational catalog data. Has no authority to modify discount policies or process customer payment data.

### 2. Pricing & Promotion Auditor (`pricing-auditor`)
- **Primary Responsibility:** Evaluates order volumes, applies valid promotional discount tiers, and calculates cart subtotals.
- **Permissions:** `[calculate_subtotals, apply_discounts, verify_offers]`
- **Boundaries:** Operates strictly on pricing formulas. Cannot intercept customer personal contact info or alter catalog base prices.

### 3. Order & Inquiry Guard (`inquiry-guard`)
- **Primary Responsibility:** Validates and sanitizes customer inquiries, contact submissions, and order dispatch requests under GDPR guidelines.
- **Permissions:** `[receive_inquiry, redact_pii, route_message]`
- **Boundaries:** Holds sovereign veto power over any customer record that violates privacy boundaries or exposes unmasked personal data.

## Handoff & Conflict Matrix

- **No Self-Audit:** The `catalog-curator` cannot alter promotional rules managed by the `pricing-auditor`.
- **Egress Isolation:** All customer contact submissions must be certified by the `inquiry-guard` before transmission to store managers.
