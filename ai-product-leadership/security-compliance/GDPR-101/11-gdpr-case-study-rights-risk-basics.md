# GDPR Case Study – Part 2: Data Subject Rights, Risk Rating, and Compliance

Continuing the scenario of a fictional mobile app registration process, this section explores data subject rights, project‑risk level, and GDPR’s role for a business like XYZ Company.

---

## Q4: Evaluate data subjects’ rights in the mobile app project

**Question:**  
Evaluate the data subjects’ rights that may be relevant to this mobile application project. Identify specific rights that users may exercise regarding their personal data and explain how the organization can ensure compliance with these rights.

**Answer:**  

Relevant data subject rights for users in this mobile application project include:

- **Right of access**  
  Users have the right to request a copy of the personal data the organisation holds about them (e.g., profile, registration details, activity logs) and information on how it is processed.

- **Right to rectification**  
  Users may request that inaccurate or incomplete data (e.g., wrong email or birthday) be corrected.

- **Right to erasure (“right to be forgotten”)**  
  Under certain conditions, users may request deletion of their data, for example when it is no longer necessary for the purpose or if consent is withdrawn (subject to legal exceptions, such as tax or regulatory retention).

- **Right to object and restrict processing (bonus relevance for social apps)**  
  Users may object to certain types of processing such as profiling or marketing, or request that processing is temporarily restricted while disputes (e.g., data‑accuracy claims) are resolved.

**How the organisation can ensure compliance:**

- Implement clear **in‑app or web‑based forms** so users can easily submit requests for access, correction, or deletion.  
- Design **back‑end workflows** that allow customer‑support or automated systems to locate, verify, and process each request within the typical **one‑month** timeframe.  
- Maintain **accurate and up‑to‑date data models** so that rectification and deletion are applied consistently across all relevant systems (e.g., app backend, analytics, CRM).  
- Introduce **secure data‑storage and retention practices**, including auto‑deletion or archival rules, so erasure requests can be executed reliably.  

These steps reflect GDPR’s focus on **accountability** and **transparency**: users’ rights are not just mentioned in a policy, but built into product and operational flows.

---

## Q5: Risk rating for the project

**Question:**  
Evaluate the risk of the project and provide an explanation for why you choose that risk level (Low / Medium / High / Very High).

**Answer:**  

This project can be rated as **Medium risk**.

**Reasons:**  

1. **Privacy concerns**  
   The app collects **direct identifiers** such as full names, dates of birth, and email addresses. If not adequately protected, this information could be exposed to unauthorized access, profiling, or misuse, which has a moderate impact on individuals’ privacy and trust.

2. **Data security**  
   The mobile app handles personal data that must be protected against breaches, weak authentication, or insecure APIs. If data‑security measures are inadequate, users’ sensitive information could be compromised. However, the risk is **moderate rather than very high** because the data does not typically include highly sensitive categories (e.g., health, biometrics, or financial data) and processing is for straightforward account‑management and socialisation.

3. **Compliance obligations under GDPR**  
   The organisation must comply with GDPR requirements such as lawful bases, purpose limitation, data‑minimisation, security, and data‑subject rights. Failure to comply can lead to **regulatory scrutiny and potential fines**, but the risk level is **moderate** because the processing is limited to necessary account‑management and social features, not large‑scale automated decision‑making or high‑risk profiling.

Overall, **Medium risk** reflects that the project involves **real, but not extreme, privacy and security impact** on individuals, with a clear path to mitigation through standard GDPR‑aligned controls and product‑design choices.

---

## Q6: Purpose and significance of GDPR for XYZ Company

**Question:**  
Explain the purpose of the General Data Protection Regulation (GDPR) and its significance for businesses like XYZ Company that handle personal data.

**Answer:**  

The GDPR aims to **protect the fundamental rights and freedoms of individuals**, especially their **right to privacy and data protection**, by regulating how organisations collect, store, use, and share personal data. It gives individuals more control over their data while creating a **harmonised regulatory framework** across the EU and EEA.

For businesses like **XYZ Company** (handling personal data through mobile apps, web services, or other digital products), GDPR is significant because:

