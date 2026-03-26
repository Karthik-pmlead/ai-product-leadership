# Product‑Safety Incident Playbook (IoT / CE‑Style)

Use this playbook when a **product‑safety‑incident or near‑miss** is detected, particularly for IoT or cyber‑physical products (e.g., smart lock, sensor, industrial‑controller). This playbook is aligned with CE‑Marking‑style safety‑thinking and ISO‑27001‑style incident‑management principles.

---

## 1. When to run this playbook

Run this playbook when:

- A **device‑failure leads to, or nearly leads to, physical‑harm** (e.g., lock‑failure‑trapping‑user, brake‑system‑malfunction, overheating).  
- A **safety‑hazard** is detected (e.g., overheating, unexpected‑actuation, loss‑of‑control).  
- A **near‑miss** is reported (e.g., “I almost got trapped”, “door‑almost‑didn’t‑unlock”, “device‑started‑smoking”).

Once triggered, merge this with `incident-response/incident-response-playbook.md` and run both together.

---

## 2. Roles and responsibilities (safety‑specific)

- **Incident‑lead**  
  - Coordinates the overall incident; ensures safety‑and‑compliance‑leads are looped in.  

- **Product‑safety‑/hardware‑lead**  
  - Owns:
    - Hardware‑failure‑analysis.  
    - Safety‑design‑and‑safe‑default‑state‑review.  

- **Firmware‑/embedded‑lead**  
  - Owns:
    - Firmware‑behaviour during failure‑modes.  
    - Watchdog‑timer, safe‑state‑logic, OTA‑recovery.  

- **Product‑owner**  
  - Owns user‑impact, communication, and roadmap‑impact for safety‑debt‑reduction.  

- **Compliance / CE‑lead**  
  - Ensures incident‑handling aligns with CE‑Marking‑style product‑safety‑expectations and Technical‑File‑requirements.

---

## 3. Phase 1 – Detection & Triage (0–30 minutes)

- [ ] **Detect**  
  - Identify the safety‑incident or near‑miss via:
    - User‑support‑ticket.  
    - Field‑report.  
    - Internal‑testing.  
    - Monitoring‑alert (e.g., temperature‑threshold, actuator‑abnormality).  

- [ ] **Triage**  
  - Estimate:
    - What happened (e.g., lock‑failed‑to‑unlock, device‑overheated, unexpected‑actuation).  
    - What is affected:
      - Devices‑in‑field,  
      - Users‑at‑risk,  
      - Installation‑environment (home, office, industrial).  
    - What is the **potential‑impact** (physical‑harm, injury, fire, monetary‑loss, reputational‑damage)?  

- [ ] **Escalate**  
  - Notify:
    - Incident‑lead.  
    - Safety‑/hardware‑lead.  
    - Firmware‑lead.  
    - Compliance / CE‑lead.  
    - Product‑owner.  

- [ ] **Create a safety‑war‑room**  
  - Open a dedicated channel and add all above roles.  
  - Assign a **safety‑incident‑owner** (often safety‑/hardware‑lead) to coordinate technical‑analysis.

---

## 4. Phase 2 – Containment & Mitigation (30–120 minutes)

- [ ] **Contain** the immediate risk to users  
  - Examples:
    - If the device is remotely controllable, disable or restrict unsafe‑functions.  
    - If it is a safety‑critical‑lock, ensure manual‑override‑or‑mechanical‑key‑is‑functional‑everywhere.  
    - In extreme cases, advise users to **power‑off** or **physically‑disconnect** the device, if safe and feasible.  

- [ ] **Preserve evidence**  
  - Gather:
    - Device‑logs,  
    - Firmware‑version,  
    - Environmental‑conditions (temperature, power‑supply, network‑state),  
    - Photos or videos if available.  
  - Do not overwrite or erase device‑or‑system‑state prematurely.

- [ ] **Stabilize**  
  - Restore safe‑operation if possible (e.g., roll‑back‑firmware, re‑calibrate, manual‑unlock).  
  - Temporarily disable or limit risky‑features until root‑cause is understood.

- [ ] **Update stakeholders**  
  - Inform:
    - Leadership.  
    - Compliance / CE‑lead.  
    - Support‑team (with guidance for what to tell affected‑users).  
  - Provide a short‑safety‑summary:
    - What happened.  
    - What is being done.  
    - Any immediate‑safety‑steps for users.

---

## 5. Phase 3 – Investigation & RCA (Hours–Days)

- [ ] **Run an RCA** using `risk-management/rca-template.md`  
  - Investigate:
    - The **technical‑cause** (e.g., firmware‑bug, race‑condition, sensor‑drift, power‑surge).  
    - The **process‑cause** (e.g., missing test‑case, no stress‑test for this‑scenario, no watchdog‑timer‑configured).  
    - The **systemic‑cause** (e.g., no safe‑default‑state for this‑failure‑mode, no over‑temperature‑protection).  

