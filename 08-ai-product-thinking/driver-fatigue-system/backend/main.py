from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from aiortc import RTCPeerConnection, RTCSessionDescription

from backend.webrtc import VideoTrack

app = FastAPI()

# ---------------------------
# CORS (required for browser)
# ---------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pcs = []


@app.get("/")
def health():
    return {"status": "WebRTC Driver Fatigue API running"}


# ---------------------------
# WEBRTC OFFER ENDPOINT
# ---------------------------
@app.post("/offer")
async def offer(data: dict):

    print("🔥 OFFER RECEIVED")

    pc = RTCPeerConnection()
    pcs.append(pc)

    channel_holder = {"channel": None}

    # ---------------------------
    # DataChannel handler
    # ---------------------------
    @pc.on("datachannel")
    def on_datachannel(channel):
        print("📡 DataChannel created:", channel.label)

        channel_holder["channel"] = channel

        @channel.on("open")
        def on_open():
            print("✅ DataChannel OPENED")
            channel.send("connected")

    # ---------------------------
    # Video track handler
    # ---------------------------
    @pc.on("track")
    def on_track(track):
        print("📹 Track received:", track.kind)

        if track.kind == "video":
            pc.addTrack(VideoTrack(track, channel_holder))

    # ---------------------------
    # WebRTC handshake (IMPORTANT FIX)
    # ---------------------------
    offer = RTCSessionDescription(
        sdp=data["sdp"],
        type=data["type"]
    )

    # ✅ aiortc uses camelCase methods
    await pc.setRemoteDescription(offer)
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    print("📤 SDP answer created")

    return {
        "sdp": pc.localDescription.sdp,
        "type": pc.localDescription.type
    }
