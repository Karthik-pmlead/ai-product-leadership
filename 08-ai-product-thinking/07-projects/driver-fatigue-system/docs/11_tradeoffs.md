# System Tradeoffs

## 1. Rule-Based vs ML Model
- Chosen: Rule-based (EAR + thresholds)
- Reason: Low latency, interpretable
- Tradeoff: Lower adaptability vs deep learning models

## 2. Edge vs Cloud Processing
- Chosen: Edge processing (local backend)
- Reason: Privacy + latency constraints
- Tradeoff: Limited scalability

## 3. MediaPipe vs Custom CV Model
- Chosen: MediaPipe
- Reason: Robust, production-grade, fast integration
- Tradeoff: Less control over model internals

## 4. Real-time vs Batch Processing
- Chosen: Real-time streaming
- Tradeoff: No historical deep analytics in MVP
