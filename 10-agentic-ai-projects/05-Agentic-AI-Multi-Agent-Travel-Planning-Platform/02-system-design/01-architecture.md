# System Architecture

## 1. Overview

The platform uses a hierarchical multi-agent architecture implemented in n8n. A user-facing workflow coordinates request intake, input validation, execution, and final response generation. A separate execution workflow delegates travel research to specialized agents.

The architecture separates **request coordination, domain-specific research, and final itinerary validation**.

## 2. High-Level Architecture

```text
USER
  |
  v
V4: MAIN WORKFLOW
  |
Chat Trigger
  |
Coordinator Agent
  |-- Extract trip requirements
  |-- Maintain conversational context
  |-- Validate mandatory fields
  |
  v
Required-Field Check
  |-- Missing information -> Error Response
  |
  v
Planner Agent
  |
  v
V3: EXECUTION SUB-WORKFLOW
  |
Travel Orchestrator
  |-- Flights Agent -> Google Flights (SerpApi)
  |-- Hotels Agent  -> Google Hotels (SerpApi)
  |-- Activities Agent -> Google Local (SerpApi)
  |                    -> Tavily Search
  |
  v
Consolidated Research Results
  |
  v
V4: VALIDATOR & SUMMARIZER
  |
  |-- Date consistency
  |-- Hotel-stay alignment
  |-- Activity scheduling
  |-- Conflict correction
  |
  v
Final Itinerary
  |
Chat Response
```

## 3. Architectural Components

| Component | Responsibility |
|---|---|
| Chat interface | Accept user trip requests |
| Coordinator | Extract requirements and validate mandatory inputs |
| Planner | Delegate execution to the travel research workflow |
| Travel orchestrator | Coordinate specialist travel agents |
| Flights agent | Research flight options |
| Hotels agent | Research accommodation options |
| Activities agent | Discover attractions and experiences |
| Validator and summarizer | Review, curate, and present consolidated results |

## 4. Technology Stack

- **Workflow orchestration:** n8n
- **LLM:** OpenAI GPT-4o-mini
- **Flight and hotel research:** SerpApi
- **Local discovery:** SerpApi Google Local
- **Web research:** Tavily
- **Conversational memory:** Simple Memory Buffer Window
- **Structured extraction:** Coordinator Agent with Structured Output Parser

## 5. Architectural Principles

1. Separation of coordination and domain execution.
2. Specialized agents with bounded responsibilities.
3. Reuse of the execution workflow through a sub-workflow interface.
4. Validation before presenting the final itinerary.
5. Extensibility through independently replaceable research agents.

## 6. Current Scope

The system researches and recommends travel options and produces a consolidated itinerary. Automated booking, payment, reservation confirmation, and end-to-end travel execution are outside the implemented scope.
