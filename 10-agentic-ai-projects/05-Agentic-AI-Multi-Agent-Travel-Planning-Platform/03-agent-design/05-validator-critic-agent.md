# Validator and Critic Agent

## 1. Purpose

The Validator and Summarizer reviews the consolidated research produced by the V3 execution workflow and prepares a coherent final itinerary.

It acts as the final quality-review layer before results are presented to the user.

## 2. Position in Architecture

- Workflow: V4 Main Workflow.
- Upstream component: Planner Agent and V3 Execution Workflow.
- LLM: OpenAI GPT-4o-mini.
- Execution platform: n8n.

## 3. Responsibilities

1. Review consolidated flight, hotel, and activity recommendations.
2. Check consistency with the original trip requirements.
3. Identify obvious date and scheduling conflicts.
4. Review hotel stay duration against trip duration.
5. Correct or remove obvious inconsistencies.
6. Curate recommendations for the final response.
7. Present a structured itinerary.

## 4. Input Contract

- Original trip requirements.
- Consolidated flight research.
- Consolidated hotel research.
- Consolidated activity recommendations.

## 5. Validation Responsibilities

| Validation area | Expected review |
|---|---|
| Date consistency | Flight and activity dates align with the requested trip |
| Hotel duration | Accommodation period aligns with trip duration |
| Activity timing | Activities have plausible timing |
| Cross-agent consistency | Obvious conflicts across recommendations |
| Recommendation curation | Select relevant options for final presentation |

## 6. Output Structure

The agent is instructed to produce:

### Trip Overview
- Origin and destination.
- Travel dates.
- Traveler details.

### Flights
- 2–3 curated flight options.

### Hotel
- 2–3 curated accommodation options.

### Activities
- 5–8 selected activities.

### Final Itinerary
- Consolidated recommendations organized for user consumption.

## 7. Current Validation Approach

Validation is LLM-driven and prompt-based.

The workflow instructs the agent to identify and correct obvious conflicts. It does not establish a deterministic scheduling engine or guarantee that every constraint is satisfied.

## 8. Current Limitations

- No deterministic itinerary constraint solver.
- No guaranteed flight or hotel availability verification.
- No automated booking confirmation.
- No formal validation confidence score.
- No guaranteed travel-time optimization.
- No machine-enforced cross-agent schema validation.

## 9. Future Enhancements

- Introduce deterministic date and duration validation.
- Add structured output validation.
- Implement budget aggregation across recommendations.
- Validate activity feasibility using travel-time estimates.
- Preserve source URLs and retrieval timestamps.
- Add explicit validation status and unresolved-conflict reporting.

## 10. Evaluation Metrics

Proposed metrics:
- Cross-agent conflict detection rate.
- Date-consistency pass rate.
- Hotel-duration validation rate.
- Activity-schedule consistency.
- Final itinerary acceptance rate.

These are proposed evaluation metrics, not measured production results.
