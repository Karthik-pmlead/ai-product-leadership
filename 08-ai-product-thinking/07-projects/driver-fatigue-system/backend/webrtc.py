import json
from aiortc import VideoStreamTrack
from av import VideoFrame

from backend.face_metrics import FaceMetrics
from backend.blink_detector import BlinkDetector
from backend.fatigue_v2 import FatigueEngineV2


face = FaceMetrics()
blink = BlinkDetector()
engine = FatigueEngineV2()


class VideoTrack(VideoStreamTrack):

    def __init__(self, track, channel_holder):
        super().__init__()
        self.track = track
        self.channel_holder = channel_holder
        self.counter = 0

    async def recv(self):

        # ---------------------------
        # FRAME
        # ---------------------------
        frame = await self.track.recv()
        img = frame.to_ndarray(format="bgr24")

        # ---------------------------
        # MEDIAPIPE EAR
        # ---------------------------
        ear, landmarks = face.process(img)

        if ear is None:
            ear = 0.25  # fallback safe value

        # ---------------------------
        # BLINK + MICROSLEEP
        # ---------------------------
        blink_data = blink.update(ear)

        # ---------------------------
        # FATIGUE SCORE ENGINE
        # ---------------------------
        result = engine.update(
            ear=blink_data["ear"],
            blink_count=blink_data["blink_count"]
        )

        # merge signals
        result["blink_count"] = blink_data["blink_count"]
        result["microsleep"] = blink_data["microsleep"]

        # ---------------------------
        # SEND VIA DATA CHANNEL
        # ---------------------------
        self.counter += 1

        if self.counter % 3 == 0:

            channel = self.channel_holder.get("channel")

            if channel:
                try:
                    print("📤 sending:", result)
                    channel.send(json.dumps(result))

                except Exception as e:
                    print("❌ Send error:", e)

        # ---------------------------
        # return frame
        # ---------------------------
        return VideoFrame.from_ndarray(img, format="bgr24")
