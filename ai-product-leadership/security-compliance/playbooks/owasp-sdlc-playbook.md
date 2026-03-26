# OWASP‑Aligned SDLC Playbook

Use this playbook to **embed OWASP‑Top‑10‑style thinking into your SDLC** — from PRD to production — for any web, API, or microservices‑based product.

---

## 1. When to run this playbook

- During **feature‑kickoff** for any component that:
  - Handles user‑inputs (forms, APIs, search, upload).  
  - Involves auth, sessions, payments, or admin‑interfaces.  
  - Uses libraries or external‑services.  
- During **design‑reviews**, **sprint‑planning**, and **pre‑release** hardening.

---

## 2. Step 1 – Map OWASP‑categories to the feature

For each feature, tag which **OWASP‑Top‑10 categories** are relevant:

- **A01: Broken Access Control**  
  - Any endpoint that serves user‑specific‑data or admin‑functions.

- **A03: Injection**  
  - Any API, search, or user‑input‑to‑SQL / OS‑command / template‑path.

- **A07: Identification and Authentication Failures**  
  - Login, MFA, password‑reset, token‑management.

- **A10: SSRF**  
  - Any endpoint that uses user‑provided‑URLs (webhooks, imports, scrapers).

- Others (A02, A05, A06, A08, A09) as relevant.

Document this in a **PRD‑section** or JIRA‑field.

---

## 3. Step 2 – Define OWASP‑style requirements

Turn OWASP‑categories into **product‑level requirements**:

- **A01 – Access control**  
  - “User cannot access data or admin‑functions they shouldn’t.”  
  - Implement RBAC checks on every sensitive endpoint.

- **A03 – Injection**  
  - “All user‑input 
