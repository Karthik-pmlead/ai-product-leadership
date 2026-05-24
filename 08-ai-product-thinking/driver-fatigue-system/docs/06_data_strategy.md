# Data Strategy

## Data Sources
- Live webcam video stream (primary)
- Face landmark coordinates (MediaPipe output)
- Derived features:
  - Eye Aspect Ratio (EAR)
  - Blink count
  - Eye closure duration

## Data Processing Pipeline
1. Frame capture via WebRTC
2. Face landmark extraction (MediaPipe)
3. Feature computation (EAR, blink signals)
4. Temporal aggregation (rolling windows)

## Storage Strategy (MVP)
- No persistent storage (real-time system only)
- Optional in-memory buffers for trend visualization

## Future Data Strategy
- Store anonymized feature vectors
- Time-series fatigue logs per driver
- Use for supervised learning (fatigue prediction models)

## Data Privacy
- No face images stored
- Only derived numerical features used
