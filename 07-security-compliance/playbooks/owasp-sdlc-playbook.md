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
  - “All user‑input used in queries or commands must be parameterized or strongly‑sanitized.”  
  - Use schema‑validation and strict escaping.

- **A07 – Authentication**  
  - “All auth‑endpoints use strong‑password‑rules and MFA where applicable.”  
  - Logs capture failed‑login attempts.

- **A10 – SSRF**  
  - “URL‑fields must be allow‑listed or sandboxed; no direct‑internal‑calls.”

Bind these to specific **acceptance‑criteria**.

---

## 4. Step 3 – Embed into SDLC stages

### Discovery / PRD

- Run a **threat‑model** using `risk-management/threat-model-template.md`.  
- Add **OWASP‑risk‑items** to `risk-management/registers/example-owasp-risk-register.md`.

### Design

- Finalize **data‑contracts and schemas**; enforce input‑validation at borders.  
- Sketch **auth‑and‑RBAC** models (e.g., roles, scopes).

### Development

- Follow **secure‑coding‑guidelines** (`secure-coding-guidelines.md`).  
- Use **linter‑plugins** for SAST / secrets‑scan.  
- Do **manual‑checks** for OWASP‑patterns before PRs.

### PR Review

- Add a **security‑checklist** to PR templates:
  - Is auth‑present on all sensitive endpoints?  
  - Are all inputs parameterized and escaped?  
  - Are secrets externalised and not hardcoded?

### Testing

- QA‑plan should include:
  - Auth‑bypass tests.  
  - Injection‑type tests.  
  - SSRF‑style tests (if applicable).  
- Use DAST / VAPT‑style scanning for high‑risk features.

### Pre‑release

- Verify **OWASP‑risk‑register** is up‑to‑date; all high‑and‑critical items either mitigated or accepted.  
- Ensure **logging for security‑events** (failed‑logins, admin‑actions, errors).

---

## 5. Example in a sprint

- **Sprint‑0**  
  - Tag OWASP‑categories on PRD tickets; update risk‑register.

- **Sprint‑1–2**  
  - Implement controls, write tests, and run SAST.  
  - Mark OWASP‑fixes in PRs (e.g., `OWASP‑003`).

- **Post‑release**  
  - Track OWASP‑risk‑status in quarterly‑releases; review missing‑pieces.

This playbook makes **OWASP** a **product‑level habit**, not just a security‑team checklist.
