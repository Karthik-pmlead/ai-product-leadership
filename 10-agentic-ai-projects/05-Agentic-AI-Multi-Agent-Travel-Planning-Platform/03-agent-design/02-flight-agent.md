# Flights Agent

## 1. Purpose

The Flights Agent researches round-trip flight options based on the user's trip requirements and returns alternatives for the Travel Orchestrator to consolidate.

## 2. Position in Architecture

- Parent: Travel Orchestrator (V3).
- Search integration: SerpApi – Google Flights.
- LLM: OpenAI GPT-4o-mini.
- Execution platform: n8n.

## 3. Responsibilities

1. Research round-trip flights between the requested origin and destination.
2. Consider departure and return dates.
3. Identify viable flight alternatives.
4. Include a mix of nonstop and one-stop options where relevant.
5. Present comparable flight information for evaluation.

## 4. Input Contract

- Origin.
- Destination.
- Departure date.
- Return date.
- Number of travelers.
- Flight preferences, when provided.

## 5. Expected Output

The agent is prompted to return approximately 4–6 viable flight options.

| Attribute | Description |
|---|---|
| Airline | Operating airline |
| Departure | Departure time |
| Arrival | Arrival time |
| Duration | Total journey duration |
| Stops | Number of stops |
| Estimated price | Indicative total price |

## 6. Tool Integration

The agent uses SerpApi's Google Flights search integration to retrieve flight information.

## 7. Constraints

- Results depend on external search availability and freshness.
- Prices are estimates and may change.
- Search results do not constitute confirmed reservations.
- Automated booking and payment are outside the current scope.

## 8. Evaluation Metrics

Proposed metrics:
- Flight-result relevance.
- Search-result completeness.
- Preference alignment.
- Date consistency.
- Accuracy of displayed flight details.
