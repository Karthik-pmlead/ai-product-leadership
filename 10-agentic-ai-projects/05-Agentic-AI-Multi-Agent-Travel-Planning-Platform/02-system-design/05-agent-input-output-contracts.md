# Agent Input/Output Contracts

## 1. Purpose

Define the expected information exchanged between the coordinator, orchestrator, specialist agents, and final validator.

The current implementation primarily defines these expectations through prompts and workflow connections. The contracts below document the logical interfaces; they are not all enforced as strict JSON schemas.

## 2. Coordinator Agent

**Input**
- User's natural-language travel request.
- Conversational context.

**Output**
- Origin.
- Destination.
- Departure and return dates.
- Optional traveler count, budget, travel style, and preferences.
- Missing-field indicator and clarification message when required information is unavailable.

**Contract rule:** Do not delegate until mandatory trip details are available.

## 3. Planner Agent

**Input**
- Validated trip request.
- Chat session identifier.

**Output**
- Result returned by the V3 execution workflow.

**Contract rule:** Delegate execution rather than independently generating travel recommendations.

## 4. Travel Orchestrator

**Input**
- Validated trip request.

**Expected specialist outputs**

| Specialist | Expected output |
|---|---|
| Flights Agent | 4–6 flight alternatives with airline, timings, duration, stops, and estimated price |
| Hotels Agent | 5–7 accommodation alternatives with rating, location, nightly price, and estimated stay cost |
| Activities Agent | 8–12 activities with descriptions and loose day grouping |

**Output**
- Consolidated flight, hotel, and activity research.

**Contract rule:** Invoke each specialist once as instructed and consolidate its findings without duplicating specialist research.

## 5. Specialist Agent Contracts

### Flights Agent
Input: Origin, destination, departure date, return date, traveler count, and flight preferences.

Output: Round-trip flight alternatives with relevant itinerary details and estimated prices.

### Hotels Agent
Input: Destination, travel dates, traveler count, budget, travel style, and hotel preferences.

Output: Accommodation alternatives with location, rating, nightly price, and estimated total stay cost.

### Activities Agent
Input: Destination, trip dates, preferences, and travel style.

Output: Attractions and local experiences, including descriptions and suggested day grouping.

## 6. Validator and Summarizer

**Input**
- Consolidated research results.
- Original trip request.

**Output**
- Curated flight options.
- Curated hotel options.
- Curated activities.
- Final itinerary overview.
- Corrected or removed obvious inconsistencies.

**Contract rule:** Preserve the user's trip requirements while improving coherence and readability.

## 7. Contract Gaps and Future Improvements

The current workflow does not establish strict machine-enforced contracts for every specialist agent.

Recommended enhancements:
- Define JSON schemas for each agent's output.
- Validate required fields before consolidation.
- Standardize dates, currencies, and time zones.
- Include source URL and retrieval timestamp.
- Define explicit empty-result and error responses.
- Reject malformed or incomplete agent outputs before final synthesis.
