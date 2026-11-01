# Assumptions and Constraints

## Assumptions

1. Users can provide origin, destination, departure date, and return date.
2. Traveler count defaults to one when not specified.
3. Budget, travel style, and preferences are optional inputs.
4. External search providers return sufficiently relevant travel information.
5. Search results are recommendations and may change before booking.
6. The generated itinerary is intended as a planning aid, not a booking confirmation.

## Technical Constraints

| Area | Constraint |
|---|---|
| Orchestration | Workflows are implemented using n8n |
| Language model | Agent execution uses OpenAI GPT-4o-mini |
| Flight discovery | Depends on SerpApi Google Flights |
| Hotel discovery | Depends on SerpApi Google Hotels |
| Activity discovery | Depends on SerpApi Google Local and Tavily |
| External dependencies | Search availability, API limits, and response quality affect execution |
| Output quality | Agent-generated recommendations require validation |

## Product Constraints

- The current implementation researches and recommends options; it does not complete bookings.
- Prices and availability are subject to change.
- Search results may vary by destination and travel dates.
- The system depends on users supplying accurate mandatory travel details.
- The current specialist architecture covers flights, hotels, and activities.

## Design Decisions

- Separate the user-facing workflow from the execution sub-workflow.
- Use specialized agents rather than one general-purpose travel research agent.
- Enforce structured request extraction before execution.
- Keep domain research separate from itinerary validation and presentation.
- Use external search integrations for destination-specific information.

## Future Considerations

- Transportation and travel-time optimization.
- Weather-aware itinerary planning.
- Budget allocation across travel components.
- Structured agent output contracts.
- Explicit API fallback and retry strategies.
- Concurrent agent execution where supported.
- Source freshness and recommendation traceability.
