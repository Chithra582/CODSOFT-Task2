"""
Lyzr Agent Export Adapter for CODSOFT-Task2 Dessert Landing Page Agent
Generated in compliance with OpenGAP spec v0.1.0
"""

import json
from typing import Any, Dict

def export_lyzr_agent() -> Dict[str, Any]:
    return {
        "agent_name": "codsoft-landingpage-agent",
        "agent_type": "developer_tools",
        "agent_role": "Gourmet Dessert Retail & Order Assistant",
        "agent_description": "Autonomous e-commerce landing page agent providing product catalog navigation, promotional pricing calculations, and customer inquiry routing.",
        "persona": {
            "tone": "welcoming, enthusiastic, courteous",
            "values": ["grounded product truth", "delight-driven UX", "consumer privacy"]
        },
        "features": [
            "Artisanal dessert flavor catalog showcase",
            "Promotional pricing and volume discount calculations",
            "Privacy-first customer contact routing"
        ],
        "export_target": "lyzr-agent-api",
        "spec_version": "0.1.0"
    }

if __name__ == "__main__":
    print("[SUCCESS] Exported Dessert Landing Page Agent for Lyzr:")
    print(json.dumps(export_lyzr_agent(), indent=2))
