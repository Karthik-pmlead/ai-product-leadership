# Secure Incident & Data‑Event Playbook

Use this playbook when a **security incident, data‑event, or safety‑near‑miss** is suspected. It ensures a **structured, repeatable response** that aligns with ISO‑27001, GDPR‑notification‑requirements, and product‑safety‑thinking.

---

## 1. Trigger conditions

Run this playbook when:

- There is indication of:
  - A **data‑breach** (unauthorised‑access, exfiltration, accidental‑leak).  
  - A **security‑incident** (unauthorised‑access, malware, exploit‑attempt).  
  - A **product‑safety‑incident** (device‑failure‑leading‑to‑harm or near‑harm).  

- Or when:
  - Logs show abnormal‑activity.  
  - Third‑parties report suspicious‑activity.  

---

## 2. Roles and responsibilities

- **Incident‑lead**  
  - Usually a **security‑lead** or **product‑lead** with technical‑authority.  
- **Communications‑lead**  
  - Internal‑comms or legal‑team member responsible for external‑messaging.  
- **Engineering‑lead**  
  - Ensures investigation‑data, logs, and fixes are available.  
- **Product‑owner**  
  - Ensures user‑impact and remediation‑plan are clear.  

Document this in a **War Room** or **Status‑channel** (e.g., Slack / MS Teams).

---

## 3. Step 1 – Triage and initial assessment

Within **15–30 minutes** of detection:

- [ ] **Contain** the immediate threat (e.g., block IPs, revoke tokens, isolate service).  
- [ ] **Preserve evidence** (logs, stack traces, network‑captures, screenshots).  
- [ ] Estimate:
  - What systems / data / users are affected.  
  - Potential **impact** (data‑breach, outage, safety‑harm).  
  - Rough **timeline** of the incident.

---

## 4. Step 2 – Deep‑dive investigation

- [ ] Run an **RCA** using `risk-management/rca-template.md`.  
- [ ] Gather:
  - Relevant logs and metrics.  
  - User‑activity records.  
  - Configuration‑and‑deployment‑history.  
- [ ] Classify **risk‑level** using your risk‑matrix (e.g., High / Critical).

---

## 5. Step 3 – Mitigation and remediation

- [ ] Implement **immediate fixes** (e.g., patch, roll‑back, access‑revocation).  
- [ ] Update **risk‑register** if new patterns emerge.  
- [ ] Plan **long‑term fixes** (e.g., refactor‑auth, add logging, redesign‑flow) and link them to tickets.  

Prioritise based on **risk‑level** and **business‑impact**.

---

## 6. Step 4 – Communication and reporting

- Internally:
  - Communicate to stakeholders (leadership, legal, support) with a clear summary:
    - What happened.  
    - What is impact.  
    - What is being done.  
- Externally (if required):
  - Prepare **user‑notification** (e.g., email, in‑app‑banner) for GDPR‑style data‑breach‑notification.  
  - Coordinate with **legal** on regulator‑reporting timelines.

---

## 7. Step 5 – Post‑incident review

Within **1–2 weeks** after stabilization:

- [ ] Hold a **post‑incident‑review** meeting.  
- [ ] Update:
  - `risk-management/registers/...`  
  - Secure‑coding‑guidelines or design‑playbooks if needed.  
- [ ] Track **lessons‑learned** and **action items** with owners and deadlines.

---

## 8. Example incident‑timeline

You can paste this into your incident‑doc:

- **16:15** – Alert triggered on unusual‑amount‑of‑failed‑login‑attempts.  
- **16:20** – Incident‑lead notified; war‑room created.  
- **16:30** – IPs blocked; service‑partially isolated.  
- **17:00** – Logs‑gathering starts; suspect activity‑pattern identified.  
- **18:00** – RCA‑draft shared; long‑term‑fix‑ticket‑created.  

This playbook turns **incidents** into **structured, repeatable learning** instead of chaos.
