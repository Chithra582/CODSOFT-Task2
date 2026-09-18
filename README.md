# CODSOFT Task 2 — Gourmet Dessert Landing Page 🍨

[![Spec: OpenGAP v0.1.0](https://img.shields.io/badge/spec-OpenGAP%20v0.1.0-blue)](https://github.com/open-gitagent/opengap)
[![Passport: Certified](https://img.shields.io/badge/HiDevs%20GitAgent%20Passport-Approved-purple)](https://app.hidevs.xyz/passport)
[![Category: Developer Tools](https://img.shields.io/badge/category-Developer%20tools-green)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> An interactive e-commerce and retail dessert landing page and OpenGAP-compliant storefront agent created by **Chithra R**.

---

## 🛡️ GitAgent Passport Checkpoint Compliance

| Checkpoint | Status | Details |
|---|---|---|
| **01. Validate** | ✅ **Passed** | Manifest in `agent.yaml` compliant with OpenGAP spec `0.1.0` in the **Developer tools** domain. |
| **02. Explain** | ✅ **Passed** | Complete `EXPLAINABILITY.md` covering decision logic, catalog lineage, recommendation rubrics, and privacy boundaries. |
| **03. Export** | ✅ **Passed** | 4 Framework Visas earned (**OpenAI SDK**, **CrewAI**, **Claude Code**, and **Lyzr**). |

---

## 🗂️ Agent Repository Structure

```
CODSOFT-Task2/
├── agent.yaml              # OpenGAP manifest (v0.1.0)
├── SOUL.md                 # Agent persona, storefront identity & retail values
├── RULES.md                # Hard constraints, pricing rules & privacy checks
├── DUTIES.md               # Segregation of duties policy & role boundaries
├── AGENTS.md               # Universal fallback agent instructions
├── EXPLAINABILITY.md       # Decision mechanics, catalog lineage & boundaries
├── index.html              # Clean portal entry with Passport badges
├── agent.py                # Validation runner, framework exporter & CLI
├── LICENSE                 # MIT License
│
├── CODSOFT Task2/          # Landing Page Source
│   ├── landingpage.html    # Interactive Dessert Landing Page
│   └── landing page style.css # CSS Styles & Grid Layouts
│
├── images/                 # Product Photography & Visual Assets
│
├── skills/                 # Capability modules
│   ├── product-catalog-retrieval/
│   │   └── SKILL.md
│   ├── pricing-offer-calculator/
│   │   └── SKILL.md
│   └── inquiry-order-routing/
│       └── SKILL.md
│
├── tools/                  # MCP-compatible tool definitions
│   ├── get-flavour-catalog.yaml
│   ├── calculate-order-offer.yaml
│   └── submit-customer-inquiry.yaml
│
└── adapters/               # Framework export targets for Passport Visas
    ├── openai_agent.py     # OpenAI Agents SDK export
    ├── crewai_agent.py     # CrewAI agent export
    ├── claude_code.json    # Claude Code configuration
    └── lyzr_agent.py       # Lyzr Studio adapter
```

---

## 🚀 Quick Start

### 1. View Landing Page
Open `index.html` or `CODSOFT Task2/landingpage.html` directly in any web browser.

### 2. Run OpenGAP Agent Validation
```bash
python agent.py --validate
```

### 3. Framework Exports (Visas)
```bash
python agent.py --export all
```

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).
