# System Overview

The system is a real-time AI pipeline:

1. Webcam captures video
2. WebRTC streams frames to backend
3. MediaPipe extracts facial landmarks
4. EAR computed per frame
5. Blink + microsleep detection runs
6. Fatigue scoring engine updates state
7. Results streamed back via DataChannel
8. Frontend renders alerts + trend graph
