# Orchestrator Agent

## 1. Purpose

The Travel Orchestrator coordinates specialized travel research agents and consolidates their outputs into a unified set of trip recommendations.

It acts as the execution layer between the validated trip request and the final itinerary review.

**Design principle:** Delegate domain-specific research to specialized agents rather than duplicating their responsibilities within the orchestrator.

## 2. Position in the Architecture

```text
V4 Planner Agent
       |
       v
V3 Execution Workflow
       |
       v
Travel Orchestrator
       |
       |-- Flights Agent
       |      └── SerpApi: Google Flights
       |
       |-- Hotels Agent
       |      └── SerpApi: Google Hotels
       |
       |-- Activities Agent
       |      ├── SerpApi: Google Local
       |      └── Tavily Search
       |
       v
Consolidated Research Results
       |
       v
V4 Validator & Summarizer
```

## 3. Responsibilities

1. Receive the validated trip request from the V4 workflow.
2. Invoke the Flights Agent, Hotels Agent, and Activities Agent.
3. Provide a common trip context to each specialist.
4. Consolidate the research returned by the specialist agents.
5. Return the combined results to the V4 workflow for final validation and presentation.

## 4. Agent Delegation

| Specialist | Delegated responsibility | Expected output |
|---|---|---|
| Flights Agent | Research round-trip flight options | 4–6 flight alternatives |
| Hotels Agent | Find accommodation matching trip requirements | 5–7 hotel alternatives |
| Activities Agent | Discover attractions and local experiences | 8–12 activities |

The orchestrator is instructed to invoke each specialist once, avoid independently generating domain recommendations, and avoid repeated calls unless critical information is missing.

## 5. Input Contract

The orchestrator receives the validated trip request, including:

- Origin and destination.
- Departure and return dates.
- Number of travelers.
- Budget and travel style, when provided.
- General, hotel, and flight preferences, when provided.

## 6. Output Contract

The orchestrator returns consolidated research containing:

- Flight alternatives and their key travel details.
- Hotel alternatives and estimated accommodation costs.
- Activities and local experiences, with suggested day groupings.

The V4 Validator and Summarizer subsequently curates the results into the final itinerary.

## 7. Orchestration Design Decisions

**Specialization over monolithic execution**

Separate agents focus on flights, accommodation, and activities, keeping research responsibilities distinct.

**Centralized coordination**

The Travel Orchestrator provides a single coordination point for specialist execution and consolidation.

**Separation of execution and presentation**

The orchestrator focuses on research coordination. Final consistency review, recommendation curation, and user-facing presentation remain in the V4 workflow.

## 8. Current Limitations

- Agent outputs are primarily prompt-defined rather than governed by strict machine-enforced schemas.
- The workflow configuration does not establish guaranteed parallel execution.
- Explicit cross-agent budget optimization is not implemented.
- Deterministic schedule and travel-time validation is not implemented at the orchestrator level.
- External search results may vary in freshness and availability.

## 9. Future Enhancements

- Introduce standardized JSON contracts for specialist agents.
- Add deterministic validation before consolidation.
- Implement partial-result handling and agent-level retry policies.
- Add source attribution and retrieval timestamps.
- Introduce budget-aware optimization across flight, hotel, and activity choices.
- Evaluate parallel execution where supported by the workflow platform.

## 10. Success Criteria

The orchestrator should be evaluated on:

- Specialist-agent execution completion rate.
- Completeness of consolidated research.
- Cross-agent consistency.
- Relevance to the original trip requirements.
- Reduction in missing, duplicated, or conflicting recommendations.

These are proposed evaluation metrics; production performance has not yet been established.
