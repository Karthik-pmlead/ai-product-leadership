# Agentic AI Multi-Agent Travel Planning Platform

## 1. Overview

The Agentic AI Multi-Agent Travel Planning Platform is a low-code, multi-agent system built using **n8n, LangChain, OpenAI, SerpApi, and Tavily**.

It simplifies travel planning by coordinating specialized AI agents responsible for flight research, hotel discovery, and activity recommendations.

Instead of relying on a single AI agent to handle every aspect of trip planning, the platform uses a hierarchical orchestration architecture:

- A **Coordinator Agent** captures and structures the user's travel requirements.
- A **Planner Agent** invokes the multi-agent execution workflow.
- A **Travel Orchestrator** coordinates specialized domain agents.
- **Flights, Hotels, and Activities Agents** independently handle their respective research tasks.
- A **Validator and Summarizer** reviews and curates the combined itinerary before presenting it to the user.

The platform demonstrates how specialized agents, external search tools, structured inputs, and orchestration can work together to produce a personalized travel plan.

## 2. Problem Statement

Planning a trip involves coordinating several interconnected decisions:

- Finding suitable flights based on travel dates and preferences.
- Identifying hotels aligned with budget, location, and travel style.
- Discovering relevant attractions and local experiences.
- Organizing activities around the travel schedule.
- Maintaining consistency across flight dates, hotel stays, and activities.

Traditional travel planning often requires users to navigate multiple platforms and manually reconcile information.

This creates a fragmented experience, increases planning effort, and makes personalization more difficult.

### Product Opportunity

Build an agentic travel planning experience that accepts high-level travel requirements and coordinates specialized AI agents to research, consolidate, and validate relevant travel options.

## 3. Product Objectives

The platform is designed to:

1. Accept natural-language travel requests.
2. Extract structured travel requirements.
3. Identify missing mandatory information before execution.
4. Delegate research to specialized domain agents.
5. Retrieve travel options using external search integrations.
6. Consolidate results into a coherent itinerary.
7. Validate important scheduling constraints.
8. Present a readable, personalized travel plan.

## 4. System Architecture

The implementation consists of two n8n workflows.

| Workflow | Responsibility |
|---|---|
| Multi-Agent V4 — Main | User interaction, request coordination, validation, and response presentation |
| Multi-Agent V3 — Sub-workflow | Domain-specific agent execution and itinerary assembly |

### Architecture Flow

```text
                   USER
                     |
                     v
             n8n Chat Trigger
                     |
                     v
             COORDINATOR AGENT
          Structured Request Extraction
                     |
                     v
            STRUCTURED OUTPUT
                     |
                     v
             MISSING FIELD CHECK
                 /       \
              Error      Valid
                |          |
                v          v
          Error Reply   PLANNER AGENT
                           |
                           v
                 ORCHESTRATOR TOOL
                           |
                           v
                 MULTI-AGENT V3
                           |
                           v
                TRAVEL ORCHESTRATOR
                    /    |    \
                   /     |     \
                  v      v      v
              FLIGHTS  HOTELS ACTIVITIES
               AGENT   AGENT    AGENT
                  |      |       |
                  v      v       v
              GOOGLE  GOOGLE  GOOGLE LOCAL
              FLIGHTS HOTELS  + TAVILY
                   \     |     /
                    \    |    /
                     v   v   v
                 CONSOLIDATED
                   ITINERARY
                       |
                       v
              VALIDATOR AND
                 SUMMARIZER
                       |
                       v
                 CHAT RESPONSE
```

## 5. Agent Responsibilities

### 5.1 Coordinator Agent — V4

**Purpose:** Convert the user's natural-language request into structured travel requirements.

Responsibilities:

- Extract origin and destination.
- Identify departure and return dates.
- Capture the number of travelers.
- Extract budget and travel style.
- Identify user interests and preferences.
- Capture optional flight and hotel preferences.
- Identify missing mandatory fields.

A structured output parser enforces the request format.

**Mandatory fields:**
- Origin
- Destination
- Departure date
- Return date

If any mandatory field is missing, the workflow routes the request to an error response rather than proceeding with incomplete travel information.

The coordinator also uses n8n Simple Memory Buffer Window.

### 5.2 Planner Agent — V4

**Purpose:** Delegate execution to the V3 sub-workflow.

The Planner Agent passes the validated request to the `Orchestrator and Executor` workflow tool.

Its instructions explicitly prevent it from independently generating or modifying the itinerary.

This establishes separation between request handling and domain execution.

### 5.3 Travel Orchestrator — V3

