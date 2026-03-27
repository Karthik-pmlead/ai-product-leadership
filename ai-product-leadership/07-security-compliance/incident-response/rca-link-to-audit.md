# Linking RCA to Audit Evidence

This document explains how **incident‑response and RCA** connect to your **GDPR, ISO‑27001, and CE‑Marking‑style audit‑preparation**. It ensures that incidents are not just “handled and forgotten” but used as **positive evidence of due‑diligence**.

---

## 1. Why this matters for audits

- Auditors (GDPR, ISMS, CE‑style) want to see:
  - **Incident‑management**  
    - That you detect, contain, investigate, and learn from incidents.  
  - **Root‑cause analysis**  
    - That you don’t just fix symptoms but address underlying‑causes.  
  - **Continuous‑improvement**  
    - That you update policies, risk‑registers, and controls based on incidents.

By linking each incident‑RCA to your audit‑preparation materials, you show:
- **Accountability**.  
- **Systematic‑risk‑management**.  
- **Product‑safety‑and‑security‑by‑design**.

---

## 2. How to link RCA to your folders

For **every resolved incident** documented with `incident-template.md` and `risk-management/rca-template.md`:

- **Link to risk‑management**  
  - In `risk-management/registers/*`:
    - Add a new risk or update an existing risk using the Incident‑ID and RCA‑ID.  
    - Example:  
      - Risk‑ID `GDPR‑BREACH‑001` → Linked to Incident‑ID `INC‑2026‑001` and RCA.  

- **Link to policies**  
  - In `policies/security-policy.md`, `policies/data-protection-policy.md`, or `policies/ce-safety-policy.md`:
    - Add a section:  
      - “Incidents‑and‑learning” listing key‑incidents and their impact on policy‑updates.

- **Link to audit‑preparation**  
  - In `audit-prep/gdpr-audit-prep-checklist.md`, `audit-prep/isms-audit-prep-checklist.md`, or `audit-prep/ce-audit-prep-playbook.md`:
    - Add a row:  
      - “Evidence‑of‑incident‑management”: “See `incident-response/incident-template.md` for Incident‑ID‑INC‑2026‑001 and RCA‑document.”  

---

## 3. Concrete examples

### GDPR‑style data‑breach

- **Incident**  
  - `incident-response/incident-template.md` for `INC‑2026‑001` (data‑breach).  
- **RCA**  
  - `risk-management/rca-template.md` explaining missing‑auth‑on‑endpoint and no‑logging‑for‑failed‑logins.  
- **Audit‑link**  
  - In `audit-prep/gdpr-audit-prep-checklist.md`:
    - “We have documented incident‑and‑RCA for a data‑breach (e.g., `INC‑2026‑001`) showing detection, containment, user‑notification, and long‑term‑remediation‑plan.”

### ISO‑27001‑style security incident

- **Incident**  
  - `incident-template.md` for `INC‑2026‑002` (unauthorized‑admin‑access).  
- **RCA**  
  - `rca-template.md` identifying missing‑MFA‑on‑admin‑console.  
- **Audit‑link**  
  - In `audit-prep/isms-audit-prep-checklist.md`:
    - “Evidence‑of‑security‑incident‑handling and RCA for `INC‑2026‑002` is maintained; MFA‑requirements‑are‑now‑enforced‑on‑all‑admin‑consoles.”

### CE‑style product‑safety incident

- **Incident**  
  - `incident-template.md` for `INC‑2026‑003` (smart‑lock‑failure‑to‑unlock).  
- **RCA**  
  - `rca-template.md` finding a firmware‑bug‑in‑state‑machine.  
- **Audit‑link**  
  - In `audit-prep/ce-audit-prep-playbook.md`:
    - “Incident‑and‑RCA for `INC‑2026‑003` are documented in Technical‑File; the firmware‑bug‑was‑fixed and a new‑safe‑state‑logic‑implemented‑for‑low‑battery‑failure‑modes.”

---

## 4. Best practices for auditors

- **Centralise**  
  - Keep a **list of incidents** (e.g., in `incident-response/INCIDENT-INDEX.md`) with:
    - Incident‑ID,  
    - Title,  
    - Link to `incident-template.md` and `rca-template.md`.  

- **Index in Technical‑File**  
  - For CE‑Marking, reference this list in the **Technical‑File** as evidence of:
    - “incident‑management and continuous‑improvement of safety‑and‑security‑design”.

- **Show evolution**  
  - In your audit‑review, show:
    - “Incident‑N → RCA‑N → Updated‑policy / updated‑risk‑register / updated‑design”.  

This turns **every incident** into a **story of learning and improvement**, not just a problem‑to‑hide.