- [ ] **Classify risk‑level**  
  - Use your risk‑matrix:
    - Likelihood of recurrence.  
    - Impact (harm, injury, damage, downtime).  
    - Risk‑score and Risk‑level (Low / Medium / High / Critical).  

- [ ] **Update risk‑register**  
  - Add a new safety‑risk or update existing one in `risk-management/registers/example-ce-risk-register.md`.  

- [ ] **Document hazards and failure‑modes**  
  - Add any new‑hazards discovered to the product‑hazard‑analysis (e.g., new environmental‑scenario, new mechanical‑interaction).

---

## 6. Phase 4 – Remediation (Days–Weeks)

- [ ] **Implement immediate fixes**  
  - Examples:
    - Firmware‑patch to prevent unsafe‑state.  
    - Add watchdog‑timer‑based‑reboot or safe‑default‑state.  
    - Add over‑temperature‑or‑over‑current‑protection.  
    - Improve‑mechanical‑design (e.g., stronger‑case, better‑sealing).  

- [ ] **Plan long‑term fixes**  
  - Examples:
    - Redesign‑state‑machine to avoid hazardous‑states.  
    - Add new‑test‑cases for failure‑modes identified.  
    - Add logging for safety‑events and diagnostics.  
    - Improve‑user‑manuals with clearer‑safety‑warnings and procedures.

- [ ] **Track fixes**  
  - Create tickets linked to this incident‑ID.  
  - Assign owners and deadlines.

- [ ] **Validate**  
  - Test in:
    - Lab‑conditions that reproduce the incident.  
    - Field‑tests or canary‑rollouts, if feasible.  
  - Ensure the device behaves safely in failure‑scenarios.

---

## 7. Phase 5 – Communication (Throughout and post‑incident)

- **Internally**  
  - Keep leadership, safety‑team, and compliance‑lead informed with:
    - What happened.  
    - What caused it.  
    - What is being done.  

- **To users (if applicable)**  
  - Communicate:
    - That a safety‑issue or near‑miss has been identified.  
    - What is being done to fix it.  
    - Any immediate‑actions users should take (e.g., “Check‑device‑firmware‑version”, “Use‑mechanical‑key‑as‑backup”).  
  - Be transparent and empathetic.

- **To regulators / notified‑bodies (if required)**  
  - If the incident has implications for CE‑Marking or safety‑certification, coordinate with compliance‑lead to:
    - Report incidents as required.  
    - Provide evidence of investigation and remediation.  
  - Update Technical‑File with:
    - Incident‑analysis.  
    - Design‑and‑test‑changes.

---

## 8. Phase 6 – Post‑incident review & learning (1–2 weeks)

- [ ] **Hold a post‑safety‑incident‑review**  
  - Invite:
    - Incident‑lead.  
    - Safety‑/hardware‑lead.  
    - Firmware‑lead.  
    - Product‑owner.  
    - Compliance / CE‑lead.  

- [ ] **Document lessons‑learned**  
  - What went well (e.g., quick‑detection, effective‑containment).  
  - What went wrong (e.g., missing‑test‑case, late‑discovery).  
  - What can be improved (e.g., new‑test‑scenarios, better‑logging, safer‑default‑states).

- [ ] **Update artifacts**  
  - `risk-management/registers/example-ce-risk-register.md` – add new‑safety‑risk.  
  - `playbooks/ce-safety-plus-security-playbook.md` – add new‑pattern or lesson.  
  - `audit-prep/ce-audit-prep-playbook.md` – reflect improved incident‑handling.  
  - User‑manuals and safety‑instructions.

- [ ] **Track action items**  
  - Create tickets for:
    - New‑test‑cases.  
    - New‑safety‑controls.  
    - New‑logging‑or‑diagnostics.

---

## 9. Example incident‑structure (for your internal doc)

Use this as a template in your incident‑write‑up:

- **Incident title**  
- **Date/time of detection (UTC)**  
- **Device‑type / product‑variant**  
- **Affected users / installations**  
- **Incident‑description** (1–2 sentences)  
- **Hazard / hazardous‑situation**  
- **Impact summary**  
- **Containment‑actions**  
- **Timeline**  
- **RCA** (reference `rca-template.md`)  
- **Remediation‑plan**  
- **Comms‑plan**  

This playbook ensures **product‑safety‑incidents** are handled in a **systematic, CE‑aligned, product‑leadership‑owned** way that directly feeds into your broader security‑and‑compliance narrative.
