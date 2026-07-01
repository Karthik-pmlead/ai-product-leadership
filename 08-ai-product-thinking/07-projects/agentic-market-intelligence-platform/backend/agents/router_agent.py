import re


class RouterAgent:

    def __init__(self):
        pass

    def route(self, query: str):

        query_lower = query.lower()

        # ----------------------------
        # Competitor Analysis Detection
        # ----------------------------

        if " vs " in query_lower or "versus" in query_lower:

            company_a, company_b = (
                self._extract_competitors(query)
            )

            return {
                "intent":
                    "competitor_analysis",
                "company":
                    company_a,
                "secondary_company":
                    company_b
            }

        if "compare" in query_lower:

            company_a, company_b = (
                self._extract_competitors(query)
            )

            return {
                "intent":
                    "competitor_analysis",
                "company":
                    company_a,
                "secondary_company":
                    company_b
            }

        # ----------------------------
        # Industry Analysis
        # ----------------------------

        if any(
            keyword in query_lower
            for keyword in [
                "industry",
                "market",
                "sector"
            ]
        ):

            return {
                "intent":
                    "industry_analysis",
                "company":
                    self._extract_company(query)
            }

        # ----------------------------
        # Default: Company Analysis
        # ----------------------------

        return {
            "intent":
                "company_analysis",
            "company":
                self._extract_company(query)
        }

    # ----------------------------
    # Extract single company
    # ----------------------------

    def _extract_company(self, query: str):

        known_companies = [
            "Tesla",
            "Nvidia",
            "Microsoft",
            "Amazon",
            "Apple",
            "Google",
            "Meta",
            "BYD",
            "AMD",
            "Intel"
        ]

        for company in known_companies:

            if company.lower() in query.lower():

                return company

        # fallback cleanup
        cleaned = re.sub(
            r"(?i)\b(analyze|analyse|company|market|sector|compare|vs|versus)\b",
            "",
            query
        ).strip()

        return cleaned if cleaned else "Unknown"


    # ----------------------------
    # Extract competitors
    # ----------------------------

    def _extract_competitors(self, query: str):

        query_clean = re.sub(
            r"(?i)compare",
            "",
            query
        )

        if " vs " in query_clean.lower():

            parts = query_clean.split("vs")

        elif " versus " in query_clean.lower():

            parts = query_clean.split("versus")

        else:

            return (
                self._extract_company(query),
                "Unknown"
            )

        company_a = parts[0].strip()
        company_b = parts[1].strip()

        # normalize via known list

        company_a = self._match_known(company_a)
        company_b = self._match_known(company_b)

        return company_a, company_b


    def _match_known(self, text: str):

        known_companies = [
            "Tesla",
            "Nvidia",
            "Microsoft",
            "Amazon",
            "Apple",
            "Google",
            "Meta",
            "BYD",
            "AMD",
            "Intel"
        ]

        for company in known_companies:

            if company.lower() in text.lower():

                return company

        return text.strip() if text.strip() else "Unknown"
