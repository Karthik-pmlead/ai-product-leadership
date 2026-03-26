# GDPR 101 – Data Controller and Data Processor

This document clarifies the roles of data controller and data processor and their respective responsibilities.

---

## 1. What Is a Data Controller?

- **Definition**  
  The organisation that decides **why** and **how** personal data is processed. It bears primary accountability for GDPR compliance.

- **Key traits**  
  - Owns the **business purpose** (e.g., onboarding, marketing, risk scoring).  
  - Chooses **what data to collect**, **how long to keep it**, and **who can access it**.  
  - Responsible for **lawful bases**, **privacy notices**, **DPIAs**, **breach reporting**, and **data subject rights**.

- **Example**  
  An e‑commerce platform that stores customer orders, emails, and payment details for sales and fraud checks is the controller.

---

## 2. What Is a Data Processor?

- **Definition**  
  An organisation that processes personal data **on behalf of and according to the instructions of the controller**.

- **Key traits**  
  - Acts as a **service provider** (e.g., cloud, payroll SaaS, analytics, hosting).  
  - Must follow the controller’s documented instructions and cannot freely reuse data for its own purposes.  
  - Still must comply with GDPR (security, breach notification, sub‑processor rules).

- **Example**  
  A cloud provider storing customer data for a SaaS company, or a HR‑SaaS handling employee records, is a processor.

---

## 3. Controller vs Processor – Side‑by‑Side

| Aspect                    | Controller                                            | Processor                                                |
|---------------------------|-------------------------------------------------------|----------------------------------------------------------|
| **Decides “why”**         | Yes – business purpose.                               | No – follows controller’s instructions.                  |
| **Decides “how”**         | Designs overall architecture and data scope.          | Implements within those boundaries.                      |
| **Primary accountability**| Highest; ultimate responsibility.                    | Substantial but secondary to controller.                 |
| **DPIA**                  | Conducts or triggers DPIA for high‑risk processing.   | Supports controller with technical evidence.             |
| **Breach reporting**      | Reports to regulator and users.                       | Must notify the controller immediately.                  |
| **Sub‑processors**        | Cannot normally use sub‑processors.                   | May use them only with the controller’s consent.         |
| **Data subject rights**   | Directly handles access, deletion, etc.               | Enables those rights in systems and data models.         |

---

## 4. Why Product Managers Need to Know This

- **Vendor management**  
  Ensure every SaaS or cloud provider is treated as a **processor** (with a DPA) and that responsibilities are clear.

- **Architecture choices**  
  Decide early whether your product is the **controller** (e.g., owns the end‑user relationship) or a **processor** (e.g., an analytics layer embedded in others’ apps).

> **Next document:** [`05-data-subject-rights.md`](05-data-subject-rights.md) – the 8 key rights of data subjects under GDPR.
