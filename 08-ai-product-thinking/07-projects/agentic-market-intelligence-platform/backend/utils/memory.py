import time
from typing import Dict, Any, Optional


class MemoryStore:
    """
    Simple in-memory storage for agentic context persistence.
    Later upgrade path: Redis / FAISS / Vector DB
    """

    def __init__(self):

        # company -> memory object
        self.store: Dict[str, Any] = {}

    # -------------------------
    # SAVE CONTEXT
    # -------------------------

    def save(self, company: str, data: dict):

        if not company:
            return

        self.store[company] = {
            "data": data,
            "timestamp": time.time()
        }

    # -------------------------
    # GET CONTEXT
    # -------------------------

    def get(self, company: str) -> Optional[dict]:

        if not company:
            return {}

        entry = self.store.get(company)

        if not entry:
            return {}

        return entry.get("data", {})

    # -------------------------
    # DELETE MEMORY (optional)
    # -------------------------

    def clear(self, company: str):

        if company in self.store:
            del self.store[company]

    # -------------------------
    # DEBUG HELPERS
    # -------------------------

    def dump(self):

        return self.store
