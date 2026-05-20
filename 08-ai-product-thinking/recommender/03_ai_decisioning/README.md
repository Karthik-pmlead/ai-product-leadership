# AI Decision Matrix

## Decision question
Should recommendations be powered by AI, and if so, what approach should be used?

## Recommended approach
Use a hybrid recommender:
- rules for business constraints.
- retrieval or candidate generation.
- ranking model.
- re-ranking logic.
- human/business overrides where needed.

---
# FOBW Framework

## Fit
Recommendations fit well when the business has many items and users need help choosing.

## Outcome
Improve engagement, conversion, or discovery.

## Business value
High if better recommendations directly improve a business metric.

## Way to solve
Use the simplest recommendation system that can produce measurable lift.

---
# Build vs Buy

## Buy
Useful when speed matters and the use case is standard.

## Build
Useful when business rules, ranking logic, and item strategy are custom.

## Recommendation
Build if personalization and business control matter.


---
# Fine-tune vs RAG vs Prompting

## Relevance for recommenders
- Prompting: useful only for explanation or hybrid text understanding.
- RAG: useful if item knowledge or content needs grounding.
- Fine-tuning: useful for ranking or response generation in specific cases.

## Recommendation
Use these only as supporting techniques, not as the core recommender architecture.

---
# Use Case Suitability

## High-fit indicators
- Many items.
- Many users.
- Clear user action.
- Repeatable feedback loop.
- Measurable business outcome.

## Conclusion
Strong use case if discovery and ranking matter to the business.

---
