# GDPR 101 – Lawful Bases and Security / Compliance Techniques

This document covers GDPR’s six lawful bases for processing and key security and compliance techniques product teams should operationalize.

---

## 1. The Six Lawful Bases (Article 6)

### 1. Consent
Data processing is based on **clear, informed, specific, and revocable agreement** from the data subject.

- **When to use**  
  Often used for marketing, non‑core analytics, and optional features.

- **Product example**  
  A checkbox for “receive promotional emails,” with an easy unsubscribe flow.

---

### 2. Contract
Processing is necessary to **perform a contract** with the data subject.

- **When to use**  
  Onboarding, billing, delivery, account management.

- **Product example**  
  Collecting name, address, and payment details to fulfill an order.

---

### 3. Legal Obligation
Processing is required to comply with **law or regulation**.

- **When to use**  
  Tax, AML, employment‑law, or regulatory‑reporting requirements.

- **Product example**  
  A bank processing KYC data to comply with financial‑crime laws.

---

### 4. Vital Interests
Processing is necessary to **protect someone’s life or physical safety**.

- **When to use**  
  Rare, emergency‑only situations.

- **Product example**  
  A hospital sharing critical‑care data with another facility during an emergency.

---

### 5. Public Task
Processing is necessary for a **public authority** to perform an official task.

- **When to use**  
  Government‑related administration (e.g., taxation, public‑health records).

- **Product example**  
  A tax agency processing income data for tax‑assessment.

---

### 6. Legitimate Interests
Processing is necessary for a **legitimate interest** of the controller or a third party, unless overridden by the data subject’s rights.

- **When to use**  
  Fraud detection, security, internal analytics. Requires a **balancing test** and often a DPIA.

- **Product example**  
  Using IP logs and behaviour to detect and block fraud attempts.

---

## 2. Security Techniques Under GDPR (Article 32)

GDPR requires **“appropriate technical and organisational measures”** depending on the risk.

### Core technical measures

- **Encryption**  
  At rest and in transit for PII.

- **Access controls (RBAC, least privilege)**  
  Only required roles can access sensitive data.

- **Data minimisation & pseudonymization**  
  Collect only what you need and use tokens or internal IDs instead of raw identifiers.

- **Anonymization & generalization**  
  Aggregate or generalize data where individual‑level detail is not required.

- **Data‑masking & logging controls**  
  Mask PII in logs and non‑prod environments; define retention.

### Organizational / process techniques

- **Data inventory and classification**  
  Know what sensitive data you hold and where it lives.

- **Regular audits and risk assessments**  
  Security reviews, penetration tests, and DPIAs for high‑risk processing.

- **Breach detection and incident response**  
  Logging, alerting, and playbooks for 72‑hour breach reporting to regulators.

- **Retention and deletion automation**  
  Define retention periods and automate clean‑up.

- **Consent and preference management**  
  A system (CMP or in‑house) that records and honors consents and objections consistently.

---

## 3. Product‑Level Compliance Techniques

- Maintain **Records of Processing Activities (RoPA)** documenting every processing activity.  
- Design **DSAR workflows** (access, rectification, deletion, portability, restriction, objection) into the product.  
- Map data flows (including international transfers) and document transfer‑safeguards (SCCs, TIA, etc.).  
- Integrate **DPIA triggers** into feature design (e.g., profiling, biometrics, large‑scale monitoring).  

> **Next document:** [`07-international-transfers-enforcement.md`](07-international-transfers-enforcement.md) – transfers and GDPR enforcement.
