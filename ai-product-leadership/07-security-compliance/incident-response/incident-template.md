# Incident Documentation Template

Use this template to document **any security, data, or product‑safety incident** in a consistent, structured way. This directly feeds into:
- `risk-management/rca-template.md` (for RCA).  
- `audit-prep/` (evidence for GDPR, ISMS, CE‑style audits).

---

## 1. Incident metadata

- **Incident title**  
  - Short, descriptive title (e.g., `High‑severity‑unauthorized‑data‑exposure‑via‑API`).

- **Incident ID**  
  - e.g., `INC‑2026‑001`.

- **Date/time of detection (UTC)**  
  - e.g., `2026‑03‑25T14:15:00Z`.

- **Date/time of resolution / stabilization (UTC)**  
  - e.g., `2026‑03‑25T18:30:00Z`.

- **Owner(s)**  
  - Incident‑lead: `name@company.com`.  
  - Product‑owner: `name@company.com`.  
  - Compliance‑lead: `name@company.com`.

- **Related systems / features**  
  - e.g., `Web API /users/:id`, `Admin‑console`, `Smart‑lock‑v2.1`.

- **Compliance / standard(s)**  
  - e.g., `GDPR`, `ISO‑27001`, `CE‑Machinery‑Directive`.

---

## 2. Impact summary

- **What happened (1–2 sentences)**  
  - Clear, non‑technical summary for stakeholders.

- **What is affected**  
  - Systems, data, users, devices, or safety‑relevant‑functions.

- **Impact level**  
  - e.g., `Low / Medium / High / Critical`  
  - Justification: How many users, what data, what risk (e.g., data‑breach, outage, physical‑harm).

---

## 3. Timeline

Describe the **key events** in chronological order:

- **YYYY‑MM‑DD HH:MM** – First‑indication of incident (e.g., alert, log, user‑report).  
- **YYYY‑MM‑DD HH:MM** – Incident‑lead notified; war‑room created.  
- **YYYY‑MM‑DD HH:MM** – Containment‑actions taken.  
- **YYYY‑MM‑DD HH:MM** – Investigation‑started; evidence‑preserved.  
- **YYYY‑MM‑DD HH:MM** – Remediation‑implemented; service‑back‑to‑stable.  
- **YYYY‑MM‑DD HH:MM** – Communication‑sent to users / regulators.

---

## 4. Root‑cause analysis (RCA)

- **Reference**  
  - Link to `risk-management/rca-template.md` for the full‑RCA structure.

- **Immediate‑cause**  
  - What directly led to the incident (e.g., “Missing API‑auth‑check”, “Firmware‑bug‑in‑state‑machine”).

- **Process‑cause**  
  - e.g., “No access‑control‑test‑case”, “Missing‑manual‑override‑test”.

- **Systemic‑cause**  
  - e.g., “No default‑auth‑on‑admin‑endpoints”, “No watchdog‑timer‑on‑device”.

- **Risk‑level**  
  - Likelihood, Impact, Risk‑score, Risk‑level (per your risk‑matrix).

---

## 5. Actions taken

- **Containment / immediate‑fix**  
  - e.g., “Blocked‑API‑endpoints”, “Revoked‑tokens”, “Disabled‑feature‑X”, “Manual‑unlock‑enabled”.

- **Long‑term‑remediation**  
  - e.g., “Add auth‑checks to all endpoints”, “Implement watchdog‑timer and safe‑state‑logic”, “Add new‑test‑cases”.

- **Tickets created**  
  - e.g., `JIRA‑ID‑SEC‑001`, `JIRA‑ID‑PRIV‑002`, `JIRA‑ID‑IOT‑003`.

---

## 6. Communication

- **Internal comms**  
  - What was communicated to leadership, legal, security‑team, support.

- **External comms**  
  - If applicable:
    - “User‑notification sent on YYYY‑MM‑DD”.  
    - “Regulator‑report filed on YYYY‑MM‑DD”.

---

## 7. Lessons‑learned and follow‑up

- **What went well**  
  - e.g., “Quick‑detection via logging”, “Effective‑containment”.

- **What went wrong**  
  - e.g., “Missing test‑case”, “No watchdog‑timer‑configured”.

- **Improvements planned**  
  - e.g., “Add security‑checklist to PR‑template”, “Update risk‑register with new‑risk `CE‑008`”.

- **Link to audit‑preparation**  
  - e.g., “This incident and RCA feed into `audit-prep/gdpr-audit-prep-checklist.md` and `audit-prep/ce-audit-prep-playbook.md`.”

---

## 8. Attachments / evidence

- Logs, screenshots, configuration‑snippets (without exposing secrets).  
- Test‑reports or device‑logs if relevant.  
- Any external‑reports or VAPT‑findings that contributed to detection.
