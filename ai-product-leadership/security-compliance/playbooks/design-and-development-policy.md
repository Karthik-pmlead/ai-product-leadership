# Design & Development Policy Playbook

Use this playbook to ensure **security and compliance** are baked into every product‑design and development cycle, not added as a “final‑step” or “audit‑fix”.

---

## 1. When to run this playbook

Before starting or significantly changing any feature or component that:

- Handles **personal data** (GDPR‑style).  
- Provides **auth, payment, admin, or IoT‑safety‑related** functionality.  
- Uses **third‑party‑integrations or libraries** (OWASP‑style risk).  

Run this playbook in:
- Discovery / PRD phase.  
- Design‑review.  
- End‑of‑sprint hardening.

---

## 2. Step 1 – Map the risk & compliance categories

For each feature / system:

- **GDPR‑style**  
  - What personal data is involved?  
  - What is the **purpose** and **lawful‑basis** (consent, contract, legitimate‑interest, etc.)?  
  - What **user‑rights** (access, rectification, erasure, portability, etc.) must be supported?

- **ISO‑27001 / ISMS‑style**  
  - What **assets** (systems, data, secrets) are involved?  
  - What **controls** apply (access control, encryption, logging, patching, etc.)?

- **OWASP‑style**  
  - Which **OWASP‑Top‑10 categories** might apply?  
    - A01: Broken Access Control  
    - A03: Injection  
    - A07: Identification and Authentication Failures  
    - A10: SSRF, etc.

- **CE‑style (IoT‑products)**  
  - What **hazardous situations** are possible?  
  - What **safe‑default‑state** is expected if the device fails or is attacked?

Mark each relevant category on the PRD or JIRA‑ticket.

---

## 3. Step 2 – Define “security‑and‑compliance requirements”

For each feature, add explicit requirements to the PRD / acceptance‑criteria:

- **Data‑protection**  
  - “Collect only X fields; others are optional.”  
  - “User must give explicit consent for Y (marketing/analytics).”  

- **Access control**  
  - “User cannot access `/users/:id` of others.”  
  - “Admin‑functions require MFA.”

- **Secure‑coding**  
  - “Use parameterized queries for all SQL.”  
  - “Validate all inputs using schema‑validation.”

- **Logging & monitoring**  
  - “Log all failed‑login attempts and admin‑actions.”  
  - “Alert on N failures‑in‑1h.”

- **Product‑safety (IoT / CE‑style)**  
  - “In case of power‑loss, lock defaults to X‑state.”  
  - “Device enters fail‑safe‑mode when temp‑threshold is crossed.”

---

## 4. Step 3 – Embed into SDLC gates

Make security‑and‑compliance checks part of your normal workflow:

- **Design‑review**  
  - Run a **threat‑model** using `risk-management/threat-model-template.md`.  
  - Map OWASP‑categories and GDPR‑principles explicitly.

- **PR template**  
  - Add a “Security & Compliance” section:
    - “Which OWASP‑categories apply?”  
    - “Is this feature GDPR‑relevant?”  
    - “Are there any CE‑style safety‑implications?”

- **Test‑plan**  
  - Add:
    - Auth‑bypass tests.  
    - Injection‑type tests.  
    - GDPR‑type flows (consent‑change, delete‑account).  
    - CE‑style failure‑scenarios (low‑battery, heat, comms‑loss).

- **Release‑gate**  
  - Before deployment, verify:
    - SCA / dependency‑scan clean.  
    - SAST / secrets‑scan clean.  
    - Logging and monitoring in place for critical‑paths.

---

## 5. Example usage in a sprint

| Activity            | What to do using this playbook |
|---------------------|---------------------------------|
| **PRD kickoff**     | Tag GDPR‑/OWASP‑/CE‑relevance in PRD; define baseline requirements. |
| **Design‑review**   | Run threat‑model; document risks in `risk-management/registers/...`. |
| **Sprint‑demo**     | Show that security‑and‑compliance requirements are demo‑ready alongside UX. |
| **Post‑launch**     | Track any new‑risks added (e.g., via incident‑RCA) and update risk‑register. |

This playbook makes **security‑and‑compliance** part of the **normal product‑rhythm**, not an after‑thought.
