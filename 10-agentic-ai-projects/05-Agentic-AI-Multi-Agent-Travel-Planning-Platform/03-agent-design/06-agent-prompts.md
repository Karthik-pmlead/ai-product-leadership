# Agent Prompts

## 1. Purpose

This document captures the prompt responsibilities and behavioral boundaries of the platform's agents.

The prompts guide agent behavior, tool usage, delegation, and output expectations.

## 2. Coordinator Agent

**Role:** Understand the user's travel request and prepare a validated trip specification.

**Prompt responsibilities:**
- Extract origin, destination, departure date, and return date.
- Capture traveler count, budget, travel style, and preferences.
- Default traveler count to one when unspecified.
- Identify missing mandatory information.
- Return a structured response using the Structured Output Parser.
- Ask for missing mandatory details rather than initiating incomplete execution.

## 3. Planner Agent

**Role:** Delegate the validated request to the execution workflow.

**Prompt responsibilities:**
- Invoke the Orchestrator and Executor workflow.
- Pass the trip request and session context.
- Do not independently create an itinerary.
- Do not summarize or modify specialist research.
- Return execution results for final review.

## 4. Travel Orchestrator

**Role:** Coordinate specialist travel research.

**Prompt responsibilities:**
- Invoke Flights Agent once.
- Invoke Hotels Agent once.
- Invoke Activities Agent once.
- Ensure all agents receive the relevant trip context.
- Consolidate their findings.
- Avoid independently generating domain-specific recommendations.
- Avoid repeated agent calls unless critical information is missing.

## 5. Flights Agent

**Role:** Research flight alternatives.

**Prompt responsibilities:**
- Find 4–6 viable round-trip options.
- Consider nonstop and one-stop alternatives where relevant.
- Include airline, departure and arrival times, duration, stops, and estimated total price.
- Use the Google Flights search tool.

## 6. Hotels Agent

**Role:** Research accommodation alternatives.

**Prompt responsibilities:**
- Find 5–7 accommodation options.
- Align results with destination, dates, budget, and travel style.
- Include rating, area, price per night, and estimated total stay cost.
- Prefer 4-star or higher properties when budget permits.
- Use the Google Hotels search tool.

## 7. Activities Agent

**Role:** Discover attractions and local experiences.

**Prompt responsibilities:**
- Use Google Local and Tavily Search.
- Use each research tool once.
- Generate 8–12 relevant activities.
- Include major attractions and local experiences.
- Consolidate findings and group recommendations loosely by day.

## 8. Validator and Summarizer

**Role:** Review and curate the final itinerary.

**Prompt responsibilities:**
- Check date consistency.
- Check hotel stay against trip duration.
- Review activity timing.
- Identify and correct obvious conflicts.
- Curate 2–3 flight options.
- Curate 2–3 hotel options.
- Curate 5–8 activities.
- Present a structured response with Trip Overview, Flights, Hotel, and Activities.

## 9. Prompt Design Principles

1. **Role clarity:** Each agent has a defined responsibility.
2. **Bounded autonomy:** Agents operate within their assigned research or coordination scope.
3. **Tool specificity:** Research agents use designated external search tools.
4. **Context consistency:** Specialist agents work from the same trip requirements.
5. **Separation of concerns:** Research, orchestration, validation, and presentation remain distinct.
6. **Controlled synthesis:** The final validator curates specialist findings rather than independently repeating the research.

## 10. Future Prompt Improvements

- Define versioned prompt templates.
- Introduce strict JSON output schemas.
- Add explicit missing-data and empty-result handling.
- Require source URLs and retrieval timestamps.
- Add instructions for uncertainty and conflicting search results.
- Evaluate prompt changes against a fixed set of representative travel requests.

**Implementation note:** This document summarizes the prompt behavior represented in the workflow configuration. It is not a verbatim export of every system and user prompt.
