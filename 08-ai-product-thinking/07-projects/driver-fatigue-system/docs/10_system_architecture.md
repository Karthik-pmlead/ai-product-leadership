# System Architecture

## Components

Frontend:
- WebRTC video capture
- DataChannel receiver
- UI + graph rendering

Backend:
- FastAPI signaling server
- aiortc WebRTC pipeline
- MediaPipe face processing
- fatigue engine

## Data Flow
Camera → WebRTC → Backend → AI Processing → DataChannel → UI
