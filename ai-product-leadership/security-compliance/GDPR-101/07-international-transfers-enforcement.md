# GDPR 101 – International Data Transfers and Enforcement

This document explains GDPR rules for transferring data outside the EEA and how enforcement and fines work in practice, with a focus on product‑leadership and AI‑product teams.

---

## 1. International Data Transfers

Under GDPR, personal data cannot be sent to **third countries or international organisations** (i.e., outside the EEA) unless the transfer meets strict safeguards so that the **level of protection is not undermined**. [web:116][web:118][web:103]

### Key concepts

- **Third country**  
  Any country outside the EEA (e.g., India, US, Singapore).  
- **Transfer vs access**  
  A “transfer” occurs when a controller or processor in the EEA **discloses or makes data available** to an organisation in a third country, even if the data never leaves the EU‑based system. [web:116][web:123]

---

## 2. Legal Mechanisms for Transfers

### 1. Adequacy decisions
The European Commission can decide that a third country or region provides an **“adequate”** level of protection; transfers to those places are generally allowed without extra tools.

- Examples:  
  Canada, Japan, UK, Switzerland, New Zealand, and a few others. [web:118][web:123]  
- **Implication for product teams**  
  If you route EU data through adequate‑jurisdiction regions, you can often rely on adequacy as your main safeguard.

---

### 2. Standard Contractual Clauses (SCCs)

SCCs are **EU‑approved model contracts** that bind a data exporter (usually in the EU/EEA) and an importer (in a third country) to GDPR‑level obligations.

- **Common scenarios**  
  - EU SaaS → India engineering / support  
  - EU controller → US cloud provider  
- **Important nuance (Schrems II)**  
  You must assess whether the third‑country legal regime (e.g., surveillance laws) undermines those contractual protections; if it does, you must implement **additional safeguards** (e.g., encryption, access controls) or consider **Transfer Impact Assessments (TIAs)**. [web:116][web:118]

---

### 3. Binding Corporate Rules (BCRs)

BCRs are internal corporate rules approved by regulators for **multinational groups**. They allow **intra‑group** data transfers across borders while aligning all entities to GDPR‑level standards.

- Mainly used by large enterprises with complex global structures. [web:118]

---

### 4. Other tools and derogations

These are narrower and often higher‑risk, so product teams should avoid relying on them as default:

- **Approved codes of conduct or certifications**  
  Industry‑specific privacy frameworks approved under GDPR.
- **Derogations**  
  Explicit consent, necessity for contract, vital interests, or public‑task grounds, but only for **specific, limited situations**.

---

## 3. Enforcement and Fines

GDPR is **actively enforced** by national data protection authorities (DPAs) and can result in **very large fines** for serious or repeated breaches. [web:117][web:119][web:121][web:124]

### Who enforces GDPR?

- Each EU/EEA country has a **national data protection authority** (e.g., Irish DPC, CNIL, ICO‑style bodies). [web:117][web:124]  
- The **European Data Protection Board (EDPB)** coordinates cross‑border cases.

---

### Two‑tier fine structure (Article 83)

GDPR defines two main tiers of maximum fines:

| Tier | Max fine | Typical violations |
|------|----------|--------------------|
| **Tier 1 (lower‑tier)** | Up to **€10 million or 2% of global annual turnover** (whichever higher) | Failures in procedural obligations: missing records of processing, deficient DPA, lack of breach‑notification, weak DPIAs, inadequate security measures. [web:117][web:119] |
| **Tier 2 (higher‑tier)** | Up to **€20 million or 4% of global annual turnover** (whichever higher) | Violations of core principles and rights: unlawful processing, insufficient consent practices, unlawful international transfers, large‑scale violations of data‑subject rights. [web:119][web:121][web:124] |

---

### What enforcement looks like in practice

- **Investigations and audits**  
  DPAs can inspect your records, RoPA, DPIAs, DPAs, and other compliance artifacts. [web:117][web:124]  
- **Corrective actions**  
  Regulators can order you to:  
  - Stop processing.  
  - Deletion or anonymization of data.  
  - Implement specific technical and organisational measures.  
- **Administrative fines**  
  Issued for systemic failures, especially around **data transfers, consent, security, and profiling**. [web:117][web:121]

---

### Lessons from major fines

- **Big‑tech and ad‑tech**  
  Meta, Google, Amazon, and others have received **hundreds of millions of euros** for violations such as insufficient legal basis, weak consent‑management, unlawful profiling, and **deficient international transfer safeguards**. [web:121][web:124]  
- **Retail, travel, and profiling**  
  Companies using excessive tracking or profiling without proper justification or transparency have faced large fines tied to **consent and TIA failures**. [web:117][web:124]

---

## 4. Product‑Level Takeaways

- **Map and label transfers**  
  - Know which data is **EU‑subject**, and where it physically or logically resides (India, US, EU, etc.).  
  - Label whether transfers are covered by **adequacy, SCCs, TIAs, or derogations**. [web:116][web:123]  

- **Design around transfers**  
  - Avoid **indiscriminate cross‑border flows** (e.g., EU data funneling into global ML training clusters without safeguards).  
  - Prefer **data‑residency‑aware** architectures (e.g., EU‑only data plane for EU‑user data).

- **Treat fines as a product‑risk**  
  - Factor **GDPR‑level security**, **consent design**, and **DSAR workflows** into product budgets and timelines.  
  - Consider “GDPR‑risk profiles” for features involving **profiling, automation, or cross‑border data sharing**.

---

> **Next document:** [`08-india-centric-gdpr-in-practice.md`](08-india-centric-gdpr-in-practice.md) – GDPR‑in‑practice view for India‑based product and engineering teams.
