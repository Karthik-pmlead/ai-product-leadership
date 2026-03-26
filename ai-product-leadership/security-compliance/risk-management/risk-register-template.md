# Risk Register – Template

Use this template to create a **risk register** for any product, system, or initiative (e.g., GDPR‑launch, ISMS‑rollout, OWASP‑Top‑10‑remediation, CE‑Marking‑for‑smart‑lock).

---

## 1. How to use this template

For each major product or compliance‑program, create:

- `risk-management/registers/product-x-risk-register.md`  
- or `risk-management/registers/program-owasp-remediation.md`

Fill in one row per risk.

---

## 2. Risk register columns

| Column name            | Example values |
|------------------------|----------------|
| **Risk ID**            | RISK‑001 |
| **Subject / Title**    | Example: “Unauthenticated API endpoint exposes user data” |
| **Asset**              | Which asset is at risk (e.g., “User PII in API‑response”) |
| **Threat**             | e.g., “Attacker with API‑access”, “Insider‑employee‑misuse” |
| **Vulnerability**      | e.g., “Missing authentication on endpoint”, “No rate‑limiting” |
| **Likelihood (1–5)**   | e.g., 4 (Likely) |
| **Impact (1–5)**       | e.g., 5 (Critical) |
| **Risk score**         | `Likelihood × Impact` (e.g., 20 → Critical) |
| **Risk level**         | Low / Medium / High / Critical |
| **Risk‑owner**         | e.g., `po-engineer@company.com` |
| **Mitigation plan**    | e.g., “Add JWT‑auth + rate‑limiting, launch in v2.1” |
| **Due date**           | e.g., 2026‑06‑15 |
| **Status**             | Open / In‑progress / Mitigated / Accepted / Avoided |
| **Evidence / notes**   | e.g., “API‑test report attached”, “PR: #12345” |

---

## 3. Extra columns (optional)

- **Compliance link** – e.g., “GDPR‑Art‑5”, “ISO‑27001‑A.9”, “OWASP‑A01”, “CE‑Machinery‑Directive”.  
- **Linked PRD / JIRA** – e.g., “PRD‑LINK‑XYZ”, “JIRA‑ID‑ABC”.  
- **Review date** – Last‑time this risk was reviewed (e.g., quarterly).

This way, your risk register becomes both a **compliance document** and a **product‑backlog** for security‑and‑safety‑debt.
