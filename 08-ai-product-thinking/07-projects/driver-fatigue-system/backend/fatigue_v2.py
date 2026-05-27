import numpy as np
from collections import deque


class FatigueEngineV2:

    def __init__(self):
        self.ear_history = deque(maxlen=15)
        self.score_history = deque(maxlen=60)

    def update(self, ear, blink_count=0):

        self.ear_history.append(ear)

        avg_ear = np.mean(self.ear_history)

        # -------------------------
        # fatigue score
        # -------------------------
        score = (1 - avg_ear) * 70 + min(blink_count * 2, 30)
        score = int(np.clip(score, 0, 100))

        self.score_history.append(score)

        status = (
            "ACTIVE" if score < 30 else
            "DROWSY" if score < 60 else
            "CRITICAL"
        )

        return {
            "score": score,
            "avg_ear": float(avg_ear),
            "status": status,
            "trend": list(self.score_history)
        }
