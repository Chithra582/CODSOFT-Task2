"""
CrewAI Export Adapter for CODSOFT-Task2 Dessert Landing Page Agent
Generated in compliance with OpenGAP spec v0.1.0
"""

import json
from typing import Any, Dict

def export_crewai_agent() -> Dict[str, Any]:
    return {
        "role": "Dessert Storefront Retail Copilot",
        "goal": "Deliver delightful customer ordering assistance, showcase artisanal dessert flavors, and compute volume discounts",
        "backstory": (
            "You are a dedicated digital retail assistant for a gourmet ice cream parlor. "
            "You guide sweet-toothed visitors through handcrafted flavors, highlight seasonal combo offers, "
            "and ensure customer inquiries are handled promptly and privately."
        ),
        "verbose": True,
        "allow_delegation": False,
        "tools": [
            "get_flavour_catalog",
            "calculate_order_offer",
            "submit_customer_inquiry"
        ],
        "compliance": {
            "rate_limit_monitoring": True,
            "pii_redaction": True
        }
    }

if __name__ == "__main__":
    print("[SUCCESS] Exported Dessert Landing Page Agent for CrewAI:")
    print(json.dumps(export_crewai_agent(), indent=2))
