# Cross-Agent Validation

## 1. Purpose

Specialist agents research different parts of a trip. Their recommendations must be reviewed together to reduce inconsistencies before presenting a consolidated itinerary.

The V4 Validator and Summarizer performs an LLM-based review of the consolidated research results.

## 2. Validation Responsibilities

| Validation area | What is checked |
|---|---|
| Trip dates | Recommendations align with departure and return dates |
| Hotel duration | Accommodation stay aligns with trip duration |
| Activity timing | Suggested activities fit the travel schedule |
| Cross-agent consistency | Obvious conflicts across flight, hotel, and activity recommendations |
| Recommendation quality | Final options are curated and relevant |
| Presentation | Results are organized into a coherent itinerary |

## 3. Current Validation Flow

```text
Flights + Hotels + Activities
             |
             v
    Travel Orchestrator
             |
             v
    Consolidated Results
             |
             v
   V4 Validator & Summarizer
             |
       Review consistency
             |
     Correct obvious conflicts
             |
      Curate recommendations
             |
             v
       Final Itinerary
```

## 4. Validation Rules

### Date Consistency
Check that flight and activity recommendations correspond to the requested trip dates.

### Hotel Duration
Check that the accommodation period covers the intended stay.

### Activity Scheduling
Review activity timing and identify obvious scheduling conflicts.

### Cross-Agent Coherence
Review whether the consolidated flight, hotel, and activity recommendations form a plausible trip.

### Final Curation
Present a manageable selection of:
- 2–3 flight options.
- 2–3 hotel options.
- 5–8 activities.

## 5. Current Limitations

The current validator is prompt-driven. The workflow configuration does not demonstrate:
- A deterministic constraint solver.
- Machine-enforced validation of every recommendation.
- Guaranteed real-time availability.
- Verified booking or reservation status.
- A formal confidence score for validation outcomes.

## 6. Recommended Validation Enhancements

| Enhancement | Expected benefit |
|---|---|
| Deterministic date validation | Reduce date and duration errors |
| Structured output validation | Detect missing or malformed fields |
| Time-zone normalization | Improve schedule consistency |
| Travel-time estimation | Identify impractical activity sequences |
| Budget aggregation | Check estimated trip cost against user budget |
| Source freshness checks | Identify stale search results |
| Conflict severity classification | Prioritize material itinerary issues |
| Validation audit trail | Explain corrections and unresolved conflicts |

## 7. Product Principle

**An itinerary should be evaluated as one connected travel experience, not as three independent lists of recommendations.**
