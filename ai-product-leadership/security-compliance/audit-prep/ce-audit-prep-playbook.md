# CE‑Audit‑Prep Playbook (IoT / Product‑Safety)

Use this playbook in the **6–8 weeks before a CE‑Marking‑style product‑safety audit** for IoT or cyber‑physical products (e.g., smart lock, sensor, industrial‑controller).

---

## 1. Scope and systems

- [ ] Define **which products and variants** are in‑scope for CE‑audit.  

- [ ] List **applicable‑directives**:
  - e.g., Low‑Voltage‑Directive, EMC‑Directive, Machinery‑Directive, Radio‑Equipment‑Directive, etc.  

- [ ] Identify **key‑components**:
  - Hardware, firmware, connectivity, user‑manuals.

---

## 2. Risk‑assessment and Technical File

- [ ] **Risk‑assessment** completed:
  - `risk-management/registers/example-ce-risk-register.md` up‑to‑date.  
  - Hazards, risk‑levels, and mitigations clearly documented.

- [ ] **Technical‑File** assembled:
  - Design‑and‑manufacturing‑information.  
  - Risk‑assessment‑summary.  
  - Test‑reports (IP‑rating, heat‑test, mechanical‑stress, electrical‑safety).  
  - User‑manuals and safety‑instructions.

- [ ] Ensure **product‑safety‑by‑design** reflected:
  - Safe‑default‑states for failure‑modes (power‑loss, low‑battery, comms‑loss).  
  - Tamper‑detection and logging where applicable.

---

## 3. Safety‑and‑security‑controls

- [ ] **Hardware‑controls**:
  - Overcurrent‑and‑over‑temperature‑protection.  
  - Mechanical‑guards or physical‑locks‑as‑needed.  

- [ ] **Firmware‑controls**:
  - Watchdog‑timer‑based‑reboot.  
  - Secure‑boot and signed‑firmware‑updates.  

- [ ] **Access‑control**:
  - Strong‑auth and MFA‑if‑relevant for admin‑functions.  

- [ ] **Logging**:
  - Unlock‑events, tamper‑attempts, firmware‑update‑status recorded.

---

## 4. Test‑plans and evidence

- [ ] **Physical‑and‑environmental‑tests**:
  - IP‑rating, heat‑and‑cold‑tests, mechanical‑endurance‑tests documented.  

- [ ] **Firmware‑and‑security‑tests**:
  - Safe‑failure‑mode‑tests (e.g., low‑battery, comms‑loss) documented.  
  - Auth‑bypass‑and‑tampering‑tests completed.

- [ ] **User‑documentation**:
  - Safety‑warnings and emergency‑unlock‑instructions in manuals and in‑app.

---

## 5. Internal‑mock‑CE‑audit

- [ ] Run a **mock‑CE‑audit**:
  - Walk through:
    - The risk‑assessment.  
    - The Technical‑File.  
    - The test‑reports.  

- [ ] Check:
  - Is the **hazard‑analysis** exhaustive?  
  - Are **failure‑modes** adequately‑covered?  
  - Are **user‑manuals** clear and up‑to‑date?

- [ ] Update any missing‑sections or gaps found.

---

## 6. During the audit

- [ ] Designate:
  - A **CE‑primary contact** (product‑or‑hardware‑lead).  
  - A **central‑document‑hub** (this folder, plus your internal‑wiki).

- [ ] Be ready to:
  - Explain the **risk‑assessment**.  
  - Demonstrate **test‑reports**.  
  - Show **user‑manuals and safety‑instruct
