# Orchestration Design

## 1. Overview

The platform uses hierarchical orchestration across two n8n workflows:

- **V4 Main Workflow:** User interaction, request coordination, validation, and final response.
- **V3 Execution Workflow:** Specialist-agent delegation and travel research.

This separation keeps the user-facing workflow independent of individual research-agent implementations.

## 2. Execution Sequence

### Stage 1: Request Intake
1. User submits a travel request through the chat interface.
2. Coordinator extracts mandatory trip details and optional preferences.
3. Simple Memory Buffer Window supports conversational context.
4. Structured Output Parser formats the coordinator's response.

### Stage 2: Input Validation
1. Check origin, destination, departure date, and return date.
2. If mandatory information is missing, route to the error-response path.
3. Otherwise, pass the validated request to the Planner.

### Stage 3: Workflow Delegation
1. Planner invokes the V3 execution sub-workflow.
2. Pass the trip request and chat session identifier.
3. V3 receives the request through its workflow trigger.

### Stage 4: Specialist Execution
The Travel Orchestrator coordinates three specialist agents:

- Flights Agent: flight research.
- Hotels Agent: accommodation research.
- Activities Agent: local attractions and experience research.

Each agent uses its designated external search tools.

### Stage 5: Consolidation and Validation
1. Travel Orchestrator combines specialist findings.
2. Results return to the V4 workflow.
3. Validator and Summarizer reviews consistency and curates the recommendations.
4. Final response is returned through the chat interface.

## 3. Workflow Boundaries

| Workflow | Owns | Does not own |
|---|---|---|
| V4 Main | Conversation, extraction, validation, delegation, final review | Specialist travel research |
| V3 Execution | Specialist-agent coordination and research consolidation | User-facing request clarification |

## 4. Error Handling and Reliability

Implemented:
- Coordinator retry configuration: up to two attempts.
- Missing mandatory inputs are routed to an error-response path.
- Workflow delegation uses a defined sub-workflow connection.

Design considerations for future enhancement:
- Explicit fallback behavior for external search failures.
- Per-agent timeout and retry policies.
- Handling of partial specialist-agent results.
- Structured error propagation between workflows.
- Execution tracing and failure observability.

## 5. Orchestration Trade-offs

**Centralized coordination vs. independent agents**

A central orchestrator simplifies delegation and consolidation while retaining domain specialization.

**Reusable sub-workflow vs. single workflow**

Separating V3 from V4 improves modularity and allows the execution layer to evolve independently.

**LLM-based validation vs. deterministic validation**

The current final review is agent-driven. Critical constraints such as date ranges, hotel duration, and schedule conflicts could be strengthened with deterministic validation rules.

## 6. Current Execution Model

The workflow prompts instruct the Travel Orchestrator to invoke each specialist agent once. The workflow configuration establishes agent delegation, but does not by itself demonstrate concurrent execution.
