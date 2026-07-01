import time
import uuid


class Telemetry:

    def __init__(self):
        self.events = []

    def start(self, agent_name):

        return {
            "id": str(uuid.uuid4()),
            "agent": agent_name,
            "start_time": time.time()
        }

    def end(
        self,
        event,
        input_data=None,
        output=None,
        prompt=None,
        context=None,
	confidence=None
    ):

        latency = (
            time.time()
            - event["start_time"]
        ) * 1000

        trace = {
            "id": event["id"],
            "agent": event["agent"],
            "latency_ms": round(latency, 2),
            "input": input_data,
            "prompt": prompt,
            "context": context,
            "output": output,
            "confidence": confidence
        }

        self.events.append(trace)

        return trace
