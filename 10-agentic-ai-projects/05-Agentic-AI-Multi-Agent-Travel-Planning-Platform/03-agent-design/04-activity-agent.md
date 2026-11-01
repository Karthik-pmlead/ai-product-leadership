# Activities Agent

## 1. Purpose

The Activities Agent discovers attractions, experiences, and local activities relevant to the user's destination and travel preferences.

It combines local search and web research to produce a curated set of activity recommendations.

## 2. Position in Architecture

- Parent: Travel Orchestrator (V3).
- LLM: OpenAI GPT-4o-mini.
- Execution platform: n8n.

## 3. Responsibilities

1. Discover popular attractions and local experiences.
2. Identify activities relevant to user preferences.
3. Combine local discovery and web research.
4. Consolidate overlapping findings.
5. Organize recommendations loosely by day.

## 4. Input Contract

- Destination.
- Departure and return dates.
- Travel preferences.
- Travel style.
- Other relevant trip context.

## 5. Expected Output

The agent is prompted to produce approximately 8–12 activities.

Expected information includes:

| Attribute | Description |
|---|---|
| Activity | Attraction or experience |
| Location | Relevant area or address |
| Description | Brief explanation |
| Suggested day | Approximate day grouping |

Recommendations should include a mix of major attractions and local experiences.

## 6. Tool Integration

The agent uses two research tools:

**SerpApi – Google Local**
- Discovers local attractions and places.
- Provides location-oriented search results.

**Tavily Search**
- Retrieves relevant web information.
- Supplements local discovery with broader research.

The agent is instructed to use each research tool once and consolidate the findings.

## 7. Constraints

- Activity recommendations are not confirmed bookings.
- Opening hours and availability may change.
- Day groupings are suggestions, not optimized travel routes.
- Detailed travel-time and route optimization are outside the current implementation.

## 8. Evaluation Metrics

Proposed metrics:
- Activity relevance.
- Diversity of recommendations.
- Preference alignment.
- Location-information completeness.
- Duplicate recommendation rate.
- Practicality of suggested day groupings.
