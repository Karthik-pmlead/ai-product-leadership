# Architecture Decision Records

This document captures the main design choices for the message-routing agent, including their trade-offs.

## ADR-001: Use an LLM for Intent Classification

**Decision:** Use an OpenRouter language model through the n8n AI Agent.

**Reason:** Inbound messages are unstructured and may express the same intent in different ways. Semantic interpretation is more flexible than fixed keyword matching.

**Trade-off:** LLM outputs can be inconsistent, require evaluation, and introduce latency and usage costs.

**Mitigation:** Use explicit intent definitions, representative test cases, and output validation.

## ADR-002: Use n8n for Orchestration

**Decision:** Use n8n to connect the message trigger, AI Agent, model, and destination tools.

**Reason:** Visual orchestration enables rapid prototyping and makes integrations easier to inspect.

**Trade-off:** Complex branching, testing, versioning, and reliability controls can become harder to manage as workflows grow.

**Mitigation:** Keep routing rules explicit and document failure handling and execution behavior.

## ADR-003: Use Google Sheets as the Initial Data Store

**Decision:** Store routed messages in separate Google Sheets destinations for Sales, Support, and Spam.

**Reason:** Simple to configure, inspect, and demonstrate without building a custom database.

**Trade-off:** Sheets may not provide the transactional guarantees, concurrency handling, or scale needed for production workloads.

**Mitigation:** Evaluate a database or ticketing/CRM integration if the use case expands.

## ADR-004: Separate Intent Categories by Business Destination

**Decision:** Define three initial categories: Demo/Sales, Support, and Spam.

**Reason:** The categories map directly to the business actions the prototype must perform.

**Trade-off:** Mixed-intent or unclear messages may not fit neatly into one category.

**Mitigation:** Define fallback behavior and add categories only when supported by actual use cases and evaluation results.

## ADR-005: Treat Exactly-One Routing as a System Requirement

**Decision:** Require one intended destination write per message.

**Reason:** Multiple writes can create duplicate work, while incorrect routing can delay customer responses.

**Trade-off:** A prompt instruction alone cannot guarantee this behavior during retries or partial failures.

**Mitigation:** Validate the selected destination, track a stable message ID, and implement idempotent write handling where supported.

## Review Status

These decisions describe the prototype's design rationale and recommended safeguards. Verify each safeguard against the actual n8n implementation before marking it complete.
