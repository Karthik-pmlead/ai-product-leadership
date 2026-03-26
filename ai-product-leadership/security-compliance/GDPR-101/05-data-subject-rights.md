# GDPR 101 – Data Subject Rights

This document explains the core rights of data subjects under GDPR, with product‑level implications.

---

## 1. Right to Be Informed (Transparency)

- **What it means**  
  Individuals must be clearly informed about why and how their personal data is processed, including the legal basis, retention, and third‑party sharing.

- **Product implication**  
  - Privacy notices must be concise, layered, and linked at every data‑collection point.  
  - UX must clarify purposes (e.g., “We use this for fraud detection and marketing”).

- **Example**  
  A sign‑up flow shows a short banner plus a link to a privacy policy explaining data use.

---

## 2. Right of Access

- **What it means**  
  Data subjects can request a copy of all personal data an organisation holds about them.

- **Timeline**  
  Typically within **one month** (extendable to two for complex cases).

- **Product example**  
  A user requests “What data do you have on me?” and receives a structured export (JSON or PDF) of profile, logs, and third‑party integrations.

---

## 3. Right to Rectification

- **What it means**  
  Inaccurate or incomplete data must be corrected or updated.

- **Product example**  
  A user edits their address in the app, and the change propagates to billing, shipping, and support systems.

---

## 4. Right to Erasure (“Right to be Forgotten”)

- **What it means**  
  Data subjects can request deletion where:  
  - The data is no longer necessary.  
  - Consent is withdrawn and there is no other legal basis.  
  - They object to processing and no overriding grounds exist.  
  *(Subject to legal exceptions, e.g., tax, regulation.)*

- **Product example**  
  A user deletes their account; the system removes their data from active databases, logs, and third‑party vendors where reasonable.

---

## 5. Right to Restrict Processing

- **What it means**  
  Individuals can ask processing to be **paused** (e.g., while accuracy is checked) without deleting the data.

- **Product example**  
  A user disputes transaction data, and the system stops using that data for risk scoring until the dispute is resolved.

---

## 6. Right to Data Portability

- **What it means**  
  Under certain conditions, individuals can receive their data in a **structured, commonly used, machine‑readable format** and transfer it to another controller.

- **Product example**  
  A user exports order history as a CSV and uploads it to a competitor’s price‑comparison tool.

---

## 7. Right to Object

- **What it means**  
  Individuals can object to processing based on **legitimate interest, direct marketing, or profiling**.

- **Product example**  
  A user turns off “personalized ads,” and the system stops feeding that user into lookalike models and retargeting campaigns.

---

## 8. Right Not to Be Subject to Automated Decision‑Making

- **What it means**  
  Individuals must not be subject to **solely automated** decisions that have legal or significant effects (e.g., credit scoring, hiring, insurance) without human oversight.

- **Product example**  
  A loan‑approval engine flags a case as “rejected” but requires a human officer to review and confirm before finalizing.

---

## 9. Product Manager Checklist

- Every feature that collects data links to a **clear privacy notice**.  
- Systems support **full data exports**, **edit flows**, **real deletion paths**, **restriction states**, and **explicit opt‑out**.  
- High‑impact automated decisions include **human review and appeal paths**.

> **Next document:** [`06-lawful-bases-security.md`](06-lawful-bases-security.md) – lawful bases and security/compliance techniques.
