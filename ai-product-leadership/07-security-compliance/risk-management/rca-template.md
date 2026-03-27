# Root‑Cause Analysis (RCA) – Template

Use this template after any **security incident, data‑event, or product‑safety‑near‑miss** to systematically document what happened and how to prevent recurrence.

---

## 1. Incident overview

- **Incident title**:  
- **Date/time of discovery**:  
- **Duration (if known)**:  
- **Affected systems / features**:  
- **Impact summary** (e.g., data‑breach, outage, safety‑implication):  

---

## 2. Timeline

Create a **timeline** of key events (UTC‑based if possible):

| Time (UTC) | Event |
|------------|------|
| 2026‑03‑20 08:15 | Admin API endpoint exposed in logs |  
| 2026‑03‑20 08:22 | Automated alert triggered |  
| 2026‑03‑20 08:30 | Security team starts triage |  

---

## 3. Description of the problem

- **What happened**: 2–3 clear sentences.  
- **What did not happen as expected**:  
- **Observations / evidence**: (logs, screenshots, stack traces, test‑results).  

---

## 4. Root‑cause analysis

Use a simple **5‑Why**‑style or **layered‑cause** model:

- **Direct cause** (immediate technical‑glitch).  
- **Process cause** (e.g., missing code‑review check, missing test‑case).  
- **Systemic / design‑cause** (e.g., no default‑auth‑on‑admin‑endpoints, no secrets‑scanner in CI).  

---

## 5. Lessons learned and action items

- **Action items** (short, concrete bullets):

  - e.g., “Add auth‑requirements to all admin‑endpoints by 2026‑04‑15.”  
  - e.g., “Add secrets‑scanning to CI/CD pipeline by 2026‑04‑30.”  

- **Owner** for each action item.  
- **Status** (Open / In‑Progress / Done).  

---

## 6. Risk‑register link

- Add a **risk‑ID** from `risk-management/registers/...` to track this as a formal risk.  
- Or create a new risk if this is a previously‑unknown pattern.
