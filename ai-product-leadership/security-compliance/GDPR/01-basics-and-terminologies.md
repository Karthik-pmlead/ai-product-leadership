# GDPR 101 – Basics and Terminologies

This document introduces core GDPR concepts and key terms, with concise explanations and examples tailored for product, engineering, and AI‑leadership audiences.

---

## 1. Basic Terminologies

### Personal data
Any information that relates to an identified or identifiable living person (a “natural person”).  
This includes anything that can directly or indirectly single out an individual, online or offline.

**Example:**  
A customer’s name, email, phone number, IP address, or a customer‑ID that can be linked back to them.

---

### Data processing
Any operation performed on personal data, whether automated or manual.  
Covered operations include: collecting, storing, using, sharing, modifying, and deleting data.

**Example:**  
Logging a user’s email for a newsletter, storing it in a database, and later sending them marketing emails is “processing” at each step.

---

### Data Subject
The individual whose personal data is being collected or used.  
Under GDPR, most rights (e.g., access, deletion, objection) belong to this person.

**Example:**  
A user signing up for your SaaS product using their work email is the data subject for that account and contact information.

---

### Data Controller
The organization (or person) that decides **why** and **how** personal data is processed.  
Controllers bear primary accountability for GDPR compliance.

**Example:**  
An e‑commerce company that decides to collect customer names, addresses, and payment details for order fulfillment is the data controller for that data.

---

### Data Processor
An external party that processes personal data **on behalf of the controller**, following the controller’s instructions.  
They must also comply with GDPR but do not determine the purpose.

**Example:**  
A cloud hosting provider, payroll SaaS, or analytics vendor that stores or analyzes employee or customer data for your company is a data processor.

---

### Data Breach
A security incident involving accidental or unlawful access, loss, alteration, disclosure, or destruction of personal data.  
GDPR requires many breaches to be reported to the regulator and, in some cases, to affected individuals.

**Example:**  
An unencrypted laptop containing customer records is stolen, or an API logs user PII in plain text that becomes accessible to a broader team than intended.

---

### Pseudonymization
Replacing direct identifiers so individuals cannot be identified without additional information.  
This is a powerful privacy‑enhancing technique but is **reversible** with access to the “key.”

**Example:**  
Using a customer‑ID in the main system and storing names in a separate, locked dataset.

---

### Anonymization
Irreversibly altering data so individuals cannot be identified, even with additional information.  
True anonymization removes GDPR scope for that dataset.

**Example:**  
Reporting aggregate analytics such as “percentage of users in age‑band 25–34 in Bangalore” without any individual‑level identifiers.

---

## 2. Quick Cheat‑Sheet (for slides / docs)

| Term                    | 1‑line definition |
|-------------------------|-------------------|
| **Personal data**       | Any info that can identify or relate to an identifiable living person. |
| **Data processing**     | Any operation on personal data (collect, store, use, delete, etc.). |
| **Data Subject**        | The individual whose personal data is being processed. |
| **Data Controller**     | Organization that decides why and how personal data is processed. |
| **Data Processor**      | External party that processes data under the controller’s instructions. |
| **Data Breach**         | Security incident involving loss, access, or disclosure of personal data. |
| **Pseudonymization**    | Replacing direct identifiers so people cannot be identified without extra info. |
| **Anonymization**       | Irreversibly altering data so individuals cannot be identified. |

--- 

> **Next document:** [`02-gdpr-key-principles.md`](02-gdpr-key-principles.md) – deep dive into GDPR’s 7 core principles for product teams.
