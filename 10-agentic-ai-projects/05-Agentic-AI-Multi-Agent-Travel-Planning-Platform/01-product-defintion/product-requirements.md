# Product Requirements

## Product Objective

Enable users to generate a personalized travel itinerary through coordinated AI agents specializing in flights, hotels, and activities.

## Functional Requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-01 | Accept natural-language travel requests through chat | P0 |
| FR-02 | Extract origin, destination, departure date, and return date | P0 |
| FR-03 | Capture traveler count, budget, travel style, and preferences | P0 |
| FR-04 | Identify missing mandatory information before execution | P0 |
| FR-05 | Delegate flight research to a specialized agent | P0 |
| FR-06 | Delegate hotel discovery to a specialized agent | P0 |
| FR-07 | Delegate activity discovery to a specialized agent | P0 |
| FR-08 | Consolidate specialist outputs into a trip itinerary | P0 |
| FR-09 | Validate travel dates, hotel duration, and activity scheduling | P0 |
| FR-10 | Curate and present relevant options in a structured response | P0 |

## Non-Functional Requirements

- **Modularity:** Separate domain responsibilities across specialized agents.
- **Reliability:** Validate mandatory inputs before downstream execution.
- **Consistency:** Maintain alignment across travel dates and itinerary components.
- **Extensibility:** Support additional travel domains without redesigning the entire workflow.
- **Usability:** Present consolidated recommendations through a conversational interface.

## Agent Responsibilities

| Agent | Responsibility |
|---|---|
| Coordinator | Request extraction and input validation |
| Travel Orchestrator | Delegate tasks and consolidate agent outputs |
| Flights Agent | Research round-trip flight options |
| Hotels Agent | Discover accommodation options |
| Activities Agent | Research attractions and local experiences |
| Validator | Check itinerary consistency and curate recommendations |

## Out of Scope

- Automated flight or hotel booking.
- Payment processing.
- Booking confirmations.
- Real-time reservation management.

## Implementation

- n8n: Workflow orchestration.
- OpenAI GPT-4o-mini: Agent reasoning.
- SerpApi: Flight, hotel, and local search.
- Tavily: Web research.

**Workflow architecture:** V4 Main Workflow + V3 Execution Sub-workflow.
