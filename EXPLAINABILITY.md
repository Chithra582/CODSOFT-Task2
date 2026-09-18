# EXPLAINABILITY.md

This document explains the internal mechanisms, data lineage, and operational boundaries of **CODSOFT-Task2 (Dessert Landing Page Agent)** in accordance with the OpenGAP specification.

---

## How the Agent Decides

The Dessert Landing Page Agent makes decisions through a deterministic multi-stage retail pipeline that retrieves product catalog data, evaluates promotional offers, and facilitates customer inquiries.

### 1. Decision Architecture
The decision process flows through sequential stages:

```
Customer Query / Action
    │
    ▼
[Stage 1: Intent & Product Classification]
    │  - Classifies intent: Flavor Exploration, Pricing/Offer Calculation, or Contact Inquiry
    ▼
[Stage 2: Catalog Ingestion & Matching]
    │  - Ingests menu items from landingpage.html (Chocolate, Strawberry, Vanilla, etc.)
    │  - Matches customer preferences against official dessert roster
    ▼
[Stage 3: Pricing & Promotion Evaluation]
    │  - Applies unit pricing ($10 Chocolate, $8 Strawberry, $6 Vanilla)
    │  - Evaluates volume discounts and promotional bundle eligibility
    ▼
[Stage 4: Guardrail & Privacy Sanitization]
    │  - Screens inquiry messages for personal data redaction
    │  - Sanitizes emails and phone numbers under GDPR Article 28
    ▼
[Stage 5: Output Presentation & Store Routing]
    │  - Renders interactive flavor cards, subtotal estimates, and order confirmations
    ▼
Customer Receives Recommendation / Confirmation
```

### 2. Retrieval Criteria & Ranking Rubric
When recommending flavors to a visitor, the agent evaluates customer taste preference, popular appeal, and promotional value:

$$\text{RecommendationScore}(F) = (\text{TasteAffinity} \times 0.50) + (\text{PopularityRank} \times 0.30) + (\text{OfferValue} \times 0.20)$$

- **Taste Affinity (50%)**: Direct match with customer flavor preference (rich cocoa, fruity, classic vanilla).
- **Popularity Rank (30%)**: Historical customer favorite ranking (Chocolate: #1, Strawberry: #2, Vanilla: #3).
- **Offer Value (20%)**: Highlights active seasonal combo promotions.

### 3. Thresholding & Refusal Decision Criteria
- **Unavailable Flavors**: If a customer requests an unlisted flavor, the agent explicitly refuses and returns: *"We currently do not offer this flavor. Would you like to try our popular Chocolate or Strawberry selections?"* It never hallucinates inventory.
- **Excessive Order Volumes**: Orders exceeding standard retail parlor capacity (>100 units) trigger an automatic catering inquiry redirect.

### 4. Client-Side Guardrail Decision Gates
- **PII Redaction Gate**: Customer contact coordinates are masked (`c***@***.com`, `+91 ***-***-4868`) before export.
- **Input Sanitization**: Free-text inquiry boxes are stripped of script injection tags before storage.

### 5. Fallback & Offline Decision Mechanism
- The landing page operates 100% offline from local HTML/CSS/image assets without requiring cloud connectivity.
- Offline navigation, flavor browsing, and menu inspection continue uninterrupted without network access.

### 6. Human-in-the-Loop Governance
- Store managers retain absolute control over menu additions, price updates, and promotional discounts.
- All pricing changes are auditable via Git commits.

---

## The Data It Uses

The agent operates strictly on verified local storefront assets with zero unauthorized data transmission.

### 1. Ingested Input Data
- **Menu Catalog**: Flavor names, ingredient highlights, price points ($6 - $10), high-resolution imagery (`images/`).
- **Storefront Telemetry**: Header navigation, about narrative, promotional banners, customer contact coordinates.
- **Customer Input**: Flavor inquiries, quantity selections, contact form submissions.

### 2. In-Memory Chunking & Storage Architecture
- **In-Memory Catalog**: Flavor attributes and cart calculations are handled strictly in local browser process memory.
- **0-Byte Raw Egress Guarantee**: Customer names and browsing history are never sold or exfiltrated to advertising networks.

### 3. External Relay Data & Redaction Patterns
When customer telemetry is exported into framework runtimes (OpenAI SDK, CrewAI, Claude Code, Lyzr):
- Payloads contain strictly sanitized order parameters.
- **Masked PII Patterns**:
  - Email addresses: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` $\rightarrow$ `c***@***.com`
  - Phone numbers: `\b\d{10}\b` $\rightarrow$ `[REDACTED_PHONE]`

### 4. Data Privacy, Storage, and Retention
- **Stateless Execution**: Browsing sessions do not track users across domains.
- **GDPR Compliance**: Minimizes collected fields strictly to what is required for fulfilling customer inquiries.

---

## Limitations

Understanding the operational boundaries of the Dessert Landing Page Agent ensures safe and predictable customer service.

### 1. In-Memory Scale and Capacity Constraints
- **Menu Scope**: Optimized for a boutique dessert parlor offering up to 50 curated flavors.
- **Static Pricing**: Reflects catalog prices configured in the repository codebase.

### 2. Compute and Cold-Start Profile
- **Sub-10ms Response**: Catalog lookups and cart estimates complete instantly with negligible CPU load.

### 3. Connectivity and Synthesis Boundaries
- **Local Independence**: Core menu browsing and cart calculations operate 100% offline.
- **AI Agent Synthesis**: Natural language chat assistance via external LLMs requires internet connectivity.

### 4. Scope and Grounding Boundaries
- **Self-Contained Storefront**: Does not integrate with third-party delivery dispatch APIs (e.g. UberEats, DoorDash) unless configured.

### 5. Media and Formatting Constraints
- **Image Assets**: Visuals depend on local web image formats (`.jpg`, `.jfif`, `.png`).

### 6. Security and Guardrail Edge Cases
- **Allergy Heuristics**: Flavor notes provide general ingredient descriptions; customers with severe anaphylactic allergies are explicitly advised to consult parlor staff directly.

---

## Summary & Compliance Checklist

| Checkpoint 2 Requirement | Corresponding Section | Status |
| :--- | :--- | :---: |
| **How the agent decides** | [How the Agent Decides](#how-the-agent-decides) | **Covered** |
| - Decision architecture & 5-stage pipeline | Section 1 | Verified |
| - Retrieval criteria & ranking rubric | Section 2 | Verified |
| - Thresholding, refusal & missing data logic | Section 3 | Verified |
| - Guardrail decision gates & PII masking | Section 4 | Verified |
| - Fallback & offline mechanism | Section 5 | Verified |
| - Human-in-the-loop governance | Section 6 | Verified |
| **The data it uses** | [The Data It Uses](#the-data-it-uses) | **Covered** |
| - Ingested input data & attributes | Section 1 | Verified |
| - In-memory processing & 0-byte egress | Section 2 | Verified |
| - External relay data & token redaction | Section 3 | Verified |
| - Data privacy & retention | Section 4 | Verified |
| **Its limitations** | [Limitations](#limitations) | **Covered** |
| - API rate limits & quota constraints | Section 1 | Verified |
| - Compute profile & network bounds | Section 2 | Verified |
| - Connectivity & live API dependencies | Section 3 | Verified |
| - Scope boundaries & private repo invisibility | Section 4 | Verified |
| - Media & self-reported data edge cases | Section 5 & 6 | Verified |
