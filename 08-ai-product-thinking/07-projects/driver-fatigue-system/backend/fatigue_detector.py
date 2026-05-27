class FatigueDetector:
    def __init__(self, ear_threshold=0.22, frame_limit=15):
        self.ear_threshold = ear_threshold
        self.frame_limit = frame_limit
        self.low_ear_frames = 0

    def analyze(self, ear):
        if ear is None:
            return "NO_FACE", 0.0

        if ear < self.ear_threshold:
            self.low_ear_frames += 1
        else:
            self.low_ear_frames = 0

        if self.low_ear_frames >= self.frame_limit:
            return "DROWSY", ear

        if ear < self.ear_threshold:
            return "SLEEPY", ear

        return "ALERT", ear
