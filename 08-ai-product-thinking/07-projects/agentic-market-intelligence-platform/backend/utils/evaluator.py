class Evaluator:

    def score_risks(self, risks: list):

        if not risks:
            return {
                "quality": 0.0,
                "confidence": 0.0,
                "coverage": 0.0
            }

        # Simple heuristic scoring (MVP version)

        quality = min(len(risks) / 5, 1.0)
        confidence = 0.7 if len(risks) >= 3 else 0.5
        coverage = min(len(set(risks)) / 5, 1.0)

        return {
            "quality": round(quality, 2),
            "confidence": round(confidence, 2),
            "coverage": round(coverage, 2)
        }

    def score_opportunities(self, ops: list):

        if not ops:
            return {
                "quality": 0.0,
                "confidence": 0.0,
                "coverage": 0.0
            }

        quality = min(len(ops) / 5, 1.0)
        confidence = 0.75 if len(ops) >= 3 else 0.55
        coverage = min(len(set(ops)) / 5, 1.0)

        return {
            "quality": round(quality, 2),
            "confidence": round(confidence, 2),
            "coverage": round(coverage, 2)
        }

    def score_recommendations(self, recs: list):

        if not recs:
            return {
                "quality": 0.0,
                "actionability": 0.0
            }

        quality = min(len(recs) / 3, 1.0)
        actionability = 0.8 if len(recs) >= 2 else 0.6

        return {
            "quality": round(quality, 2),
            "actionability": round(actionability, 2)
        }
