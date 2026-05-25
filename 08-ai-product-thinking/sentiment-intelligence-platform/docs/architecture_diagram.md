```mermaid
flowchart TD

A[Customer Review Stream] --> B[FastAPI Backend]

B --> C[NLP Sentiment Inference]

B --> D[Topic Classification Engine]

B --> E[MLOps Metrics Layer]

C --> F[Explainability Layer]

D --> F

F --> G[WebSocket Streaming Layer]

E --> G

G --> H[React Operational Dashboard]

H --> I[Sentiment Analytics]

H --> J[Language Distribution]

H --> K[Topic Intelligence]

H --> L[MLOps Observability]
