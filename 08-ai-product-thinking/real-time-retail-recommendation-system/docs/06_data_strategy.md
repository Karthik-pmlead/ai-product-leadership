# 06 - Data Strategy

## Data Sources

### 1. User Event Stream
Generated events:
- view
- click
- cart
- purchase

---

### 2. User Profile Data
Derived data:
- category preference scores
- long-term interest model

---

### 3. Session Data
Short-term memory:
- recent actions
- interaction sequence

---

### 4. Product Catalog
Static dataset:
- product id
- category
- metadata

---

## Data Flow

User Event → Event API → Session Store → Profile Update → Ranking Engine

---

## Data Storage (MVP)

- In-memory dictionaries
- session_store
- user_profile
- user_item_matrix

---

## Future Production Upgrade

- Kafka event streaming
- Redis session store
- Data lake (S3 / BigQuery)
- Feature store (Feast)

---

## Data Quality Considerations

- deduplication of events
- session expiration handling
- noisy event filtering
