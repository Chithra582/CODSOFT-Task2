"""
OpenAI SDK Export Adapter for CODSOFT-Task2 Dessert Landing Page Agent
Generated in compliance with OpenGAP spec v0.1.0
"""

import json
from typing import Any, Dict

SYSTEM_PROMPT = """You are Dessert Landing Page Agent, an autonomous e-commerce retail copilot representing Tasty & Delicious Ice Cream.
Your role is to guide customers through dessert flavors (Chocolate $10, Strawberry $8, Vanilla $6), compute order subtotals and discounts,
and process customer inquiries with privacy protection."""

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_flavour_catalog",
            "description": "Returns active dessert flavors with descriptions and prices",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {"type": "string"}
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_order_offer",
            "description": "Calculates order total and applies promotional discounts",
            "parameters": {
                "type": "object",
                "properties": {
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "flavour": {"type": "string"},
                                "quantity": {"type": "integer"}
                            }
                        }
                    }
                },
                "required": ["items"]
            }
        }
    }
]

def export_openai_spec() -> Dict[str, Any]:
    return {
        "model": "gpt-4o-mini",
        "temperature": 0.2,
        "max_tokens": 4096,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT}
        ],
        "tools": TOOLS
    }

if __name__ == "__main__":
    print("[SUCCESS] Exported Dessert Landing Page Agent for OpenAI SDK:")
    print(json.dumps(export_openai_spec(), indent=2))
