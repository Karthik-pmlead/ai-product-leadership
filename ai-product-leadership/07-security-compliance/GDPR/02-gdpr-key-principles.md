# GDPR 101 – Key Principles

This document explains GDPR’s 7 core principles (Article 5) in language suited for product managers, engineers, and AI‑product leaders.

---

## 1. Lawfulness, Fairness, and Transparency

Personal data must be processed **lawfully**, **fairly**, and in a **transparent** way toward the data subject.

- **What it means**  
  You must have a valid legal basis for processing (e.g., consent, contract, legitimate interest) and clearly explain purposes in the privacy notice.

- **Product example**  
  A SaaS product collects emails and IP addresses for onboarding and analytics. The privacy notice lists these purposes and obtains explicit consent for marketing.

---

## 2. Purpose Limitation

Data must be collected for **specified, explicit, and legitimate purposes** and not further processed in an incompatible way.

- **What it means**  
  You cannot reuse data for unrelated purposes without re‑evaluating the legal basis and updating transparency.

- **Product example**  
  A bank collects KYC data for account‑opening and AML checks. It should not use that same data for unrelated marketing campaigns without a separate legal basis and notice.

---

## 3. Data Minimisation

Personal data must be **adequate, relevant, and limited** to what is necessary for the purpose.

- **What it means**  
  Avoid “collect‑everything‑just‑in‑case.” Only keep fields strictly needed for the use case.

- **Product example**  
  A job‑board collects skills, experience, and contact info, but not medical history or family details, unless explicitly justified.

---

## 4. Accuracy

Personal data must be **accurate and, where necessary, kept up to date**.

- **What it means**  
  Implement processes to correct or delete inaccurate or incomplete data.

- **Product example**  
  A CRM flags phone numbers that repeatedly fail to connect and prompts users to update or verify them.

---

## 5. Storage Limitation

Data should not be kept **longer than necessary** for the stated purpose.

- **What it means**  
  Define and enforce retention periods (e.g., auto‑deletion, archival) for each data type.

- **Product example**  
  Interview‑recording videos are auto‑deleted after 30 days unless local law requires longer retention.

---

## 6. Integrity and Confidentiality (Security)

Data must be processed to ensure **appropriate security** against unauthorized access, loss, alteration, or damage.

- **What it means**  
  Use technical and organisational measures (encryption, access controls, logging, audits).

- **Product example**  
  A fintech encrypts customer bank‑account data at rest and in transit and restricts access to a small set of roles.

---

## 7. Accountability

The data controller must **demonstrate compliance** with all 6 principles above.

- **What it means**  
  Keep Records of Processing Activities (RoPA), document lawful bases, and maintain governance and training.

- **Product example**  
  A company maintains a RoPA, signs data‑processing agreements with vendors, and runs periodic GDPR‑compliance audits.

---

## 2. Cheat‑Sheet for Product Managers

| Principle                             | 1‑line definition |
|---------------------------------------|-------------------|
| **Lawfulness, fairness, transparency** | Data is processed legally and transparently, with clear purpose and notice. |
| **Purpose limitation**                | Data is collected only for specific, explicit, and legitimate purposes. |
| **Data minimisation**                 | Only the minimum necessary data is collected for the purpose. |
| **Accuracy**                          | Data is accurate and kept up to date. |
| **Storage limitation**                | Data is kept only as long as necessary. |
| **Integrity & confidentiality**       | Data is protected with appropriate security measures. |
| **Accountability**                    | The controller can prove it follows all other principles. |

---

> **Next document:** [`03-privacy-by-design.md`](03-privacy-by-design.md) – how to bake GDPR into product design and defaults.
