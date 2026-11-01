# Hotels Agent

## 1. Purpose

The Hotels Agent researches accommodation options aligned with the user's destination, travel dates, budget, and accommodation preferences.

## 2. Position in Architecture

- Parent: Travel Orchestrator (V3).
- Search integration: SerpApi – Google Hotels.
- LLM: OpenAI GPT-4o-mini.
- Execution platform: n8n.

## 3. Responsibilities

1. Identify accommodation options at the destination.
2. Consider travel dates, budget, and travel style.
3. Evaluate available hotel information.
4. Prioritize suitable options based on user preferences.
5. Return comparable accommodation alternatives.

## 4. Input Contract

- Destination.
- Departure and return dates.
- Number of travelers.
- Budget, when provided.
- Travel style: budget, mid-range, or luxury.
- Hotel preferences, when provided.

## 5. Expected Output

The agent is prompted to return approximately 5–7 hotel options.

| Attribute | Description |
|---|---|
| Hotel name | Accommodation name |
| Rating | Available customer rating |
| Area | Hotel location |
| Price per night | Estimated nightly price |
| Total stay cost | Estimated accommodation cost for the trip |

The agent is instructed to prefer 4-star or higher properties when the user's budget allows.

## 6. Tool Integration

The agent uses SerpApi's Google Hotels search integration.

## 7. Constraints

- Search results and prices depend on external data availability.
- Displayed prices may change.
- Hotel recommendations do not represent confirmed availability.
- Booking and payment are outside the current scope.

## 8. Evaluation Metrics

Proposed metrics:
- Accommodation relevance.
- Budget alignment.
- Preference alignment.
- Completeness of hotel information.
- Consistency between hotel dates and trip duration.
