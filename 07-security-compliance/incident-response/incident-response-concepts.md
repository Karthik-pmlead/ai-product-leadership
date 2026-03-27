# Incident Response – Core Concepts

This document defines the **core concepts** you can use when running incidents for security, data, and product‑safety‑related events.

---

## 1. What is an “incident”?

In a product‑security context, an **incident** is:

> *An event that compromises or threatens the confidentiality, integrity, or availability of data, systems, or product‑safety.*

Common types:

- **Security incident**  
  - e.g., unauthorised‑access, malware, exploit, DDoS.  
- **Data‑incident / breach**  
  - e.g., accidental‑leak, unauthorised‑exposure, misuse of data.  
- **Product‑safety‑incident or near‑miss**  
  - e.g., device‑failure‑leading‑to‑harm, safety‑hazard‑detected, erroneous‑actuation.

---

## 2. Incident‑response phases

Most teams follow a **phased model**:

1. **Detection & triage**  
   - Identify that something is wrong (alert, log, user‑report).  
   - Estimate impact and decide whether to escalate.

2. **Containment & mitigation**  
   - Stop the immediate threat (e.g., block IPs, revoke tokens, halt‑service‑partially, isolate device).  
   - Prevent further damage.

3. **Investigation & RCA**  
   - Gather logs, metrics, configs, and user‑traces.  
   - Run an **RCA** using `risk-management/rca-template.md`.

4. **Remediation**  
   - Implement fixes:
     - Patch, roll‑back, redeploy, reconfigure.  
   - Update risk‑register and controls.

5. **Communication**  
   - Internal comms (leadership, legal, support, users).  
   - If needed, external‑comms (regulator, customers, press).

6. **Post‑incident review & learning**  
   - Hold a **post‑incident‑review**.  
   - Update:
     - Playbooks,  
     - Risk‑register,  
     - Training‑material.

---

## 3. Key roles

- **Incident‑lead**  
  - Usually a **security‑lead** or **product‑lead** with technical‑and‑product‑authority.  
  - Manages the incident‑timeline, roles, and decisions.

- **Communications‑lead**  
  - Often **legal** or **PR/comms**; responsible for internal and external‑messaging.

- **Engineering‑lead**  
  - Ensures logs, configs, and code‑changes are available for investigation and fix.

- **Product‑owner**  
  - Ensures user‑impact and remediation‑plan are clear; owns timelines for product‑fixes.

- **Compliance / Audit‑lead**  
  - Ensures the incident‑handling and documentation aligns with GDPR, ISO‑27001, or CE‑expectations.

---

## 4. Why this matters for product‑leadership

- By treating incident‑response as a **product‑process**, you:
  - Turn chaos into a **structured workflow**.  
  - Turn incidents into **measurable learning** (e.g., “N incidents‑to‑fix; M preventable‑with‑this‑control”).  
- Your incident‑responses directly feed into:
  - `risk-management/registers/*` – new risks.  
  - `audit-prep/` – evidence of incident‑management and RCA.

This section sets the **conceptual foundation** for the concrete playbooks that follow.
