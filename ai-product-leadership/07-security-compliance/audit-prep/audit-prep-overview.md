# Audit‑Prep – Overview and Mindset

This document explains **how to think about audits** and how to prepare for them in a product‑leadership‑friendly way.

---

## 1. What an audit usually looks for

Auditors (GDPR, ISO‑27001, CE‑style) typically want to see evidence of:

- **Governance & accountability**  
  - Who owns what? (e.g., data‑protection‑officer, security‑lead, product‑owner).  

- **Policies and controls**  
  - Are there documented **policies** (`policies/data-protection-policy.md`, `policies/security-policy.md`, etc.)?  
  - Are there **controls** that match those policies (e.g., MFA, logging, access‑reviews)?  

- **Risk‑management**  
  - Is there a **risk‑assessment** and a **risk‑register**?  
  - Are high‑and‑critical‑risks being mitigated or reasonably accepted?

- **Evidence and traceability**  
  - Can you show that:
    - Features are designed with security‑and‑compliance in mind (`playbooks/design-and-development-policy.md`)?  
    - Tests were run (`playbooks/pre-launch-checklist.md`)?  
    - Incidents were handled and learned from (`playbooks/secure-incident-playbook.md`, `risk-management/rca-template.md`)?  

---

## 2. How to structure your audit‑prep

Treat audit‑prep as a **product‑epic** with its own:

- **Scope**: Which systems, products, or assets are in‑scope?  
- **Timeline**: 4–6 weeks before the audit is typical.  
- **Roles**:
  - **Product‑owner**: Overall scope and evidence‑ownership.  
  - **Engineering‑lead**: Technical‑evidence (logs, configs, code‑reviews).  
  - **Security‑/compliance‑lead**: Maps evidence to standards (GDPR‑Art‑5, ISO‑27001‑controls, CE‑directives).  

---

## 3. Typical audit‑prep cadence

- **6–4 weeks before**  
  - Review scope and **list potential‑evidence‑sources** (PRDs, risk‑registers, logs, test‑plans).  

- **4–2 weeks before**  
  - Start **gathering and organizing** evidence.  
  - Fix obvious‑gaps (e.g., missing‑logging‑for‑failed‑login, untagged‑risk‑items).  

- **2–1 weeks before**  
  - Conduct an **internal‑mock‑audit** or “dry‑run” with someone playing the auditor.  
  - Clarify questions and update documents.

- **Audit week**  
  - Designate:
    - A **primary contact** for each topic (e.g., GDPR, ISMS, CE‑Marking).  
    - A **war‑room** (physical or virtual) where evidence is shared.

---

## 4. How this fits into your repo

Use this overview to:

- Align `audit-prep/` with:
  - `policies/`,  
  - `risk-management/`,  
  - `playbooks/`,  
  - `videos/` (if you want to point to external references).  

By the time an auditor arrives, this folder should be **the single source of truth** for:
- “What do we do?”  
- “How do we prove it?”  
- “What are our open‑risks?”
