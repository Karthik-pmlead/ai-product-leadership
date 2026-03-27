# GDPR Feature‑Design Playbook

Use this playbook every time you design a **new feature that collects, processes, or exposes personal data** (e.g., user profiles, consent, analytics, marketing, IoT‑device‑user‑mapping). It ensures **GDPR‑style thinking** is baked into the PRD, not added as a late‑stage legal‑patch.

---

## 1. When to run this playbook

Run this playbook:

- At **PRD kickoff** for any feature touching:
  - User identifiers (email, phone, device‑ID, IP).  
  - Sensitive data, behavioural‑tracking, or consent‑management.  
- During **design‑reviews** and before **final‑wireframes / API‑specs**.
- For **existing features** that are being redesigned or expanded.

---

## 2. Step 1 – Define GDPR‑relevance

Ask and document:

- **What personal data** does this feature involve?  
  - List each field (e.g., `email`, `location`, `device‑ID`, `activity‑log`).  
- **What is the purpose** of collecting each field?  
  - e.g., “Enable login”, “Send transactional emails”, “Personalised recommendation”.  
- **What is the lawful‑basis**?  
  - Consent, contract, legitimate‑interest, legal‑obligation, etc.  
- **Does this feature relate to any user‑rights**?  
  - Access, rectification, erasure, restriction, portability, objection.

Add this as a **GDPR‑section** in the PRD.

---

## 3. Step 2 – Bake in privacy‑by‑design principles

For each feature, make sure:

- **Data‑minimisation**  
  - Only collect data that is **strictly necessary** for the stated purpose.  
  - Avoid “nice‑to‑have” fields.  

- **Consent‑management**  
  - If consent is the lawful‑basis:
    - Add a **clear consent‑checkbox or toggle**.  
    - Default to **“off”** for marketing/analytics.  
    - Make it **easy to withdraw** consent later.  

- **Right‑to‑be‑forgotten and right‑to‑erasure**  
  - Ensure the feature can:
    - Delete user‑data on demand.  
    - Break links to pseudonymised‑or‑anonymised‑data where appropriate.  

- **Data‑retention**  
  - Define **retention‑periods** per data‑type (e.g., logs = 90 days, support‑tickets = 2 years).  
  - Implement **auto‑deletion** where possible.

Include these as **explicit requirements** in the PRD and acceptance‑criteria.

---

## 4. Step 3 – Design user‑facing flows

For each key GDPR‑pattern, sketch a flow:

- **Consent‑flow**  
  - When is consent asked?  
  - Where is it stored?  
  - How is it re‑captured if changed?  

- **Access‑and‑portability‑flow**  
  - “Download my data” page or API.  
  - Format (JSON, CSV).  

- **Deletion‑flow**  
  - “Delete my account” button or support‑request.  
  - What is preserved (e.g., fraud‑logs) vs erased.  

- **Rectification‑flow**  
  - Edit‑profile UX; validation; confirmation.  

Make sure **designers and UX** co‑own this section.

---

## 5. Step 4 – Align with risk and logging

- **Add to risk‑register**  
  - Create a risk‑item for each GDPR‑pattern (e.g., `GDPR‑001`, `GDPR‑002`) in `risk-management/registers/example-gdpr-risk-register.md`.  

- **Logging**  
  - Log key GDPR‑events:
    - Consent‑change.  
    - Data‑access or deletion‑request.  
    - Data‑breach‑detection‑events.  

- **Testing**  
  - QA‑plan should include:
    - “Can I withdraw consent and verify it’s honoured?”  
    - “Can I delete my data and check downstream systems?”  
    - “Are logs recording GDPR‑relevant‑events correctly?”

---

## 6. Example usage in a sprint

- **Sprint‑0 (Discovery)**  
  - Run this playbook to define GDPR‑relevance and lawful‑basis; add GDPR‑requirements to PRD.

- **Sprint‑1 (Build)**  
  - Implement consent‑UI, deletion‑flow, and logging.  
  - Mark GDPR‑related tickets in JIRA with “GDPR‑feature‑design” label.

- **Sprint‑2 (Hardening)**  
  - QA‑team runs GDPR‑test‑scenarios.  
  - Security‑lead reviews logging and risk‑register status.

This playbook turns **GDPR** from a legal exercise into a **product‑design lever** that shapes requirements from day one.
