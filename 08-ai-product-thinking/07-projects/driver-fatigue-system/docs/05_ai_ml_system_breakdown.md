# AI/ML System Breakdown

## Feature Extraction
- MediaPipe FaceMesh landmarks

## Engineered Features
- Eye Aspect Ratio (EAR)
- Blink count
- Eye closure duration

## Temporal Modeling
- Moving average EAR
- Rolling fatigue score
- Microsleep detection thresholding

## Output
- Fatigue score (0–100)
- State: ACTIVE / DROWSY / CRITICAL