**Purpose:** Coordinate the specialist travel agents.

The orchestrator receives the structured trip request and is instructed to:

- Invoke the Flights Agent.
- Invoke the Hotels Agent.
- Invoke the Activities Agent.
- Ensure the results align with the travel dates.
- Combine agent outputs into a structured itinerary.

Each specialist is instructed to be called once, avoiding unnecessary repeated research unless critical information is missing.

The orchestrator is responsible for coordination and consolidation rather than independently generating domain-specific options.

### 5.4 Flights Agent

**Purpose:** Research round-trip flight options.

**Integration:** SerpApi — Google Flights.

The agent receives:
- Origin and destination.
- Departure and return dates.
- Number of travelers.
- Flight preferences.

Its configured responsibilities include generating 4–6 viable round-trip options with:

- Airline.
- Departure and arrival times.
- Journey duration.
- Number of stops.
- Estimated total price.

The agent is instructed to include a mix of nonstop and one-stop options where relevant.

### 5.5 Hotels Agent

**Purpose:** Identify accommodation options aligned with trip requirements.

**Integration:** SerpApi — Google Hotels.

The agent receives:
- Destination.
- Check-in and check-out dates.
- Number of travelers.
- Hotel preferences.
- Budget and travel style.

Its configured responsibilities include generating 5–7 hotel options with:

- Hotel rating.
- Location or area.
- Price per night.
- Estimated total stay cost.

The agent is instructed to prioritize four-star or higher properties when the budget allows.

### 5.6 Activities Agent

**Purpose:** Discover attractions and experiences relevant to the destination.

**Integrations:**
- SerpApi — Google Local.
- Tavily Search API.

The agent uses both local search and web search to identify relevant activities.

Its configured responsibilities include:

- Generating 8–12 activity options.
- Including popular attractions and unique local experiences.
- Incorporating user interests.
- Grouping activities loosely by day.

The agent consolidates the results from its two search tools.

## 6. Validation and Itinerary Curation

The Validator and Summarizer Agent operates in the V4 main workflow after the Planner returns the sub-workflow output.

Its responsibilities include three areas.

### 6.1 Schedule Validation

The agent is instructed to check:

- Travel date consistency.
- Hotel stay against trip duration.
- Activity timing against the daily schedule.
- Obvious scheduling conflicts.
- Unrealistic activity scheduling.

Small issues are intended to be corrected during this stage.

### 6.2 Option Curation

The configured selection guidelines are:

| Category | Curation guidelines |
|---|---|
| Flights | Select 2–3 options; balance price and duration; prefer nonstop or minimal layovers |
| Hotels | Select 2–3 options; prioritize central location and value; prefer four-star or higher when available |
| Activities | Select 5–8 experiences; distribute across days; balance iconic and local experiences |

### 6.3 Final Presentation

The final response is organized into:

1. Trip Overview
2. Flights
3. Hotel
4. Activities

The objective is to provide a clear, consolidated travel plan rather than exposing internal workflow details.

## 7. Technology Stack

| Layer | Technology |
|---|---|
| Workflow orchestration | n8n |
| Agent framework | LangChain n8n nodes |
| Language model | OpenAI GPT-4o-mini |
| Structured output | LangChain Structured Output Parser |
| Conversational interface | n8n Chat Trigger and Chat Response |
| Flight search | SerpApi Google Flights |
| Hotel search | SerpApi Google Hotels |
| Local activity discovery | SerpApi Google Local |
| Web research | Tavily Search API |
| Conversational memory | n8n Simple Memory Buffer Window |

## 8. Workflow Design

### V4 — Main Workflow

The main workflow manages the complete user interaction lifecycle.

Key components:

- Chat Trigger
- Coordinator Agent
- Structured Output Parser
- Missing-field validation using an IF node
- Planner Agent
- Orchestrator and Executor workflow tool
- Validator and Summarizer Agent
- Chat Response and Error Response

### V3 — Execution Sub-workflow

The sub-workflow is independently triggered by the main workflow.

Its input contract contains:

| Input | Description |
|---|---|
| `chatInput` | Structured travel request passed by the main workflow |
| `sessionId` | Chat session identifier |

The sub-workflow contains:

- Travel Agent (Orchestrator)
- Flights Agent
- Hotels Agent
- Activities Agent
- External search integrations
- Dedicated language model connections for the agents

This modular separation allows the execution workflow to be maintained independently of the user-facing request workflow.

## 9. Reliability and Error Handling

The implemented workflow includes:

