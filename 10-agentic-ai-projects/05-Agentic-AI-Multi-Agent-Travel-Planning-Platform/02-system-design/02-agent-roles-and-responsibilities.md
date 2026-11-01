# Agent Roles and Responsibilities

## 1. Design Principle

Each agent owns a distinct part of the travel-planning problem. The orchestrator coordinates specialist execution, while the final validator reviews the consolidated itinerary.

## 2. Agent Responsibilities

| Agent | Primary responsibility | Expected contribution |
|---|---|---|
| Coordinator | Understand user intent and extract trip requirements | Validated trip request |
| Planner | Invoke the execution workflow | Delegated execution |
| Travel Orchestrator | Coordinate specialist agents and consolidate their findings | Combined travel research |
| Flights Agent | Research round-trip flight options | Flight alternatives |
| Hotels Agent | Identify accommodation matching budget and preferences | Hotel alternatives |
| Activities Agent | Discover attractions and local experiences | Activity recommendations |
| Validator and Summarizer | Review consistency, curate options, and format results | Final itinerary |

## 3. Agent-Level Responsibilities

### Coordinator Agent
- Extract origin, destination, departure date, and return date.
- Capture optional preferences, budget, travel style, and traveler count.
- Default traveler count to one when unspecified.
- Identify missing mandatory information.
- Return a structured request or clarification response.

### Planner Agent
- Pass the validated request to the execution sub-workflow.
- Avoid independently generating or modifying itinerary recommendations.
- Return execution results for final validation.

### Travel Orchestrator
- Invoke the Flights, Hotels, and Activities agents.
- Coordinate their research using the same trip request.
- Consolidate specialist outputs.
- Avoid duplicating domain-specific research.

### Specialist Agents

**Flights Agent**
- Research viable round-trip flight options.
- Include airline, departure and arrival times, duration, stops, and estimated price.
- Target 4–6 alternatives.

**Hotels Agent**
- Research accommodation options aligned with budget and travel style.
- Include rating, location, nightly price, and estimated stay cost.
- Target 5–7 alternatives.

**Activities Agent**
- Discover attractions and local experiences.
- Use local search and web research.
- Consolidate results and group activities loosely by day.
- Target 8–12 recommendations.

### Validator and Summarizer
- Check date consistency.
- Check hotel duration against trip duration.
- Review activity timing and obvious conflicts.
- Curate flight, hotel, and activity options.
- Present the final itinerary in a consistent format.

## 4. Responsibility Boundaries

- The Coordinator owns request understanding, not travel research.
- The Orchestrator owns delegation and consolidation, not specialist-level optimization.
- Specialist agents own their respective research domains.
- The Validator owns final review and presentation, not booking execution.

## 5. Implementation Note

These responsibilities are defined through agent prompts and workflow connections. They are not all enforced through independent services or strict machine-level interfaces.
