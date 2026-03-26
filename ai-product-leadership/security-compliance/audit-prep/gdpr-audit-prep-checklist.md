# GDPR Audit‑Prep Checklist

Use this checklist in the **4–6 weeks before a GDPR‑style audit** to ensure your product‑level evidence is ready.

---

## 1. Data‑mapping and lawful‑basis

- [ ] **Data‑map** updated for each in‑scope system:
  - What personal data is collected?  
  - Where is it stored?  
  - Who has access?  

- [ ] **Lawful‑basis** documented for each data‑processing activity:
  - Consent, contract, legitimate‑interest, etc.  

- [ ] **Purpose‑limitation** clearly stated:
  - No data is reused for purposes not explicitly declared.

---

## 2. User‑rights and flows

- [ ] **Right‑to‑be‑informed**:
  - Privacy‑policy and in‑app‑consent‑texts are up‑to‑date.  

- [ ] **Right‑of‑access**:
  - “Download my data” or similar flow exists and is tested.  

- [ ] **Right‑to‑rectification**:
  - Edit‑profile and correction‑flows are functional.  

- [ ] **Right‑to‑erasure**:
  - “Delete my account” or delete‑request‑flow is implemented and tested.  

- [ ] **Right‑to‑data‑portability**:
  - Data can be exported in a structured‑format (e.g., JSON, CSV).  

- [ ] **Right‑to‑restriction & objection**:
  - Opt‑out‑mechanisms exist for marketing / analytics.

---

## 3. Logging, evidence, and DPIA

- [ ] **Consent‑events logged**:
  - When consent is given or withdrawn.  

- [ ] **Data‑access‑and‑deletion‑events logged**:
  - User‑initiated‑actions and admin‑actions.  

- [ ] **Data‑protection‑impact‑assessment (DPIA)**:
  - DPIA exists for high‑risk‑processing (e.g., large‑scale‑processing, new‑AI‑uses).  
  - DPIA references `risk-management/registers/example-gdpr-risk-register.md`.

- [ ] **Retention‑policies**:
  - Data‑retention‑periods documented and enforced (e.g., logs, support‑tickets, analytics).

---

## 4. Policies and training

- [ ] **Data‑protection‑policy** in `policies/data-protection-policy.md` is up‑to‑date and linked in PRDs.  

- [ ] **GDPR‑aware‑training** completed for:
  - Product‑managers (`training/gdpr-for-product-managers.md`).  
  - Engineers (if applicable).  

- [ ] **Incident‑response** and **RCA** playbooks ready:
  - `playbooks/secure-incident-playbook.md`, `risk-management/rca-template.md`.

---

## 5. Internal‑mock‑audit activities

- [ ] Run a **mock‑GDPR‑audit**:
  - Ask:
    - “Can the auditor see the data‑map?”  
    - “Can they see proof of consent‑management?”  
    - “Can they see proof of data‑deletion‑flows?”  

- [ ] Fix any gaps found:
  - e.g., add missing‑logging, clarify‑purpose‑statements, update‑PRDs.

---

## 6. During the audit

- [ ] Designate:
  - A **GDPR‑primary contact** per product.  
  - A **central evidence repository** (this folder, plus your JIRA / Notion / Confluence).

- [ ] Keep an **audit‑question log**:
  - Each question and its answer documented (`audit-prep/audit-questions-answered.md` – optional).

This checklist ensures your **product‑team** is audit‑ready, not just your security‑team.
