# Shared State and Itinerary Schema

## 1. Overview

The platform passes a common trip request from the V4 Coordinator to the V3 execution workflow. Specialist agents use this request as the shared planning context.

The current implementation uses workflow inputs, chat session context, and agent prompts. It does not establish a centralized database or a formally enforced shared-state service.

## 2. Trip Request

The Coordinator extracts the following request attributes:

| Field | Required | Description |
|---|---|---|
| origin | Yes | Departure location |
| destination | Yes | Target destination |
| departure_date | Yes | Trip start date |
| return_date | Yes | Trip end date |
| number_of_travelers | No | Defaults to 1 |
| budget | No | User's stated budget |
| travel_style | No | Budget, mid-range, or luxury |
| preferences | No | General travel preferences |
| hotel_preferences | No | Accommodation preferences |
| flight_preferences | No | Flight preferences |

## 3. Workflow Context

The V4 workflow passes:
- `chatInput`: Validated trip request.
- `sessionId`: Conversation/session identifier.

The V3 workflow receives these values through its workflow trigger.

The session identifier supports continuity across the workflow boundary. It should not be interpreted as a persistent itinerary database.

## 4. Logical Itinerary Representation

The following is a recommended logical representation for documenting and evaluating itinerary results. It is not a claim that the current workflow enforces this exact JSON schema.

```json
{
  "trip": {
    "origin": "",
    "destination": "",
    "departure_date": "",
    "return_date": "",
    "number_of_travelers": 1,
    "budget": null,
    "travel_style": "",
    "preferences": []
  },
  "flights": [
    {
      "airline": "",
      "departure_time": "",
      "arrival_time": "",
      "duration": "",
      "stops": "",
      "estimated_price": ""
    }
  ],
  "hotels": [
    {
      "name": "",
      "location": "",
      "rating": "",
      "price_per_night": "",
      "estimated_total_cost": ""
    }
  ],
  "activities": [
    {
      "name": "",
      "location": "",
      "description": "",
      "suggested_day": ""
    }
  ],
  "validation": {
    "date_consistency": "",
    "hotel_duration": "",
    "activity_schedule": "",
    "conflicts": []
  }
}
```

## 5. Shared-State Design Considerations

Future enhancements:
- Adopt a versioned, machine-readable itinerary schema.
- Define required and optional fields for each agent.
- Normalize currency, dates, time zones, and location identifiers.
- Preserve source URLs and retrieval timestamps.
- Track validation status and unresolved conflicts.
- Maintain provenance for agent-generated recommendations.

## 6. Design Principle

A shared trip request provides a common context across agents. A standardized itinerary schema would make their outputs easier to validate, compare, and extend.