- Mandatory-field validation before execution.
- A dedicated error response for incomplete travel requests.
- Retry configuration on the Coordinator Agent.
- Separation of request processing and itinerary execution.
- Explicit instructions for agents to avoid generating unsupported domain options.
- A final validation and summarization stage.

The Coordinator Agent is configured with retry enabled, a maximum of two attempts, and a short wait between attempts.

**Potential future reliability enhancements:**
- Structured validation of every specialist agent's output.
- Explicit retry and fallback policies for external API failures.
- Timeouts and rate-limit handling.
- Execution-level monitoring and tracing.
- More rigorous validation of prices, availability, and source freshness.

## 10. Product Evaluation Metrics

The following metrics are proposed for evaluating the platform. They should not be interpreted as measured outcomes unless supported by execution data.

| Dimension | Suggested metric |
|---|---|
| User experience | Itinerary acceptance rate |
| Personalization | Preference alignment score |
| Planning quality | Cross-domain scheduling consistency |
| Performance | End-to-end itinerary generation time |
| Reliability | Successful workflow completion rate |
| Operational efficiency | Manual intervention rate |
| Research quality | Relevant and usable options per domain |

### Suggested Evaluation Scenarios

1. Complete trip request with all mandatory fields.
2. Request missing the origin.
3. Request missing departure or return dates.
4. Budget-oriented trip.
5. Luxury travel request.
6. Request with specific hotel preferences.
7. Request with activity preferences such as food, museums, or hiking.
8. Multi-day itinerary requiring hotel and activity scheduling consistency.

## 11. Current Scope and Future Enhancements

### Implemented Capabilities

- Natural-language trip request handling.
- Structured travel request extraction.
- Mandatory-field validation.
- Hierarchical multi-agent orchestration.
- Dedicated flight, hotel, and activity agents.
- External search integrations.
- Consolidation of domain-specific results.
- Final itinerary validation and curation.
- Chat-based response delivery.

### Future Enhancements

**Orchestration**
- Evaluate concurrent execution of independent specialist agents.
- Add explicit agent execution dependencies.
- Introduce structured agent-to-agent contracts.

**Travel optimization**
- Introduce budget allocation across flights, hotels, and activities.
- Optimize activities using geographical proximity.
- Incorporate transportation and travel time between activities.
- Improve cross-domain constraint reconciliation.

**Additional agents**
- Transportation Agent.
- Weather Agent.
- Restaurant Recommendation Agent.
- Travel Documentation Agent.

**Reliability**
- Add structured response schemas for each specialist.
- Introduce API failure recovery and fallback providers.
- Add execution tracing and agent-level performance monitoring.
- Track search freshness and source attribution.

**User experience**
- Support itinerary revisions through conversational interaction.
- Enable preference updates.
- Provide alternative itinerary scenarios.
- Add itinerary export and sharing.

## 12. Key Product and Engineering Learnings

### 1. Specialization improves separation of responsibilities

A single agent handling every travel domain would need to manage multiple research tasks and output expectations.

Specialized agents provide clearer responsibilities, prompts, and tool boundaries.

### 2. Orchestration is more than invoking agents

The orchestrator must coordinate domain outputs into a coherent result.

The quality of the final itinerary depends not only on individual agent outputs but also on how those outputs are combined and validated.

### 3. Structured inputs improve workflow reliability

Converting natural-language requests into structured JSON creates a consistent input contract and enables mandatory-field validation before downstream execution.

### 4. Validation is a distinct product capability

Researching flights, hotels, and activities is not sufficient.

The final itinerary must also make sense across dates, hotel duration, and daily activity schedules.

### 5. Modular workflows improve extensibility

Separating the main workflow from the execution sub-workflow creates a foundation for adding new travel domains without redesigning the complete user interaction lifecycle.

## 13. Project Positioning

This project demonstrates practical experience in:

- Agentic AI product design.
- Multi-agent architecture.
- Hierarchical orchestration.
- Low-code AI workflow development.
- Prompt and agent responsibility design.
- Structured data extraction.
- External API and search integration.
- Cross-domain validation.
- Product reliability and extensibility.

**Core takeaway:** The project explores how a coordinated system of specialized AI agents can transform fragmented travel research into a consolidated, personalized trip-planning experience.

---

**Implementation:** n8n workflows — Multi-Agent V4 (Main) and Multi-Agent V3 (Execution Sub-workflow).

**Status:** Working and tested, as confirmed by the project owner.

**Note:** This platform researches and recommends travel options. Automated reservations, payments, and booking confirmation are outside the current implemented scope.
