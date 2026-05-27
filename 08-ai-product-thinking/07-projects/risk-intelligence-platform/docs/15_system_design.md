# System Design

## Current MVP Design

```text
Frontend → FastAPI → Risk Engine → Alert Layer → WebSocket Stream
```
Scaled Design
```
Kafka → Feature Store → ML Risk Engine → Alert Queue → Analyst Dashboard
```

### Scalability Considerations
- horizontal API scaling
- event partitioning
- distributed stream processing
- async alert pipelines

### Reliability Considerations
- retries
- dead-letter queues
- monitoring
- observability
- audit logging
