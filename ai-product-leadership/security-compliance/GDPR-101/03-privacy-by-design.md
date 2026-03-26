# GDPR 101 – Privacy by Design and by Default

This document explains GDPR’s “data protection by design and by default” (Article 25) with a product‑management lens.

---

## 1. What “Privacy by Design” Means

- **In plain terms**  
  Privacy and data protection must be **baked into the product from the start**, not bolted on after development.

- **What it means for product**  
  - Identify privacy risks and data flows during **discovery and design**, not only during QA.  
  - Architect for **minimum data collection**, **pseudonymization**, **encryption**, and **access control** from day one.  
  - Treat privacy like performance or security: a **top‑level requirement** in PRDs and specs.

- **Example**  
  When designing an analytics dashboard:  
  - Decide early which events and fields are truly needed.  
  - Plan pseudonymization of user IDs and avoid storing raw PII in logs.  
  - Define retention and access‑control rules before writing code.

---

## 2. What “Privacy by Default” Means

- **In plain terms**  
  When a user interacts with a feature, the **most privacy‑protective setting is the default**, with no action required.

- **What it means for product**  
  - Use **opt‑in** (not opt‑out) for sensitive tracking, profiling, or third‑party sharing.  
  - Make data‑sharing, profiling, or public‑visibility features **off by default**.  
  - Where multiple options exist, the **least‑invasive** configuration is pre‑selected.

- **Example**  
  A B2C SaaS:  
  - Profile visibility is “private” or “only my team,” not public.  
  - Behavioral tracking and third‑party integrations are off until the user explicitly enables them.

---

## 3. Technical and Organisational Measures (PM Checklist)

At the product design level, you should ensure:

- **Data minimisation**  
  Only the fields and events strictly necessary for the use case are collected.

- **Pseudonymization & anonymization**  
  Use internal IDs instead of real identifiers where possible; anonymize data for analytics when individual‑level detail is not needed.

- **Encryption**  
  Require encryption at rest and in transit for PII.

- **Access controls**  
  Implement role‑based access (RBAC) and least‑privilege policies.

- **Retention and auto‑deletion**  
  Define retention periods per data type and design auto‑delete or archival flows.

- **DPIA‑trigger awareness**  
  Know when a feature requires a Data Protection Impact Assessment (e.g., profiling, biometrics, large‑scale monitoring).

---

> **Next document:** [`04-data-controller-processor.md`](04-data-controller-processor.md) – understanding who is responsible for what under GDPR.
