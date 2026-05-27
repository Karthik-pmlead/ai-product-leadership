# 06 - Data Strategy

# Overview

The platform models financial ecosystems as interconnected graph data.

---

# Data Types

## 1. Entity Data
Represents:
- banks
- hedge funds
- exchanges
- traders
- companies

Attributes:
- risk score
- entity type
- identifiers

---

## 2. Relationship Data

Represents:
- transactions
- exposure
- ownership
- dependencies

Stored as graph edges.

---

## 3. Event Data

Examples:
- liquidity stress
- fraud alert
- market anomaly
- news event

Used to dynamically update risk.

---

## 4. News Intelligence Data

Simulated:
- investigations
- regulatory concerns
- market sentiment

Influences graph risk propagation.

---

# Data Flow

```text
Event → Risk Engine → Graph Update → Alerts → UI
```

## Storage Strategy (MVP)

#### Current:
in-memory graph store

#### Future:

- Neo4j
- TigerGraph
- distributed graph DB
- Scalability Considerations

#### Future production system may require:

- streaming pipelines
- distributed graph computation
- event sourcing
- temporal graph storage
