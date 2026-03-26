# CE‑Style Safety + Security Playbook (IoT / Cyber‑Physical Products)

Use this playbook when designing or redesigning **IoT, embedded, or cyber‑physical products** (e.g., smart lock, sensor, industrial‑controller) that must meet **CE‑Marking‑style product‑safety and security expectations**.

---

## 1. When to run this playbook

- Before **launching a new IoT variant** or significantly changing:
  - Firmware, safety‑logic, access‑control, or connectivity.  
- During **product‑design reviews**, **DFMEA‑style meetings**, and **pre‑test‑campaign** planning.

---

## 2. Step 1 – Define safety‑and‑security scope

Ask and document:

- **What is the product?**  
  - e.g., “Smart lock controlling residential doors, connected via Bluetooth/Wi‑Fi.”  

- **What are the “safety‑relevant” functions?**  
  - e.g., “Lock‑and‑unlock commands”, “Emergency‑unlock”, “Tamper‑response”.

- **What are the “security‑relevant” functions?**  
  - e.g., “Auth‑and‑session‑management”, “OTA‑firmware‑update”, “Communication‑with‑gateway”.

- **What are the “hazardous situations”?**  
  - e.g., “User trapped behind locked door”, “Unauthorized‑unlock”, “Device‑bricked‑remotely”.

Add this as a **CE‑section** in the PRD or design‑document.

---

## 3. Step 2 – Perform CE‑style risk‑assessment

Use and expand `risk-management/registers/example-ce-risk-register.md`:

- **Hazard‑analysis**  
  - Brainstorm:
    - Mechanical‑hazards (pinching, force).  
    - Electrical‑hazards (overheating, power‑fault).  
    - Environmental‑hazards (moisture, dust, IP‑rating needs).  
    - Software‑hazards (firmware‑bricked, unexpected‑unlock, faulty‑state‑machine).  

- **Risk‑matrix**  
  - Rate each hazard by **Likelihood × Impact** (e.g., 1–5).  
  - Classify as **Low / Medium / High / Critical**.

- **Risk‑treatment**  
  - Choose:
    - **Mitigate** (e.g., add sensor, safe‑default‑state).  
    - **Avoid** (e.g., remove feature).  
    - **Accept** (with evidence and rationale).

Tie each risk‑item to a **design‑requirement** and **test‑case**.

---

## 4. Step 3 – Design safety‑plus‑security controls

Translate risks into product‑requirements:

- **Safe‑default‑states**  
  - Define what the device should do in failure‑modes:
    - Power‑loss, low‑battery, comms‑loss, bricked‑firmware, etc.  
  - Example: “In low‑battery scenario, lock remains unlockable via mechanical‑key.”

- **Hardware‑and‑firmware‑design**  
  - Include:
    - Overcurrent‑and‑over‑temperature‑protection.  
    - Watchdog‑timer‑based‑reboot.  
    - Secure‑boot and signed‑firmware‑updates.

- **Access‑control and auth**  
  - Ensure:
    - Only authorised‑users can initiate unlock.  
    - MFA or strong‑auth for admin‑operations.  

- **Logging and diagnostics**  
  - Device‑and‑gateway logs capture:
    - Unlock‑events.  
    - Tamper‑attempts.  
    - Firmware‑update‑status.

---

## 5. Step 4 – Plan tests and evidence‑generation

For each high‑and‑critical‑risk:

- **Physical‑and‑environmental‑tests**  
  - IP‑rating tests (e.g., IP65).  
  - Heat‑and‑cold‑tests.  
  - Mechanical‑stress‑tests (e.g., repeated‑locking).

- **Firmware‑and‑security‑tests**  
  - Safe‑failure‑mode‑test (e.g., low‑battery‑scenario, power‑off‑during‑update).  
  - Auth‑bypass / tampering‑tests (e.g., brute‑force, spoofed‑gateway).

- **User‑documentation**  
  - Safety‑warnings in manual and in‑app messages.  
  - Clear instructions for mechanical‑override and emergency‑unlock.

Document **test‑plans and test‑reports** as part of the **Technical File**.

---

## 6. Step 5 – Align with CE‑documentation and audits

- **Technical File**  
  - Ensure the CE‑risk‑register, design‑requirements, test‑plans, and reports are assembled.  

- **Declaration of Conformity (DoC)**  
  - Verify that:
    - Risk‑assessment and controls are documented.  
    - Testing‑evidence is attached.  
    - CE‑Marking‑guidelines for relevant‑directives are followed.

- **Audits**  
  - Use this playbook and the CE‑risk‑register as the **single source of truth** for:
    - Product‑safety‑and‑security‑design.  
    - Evidence‑of‑due‑diligence.

---

## 7. Example in an IoT‑sprint

- **Sprint‑0 (Discovery)**  
  - Run this playbook to define hazards and safe‑default‑states; update `example-ce-risk-register.md`.

- **Sprint‑1–3 (Design & build)**  
  - Implement hardware‑protections, firmware‑safe‑modes, and logging.  

- **Sprint‑4 (Test)**  
  - Execute physical‑and‑firmware‑test‑plans; update Technical File.

- **Post‑launch**  
  - Track new‑hazards via incident‑RCA and update risk‑register.

This playbook bridges **product‑leadership**, **engineering**, and **CE‑compliance** into one repeatable routine for safety‑plus‑security‑by‑design.