- It sets clear rules on **lawfulness, transparency, and fairness** in data processing.  
- It requires organisations to implement **appropriate technical and organisational measures** to secure personal data.  
- It gives individuals **strong data‑subject rights**, such as access, rectification, and erasure, which directly affect how products are designed and operated.  
- It allows regulators to impose **substantial fines** for serious or repeated violations, which can affect reputation and bottom line.

Compliance with GDPR is therefore **strategic, not just legal**: it builds trust with users, supports market access (particularly in the EU), and encourages privacy‑by‑design approaches that benefit product quality and security.

---

## Q7: Two data subject rights and compliance for XYZ Company

**Question:**  
Identify two data subject rights under the GDPR and explain how XYZ Company can ensure compliance with these rights.

**Answer:**  

Two key data subject rights under the GDPR are:

1. **Right to access**  
   Individuals can request a copy of their personal data and information about how it is processed (e.g., purposes, legal basis, recipients, retention periods).

2. **Right to erasure**  
   Under certain conditions (e.g., data is no longer necessary, consent is withdrawn, or the individual objects and there are no overriding grounds), individuals can request that their data be deleted.

**How XYZ Company can ensure compliance:**

- For **right to access**, XYZ Company can:  
  - Provide a **self‑service data‑request portal** or in‑app flow where users can request and download their data.  
  - Implement backend systems that can quickly locate and deliver data in a **structured, commonly used format** (e.g., JSON or CSV) within the standard **one‑month** deadline.

- For **right to erasure**, XYZ Company can:  
  - Implement a **real account‑deletion path** that removes user data from core databases, analytics, and third‑party services where practical.  
  - Maintain documented **retention policies** and exceptions (e.g., where law requires data to be kept), so erasure is applied consistently and defensibly.

These measures demonstrate **accountability** and respect for users’ privacy, which are core GDPR expectations.

---

## Q8: Measures to enhance data protection practices

**Question:**  
Describe two measures that XYZ Company can implement to enhance its data protection practices and ensure compliance with the GDPR.

**Answer:**  

Two practical measures XYZ Company can implement are:

1. **Encryption of personal data and regular data backups**  
   - Encrypt personal data **at rest** (e.g., in databases and backups) and **in transit** (e.g., via HTTPS/TLS).  
   - Perform **regular, secure backups** and test recovery procedures to prevent data loss due to accidents, ransomware, or system failures.  
   This supports GDPR’s requirement for **integrity and confidentiality** of personal data.

2. **Staff training and clear data‑handling policies**  
   - Provide **regular training** for product, engineering, support, and sales teams on GDPR basics, data‑subject rights, and incident‑response procedures.  
   - Establish **clear internal policies and procedures** that define how personal data can be collected, stored, shared, and deleted, including decision‑making around lawful bases, consent, and DPIAs.  
   This reinforces the **accountability** principle by ensuring that GDPR is embedded into daily operations, not treated as a one‑time project.

---

## Q9: Lawful basis for processing personal data

**Question:**  
Explain the concept of lawful basis for processing personal data under the GDPR. Provide two examples of lawful bases that XYZ Company can rely upon for processing customer data.

**Answer:**  

Under GDPR, **lawful basis** means there must be a valid legal justification for processing personal data. Processing is **illegal** unless at least one of six lawful bases under **Article 6** applies (e.g., consent, contract, legal obligation, vital interests, public task, or legitimate interests).

For XYZ Company, two relevant examples are:

1. **Necessity for the performance of a contract**  
   Processing customer data (e.g., name, email, delivery address) may be necessary to **fulfil an order**, manage an account, or provide core app functionality. This is a strong basis for core business‑driven processing.

2. **Compliance with a legal obligation**  
   In some cases, XYZ Company may process data to comply with **legal or regulatory requirements**, such as keeping records for tax or financial‑crime‑related obligations. This basis applies only when the law explicitly requires such processing.

Choosing the correct lawful basis is a **product‑level decision**, not just a legal footnote; it should be documented and reflected in privacy notices and user experiences.

---

## Learning Outcome

Through this continuation of the case study, learners practice:
- Evaluating **data subject rights** in a product‑context (access, rectification, erasure).  
- Reasoning about **risk levels** for data‑processing projects.  
- Connecting **GDPR’s purpose** to business‑strategy and compliance.  
- Translating **lawful bases** and **data‑protection measures** into concrete product and organisational actions.
