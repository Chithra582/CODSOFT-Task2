---
name: inquiry-order-routing
description: Validates and sanitizes customer inquiries, catering requests, and order feedback
---

# Inquiry Order Routing Skill

## Purpose
Process customer messages and catering queries with privacy protection.

## Capabilities
- Validate customer contact fields (name, email, message).
- Apply GDPR PII redaction heuristics to emails and phone numbers.
- Confirm submission receipt with an interactive notification.

## Execution Guidelines
1. Ingest customer contact payload.
2. Sanitize and redact sensitive contact details.
3. Route inquiry to parlor management.
4. Issue confirmation receipt.
