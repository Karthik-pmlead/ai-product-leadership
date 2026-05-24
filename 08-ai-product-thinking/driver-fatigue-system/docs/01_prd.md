# Product Requirements Document (PRD)

## Goal
Build a real-time driver fatigue detection system with <300ms latency.

## Features
- Live webcam streaming via WebRTC
- Face landmark detection (MediaPipe)
- EAR-based eye tracking
- Blink detection
- Microsleep detection
- Fatigue scoring engine
- Real-time UI dashboard with trend graph
- Audio alert system

## Non-Goals
- No deep learning training pipeline (v1)
- No cloud deployment (MVP)
- No multi-driver orchestration (future scope)

## Success Criteria
- Detect blink events in real-time
- Detect microsleep within 1.5s eye closure
- UI updates within <300ms latency
