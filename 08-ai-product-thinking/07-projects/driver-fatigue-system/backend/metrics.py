import time

class Metrics:
    def __init__(self):
        self.events = []

    def log(self, status, ear):
        self.events.append({
            "timestamp": time.time(),
            "status": status,
            "ear": float(ear) if ear else None
        })

    def summary(self):
        total = len(self.events)
        drowsy = len([e for e in self.events if e["status"] == "DROWSY"])
        sleepy = len([e for e in self.events if e["status"] == "SLEEPY"])

        return {
            "total_frames": total,
            "drowsy_frames": drowsy,
            "sleepy_frames": sleepy
        }
