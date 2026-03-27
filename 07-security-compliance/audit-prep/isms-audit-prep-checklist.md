# ISO‑27001 / ISMS Audit‑Prep Checklist

Use this checklist in the **4–6 weeks before an ISO‑27001‑style information‑security audit** for your product‑systems and infrastructure.

---

## 1. Policies and controls

- [ ] **Information‑security‑policy** (`policies/security-policy.md`) is up‑to‑date and understood by product‑and‑engineering‑leads.  

- [ ] **Access‑control‑policy** (`policies/access-control-policy.md`) implemented:
  - RBAC enforced.  
  - MFA for admins.  
  - Secrets‑management tools used.  

- [ ] **Secure‑development‑policy** (`policies/secure-development-policy.md`) followed:
  - OWASP‑Top‑10‑aligned secure‑coding‑guidelines in use.  
  - VAPT / SAST / SCA integrated into CI/CD.

---

## 2. Risk‑management and evidence

- [ ] **Risk‑assessment** performed:
  - `risk-management/registers/example-owasp-risk-register.md` up‑to‑date.  
  - High‑and‑critical‑risks have mitigation‑plans or justification.

- [ ] **Risk‑register** aligned with:
  - Product‑backlog (tickets created for remediation).  
  - Sprint‑planning (security‑debt visible).

- [ ] **Incident‑response** and **RCA** documented:
  - `playbooks/secure-incident-playbook.md`, `risk-management/rca-template.md`.

---

## 3. Technical controls and logging

- [ ] **Access‑reviews**:
  - Periodic‑access‑reviews performed (e.g., quarterly) for admin‑and‑privileged‑accounts.  

- [ ] **Logging and monitoring**:
  - Failed‑login attempts, admin‑actions, and critical‑errors logged.  
  - SIEM‑or‑equivalent‑alerting enabled.

- [ ] **Patch‑management**:
  - OS, libraries, and frameworks kept up‑to‑date.  
  - Critical‑vulnerabilities remediated within defined‑SLAs.

- [ ] **Network‑and‑infrastructure‑security**:
  - Firewalls, segmentation, and secure‑configurations in place.  

---

## 4. Training and awareness

- [ ] **Security‑awareness** training completed:
  - `training/owasp-top-10-talk.md`.  
  - `training/secure-coding-lightning-talk.md`.  

- [ ] **Product‑leaders** participated in:
  - Secure‑development‑policy‑briefings.  
  - Threat‑modeling‑workshops.

---

## 5. Internal‑mock‑audit

- [ ] Run an **internal‑ISMS‑mock‑audit**:
  - Ask:
    - “Can the auditor see the security‑policy?”  
    - “Can they see evidence of access‑reviews?”  
    - “Can they see evidence of incident‑management?”  

- [ ] Fix gaps:
  - e.g., add missing‑logging, update‑risk‑items, clarify‑policy‑language.

---

## 6. During the audit

- [ ] Designate:
  - A **ISMS‑primary contact** (security‑lead).  
  - A **central‑evidence‑hub** (this folder, plus internal‑wikis).

- [ ] Track **audit‑questions** and **answers** in a simple log for later follow‑up.

This checklist ensures your **ISMS‑evidence** is product‑aligned and easy to demonstrate.
