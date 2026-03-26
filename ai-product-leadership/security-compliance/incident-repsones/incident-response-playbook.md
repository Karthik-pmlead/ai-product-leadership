# Incident Response Playbook (General)

Use this as the **main playbook** whenever a **security, data, or product‑safety incident** is suspected. It is language‑agnostic and product‑agnostic (with examples for web, API, and IoT).

---

## 1. When to trigger this playbook

Trigger this playbook when:

- There is indication of:
  - Unauthorised‑access to data or systems.  
  - Malware, exploit, or compromise.  
  - Unexpected‑system‑behaviour that could affect users or safety.  
- Or when:
  - Logs show abnormal‑activity patterns.  
  - Third‑parties report suspicious‑activity.

Once triggered, create an **Incident War Room** (e.g., Slack channel, MS Teams group, or Notion page) and assign roles.

---

## 2. Roles and responsibilities

- **Incident‑lead**  
  - Owns the incident from detection to closure.  
  - Coordinates all other roles.

- **Communications‑lead**  
  - Drafts and approves internal and external‑messaging.  
  - Ensures GDPR‑style breach‑notifications are prepared on time.

- **Engineering‑lead**  
  - Provides technical‑expertise, logs, configs, and fixes.  
  - Implements containment and remediation.

- **Product‑owner**  
  - Owns user‑impact, timelines, and user‑communication.  
  - Ensures roadmap‑adjustments are captured for security‑debt‑reduction.

- **Compliance / Security‑lead**  
  - Ensures incident‑handling aligns with GDPR, ISMS, or CE‑rules.  
  - Updates risk‑register and audit‑preparation materials.

---

## 3. Phase 1 – Detection & Triage (0–30 minutes)

- [ ] **Detect**  
  - Identify that something is wrong (alert, log, user‑report, penetration‑test, etc.).  

- [ ] **Triage**  
  - Estimate:
    - What is affected (systems, data, users, devices)?  
    - What is the **impact** (data‑breach, outage, safety‑harm, financial, reputational)?  
    - What is the **timeline** (first‑signs, peak‑impact, current‑state)?  

- [ ] **Escalate**  
  - Notify:
    - Incident‑lead.  
    - Security‑team.  
    - Product‑lead.  

- [ ] **Create war room**  
  - Open a dedicated channel with:
    - Incident‑lead,  
    - Communications‑lead,  
    - Engineering‑lead,  
    - Product‑owner,  
    - Compliance‑lead.  

- [ ] **Initial‑status**  
  - Write a 3–5 sentence **incident‑summary** and share it in the war‑room.

---

## 4. Phase 2 – Containment & Mitigation (30–120 minutes)

- [ ] **Contain** the immediate threat  
  - e.g., block IPs, revoke tokens, isolate service, power‑down‑device‑remotely (if safe), close‑exposed‑endpoint.  

- [ ] **Preserve evidence**  
  - Take snapshots of logs, configs, network‑captures, screenshots, device‑states.  
  - Avoid overwriting critical‑data.

- [ ] **Stabilize**  
  - Restore critical‑functionality for users, if possible, without reintroducing risk.  

- [ ] **Update stakeholders**  
  - Notify leadership, legal, and support with a short‑update:
    - What happened (in simple terms).  
    - What is being done.

---

## 5. Phase 3 – Investigation & RCA (Hours–Days)

- [ ] **Run an RCA** using `risk-management/rca-template.md`  
  - Gather:
    - Logs, metrics, configs, user‑traces.  
    - Timeline of events.  
    - Evidence of what went wrong.

- [ ] **Identify root‑causes**  
  - Direct cause (technical‑glitch).  
  - Process cause (e.g., missing test, missing code‑review, missing logging).  
  - Systemic cause (e.g., no default‑auth on admin‑endpoints, no secrets‑scan).

- [ ] **Classify risk‑level**  
  - Use your risk‑matrix:
    - Likelihood, Impact, Risk‑score, Risk‑level.  

- [ ] **Update risk‑register**  
  - Add new risks or update existing ones in `risk-management/registers/...`.

---

## 6. Phase 4 – Remediation (Days–Weeks)

- [ ] **Implement immediate fixes**  
  - e.g., patch, roll‑back, redeploy, reconfigure.  

- [ ] **Plan long‑term fixes**  
  - e.g., refactor‑auth, add logging, redesign‑flow, add new‑tests, implement SAST/SCA.  

- [ ] **Track fixes**  
  - Create tickets and link them to the incident‑ID.  
  - Assign owners and deadlines.

- [ ] **Validate**  
  - Test the fixes in staging / canary / controlled‑environments.

---

## 7. Phase 5 – Communication (Throughout and post‑incident)

- **Internally**  
  - Provide regular updates to:
    - Leadership.  
    - Legal.  
    - Support.  
  - Share a concise **incident‑summary** and **timeline**.

- **Externally (if required)**  
  - Prepare user‑notifications (e.g., email, in‑app banner).  
  - Coordinate with legal on:
    - GDPR‑style breach‑notification‑timeline.  
    - Regulator‑reporting requirements.  

- **Compliance**  
  - Ensure incident‑handling and communications align with:
    - GDPR‑Article‑33 (breach‑notification).  
    - ISO‑27001‑incident‑management‑principles.  
    - CE‑Marking‑style product‑safety‑incident‑handling.

---

## 8. Phase 6 – Post‑incident review & learning (1–2 weeks)

- [ ] **Hold a post‑incident‑review**  
  - Invite:
    - Incident‑lead.  
    - Comms‑lead.  
    - Engineering‑lead.  
    - Product‑owner.  
    - Compliance‑lead.  

- [ ] **Document lessons‑learned**  
  - What went well.  
  - What went wrong.  
  - What can be improved (process, tooling, culture).

- [ ] **Update artifacts**  
  - `risk-management/registers/...` – add new‑risks.  
  - `secure-coding-guidelines.md` – add new‑anti‑pattern.  
  - `playbooks/` – update playbooks based on learnings.  

- [ ] **Track action 
