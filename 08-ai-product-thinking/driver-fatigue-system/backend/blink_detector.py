class BlinkDetector:

    def __init__(self, ear_threshold=0.21, microsleep_frames=12):
        self.ear_threshold = ear_threshold
        self.microsleep_frames = microsleep_frames

        self.blink_count = 0
        self.closed_frames = 0
        self.was_closed = False

        self.microsleep_event = False

    def update(self, ear: float):

        if ear is None:
            return self._output(ear)

        is_closed = ear < self.ear_threshold

        # -------------------------
        # blink detection (edge)
        # -------------------------
        if is_closed and not self.was_closed:
            self.blink_count += 1

        # -------------------------
        # microsleep detection
        # -------------------------
        if is_closed:
            self.closed_frames += 1
        else:
            self.closed_frames = 0
            self.microsleep_event = False

        if self.closed_frames >= self.microsleep_frames:
            self.microsleep_event = True

        self.was_closed = is_closed

        return self._output(ear)

    def _output(self, ear):
        return {
            "blink_count": self.blink_count,
            "is_closed": ear < self.ear_threshold if ear else False,
            "microsleep": self.microsleep_event,
            "ear": float(ear) if ear else None
        }
