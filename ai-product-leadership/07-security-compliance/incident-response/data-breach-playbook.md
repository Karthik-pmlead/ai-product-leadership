# Data‑Breach Playbook (GDPR‑Style)

Use this playbook when a **data‑breach or suspected data‑breach** is detected, particularly involving personal data of users.

---

## 1. When to run this playbook

- When there is indication of:
  - Unauthorised‑access to personal data (e.g., database‑exposure, API‑leak, misconfigured‑storage).  
  - Accidental‑leak (e.g., misconfigured‑CDN, test‑data‑in‑prod).  
  - Misuse of data (e.g., insider‑abuse, phishing, account‑takeover‑at‑scale).

Once triggered, merge this with `incident-response-playbook.md` and run both in parallel.

---

## 2. Roles and responsibilities (GDPR‑specific)

- **Incident‑lead**  
  - Coordinates with legal and communications on GDPR‑timelines.  

- **Legal‑/compliance‑lead**  
  - Ensures GDPR‑Article‑33‑style breach‑notification‑timelines are met (e.g., 72‑hour‑window).  

- **Product‑owner**  
  - Owns user‑communication and impact‑assessment.  

- **Engineering‑lead**  
  - Contains the breach and preserves evidence.

---

## 3. Phase 1 – Detection & Triage

- [ ] **Detect**  
  - Identify the breach (e.g., exposed‑database‑URL, log‑pattern, third‑party‑report).  

- [ ] **Estimate affected data**  
  - What personal data was exposed?  
    - e.g., emails, passwords, payment‑card‑IDs, device‑IDs, locations.  
  - How many users affected?  

- [ ] **Classify severity**  
  - High‑risk breaches (e.g., passwords, financial‑data) require:
    - Immediate user‑notification.  
    - Possibly regulator‑notification.  

- [ ] **Escalate**  
  - Notify:
    - Incident‑lead.  
    - Legal‑/compliance‑lead.  
    - Product‑o
