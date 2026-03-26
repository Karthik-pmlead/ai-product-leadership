# GDPR Case Study: A Mobile App Registration Process

A fictional company is launching a mobile app that allows users to register and use social features. In this case study, learners apply core GDPR concepts to a realistic product scenario.

---

## Scenario

A mobile‑first social‑networking app lets users register with the following information:
- Full name  
- Date of birth  
- Email address  

The app aims to provide profile‑based social interactions, friend discovery, and targeted content based on user interests.

---

## Q1: Identify and explain the key personal data elements

**Question:**  
Identify the key personal data elements involved in the registration process for the mobile application. Based on GDPR, explain why these data elements are considered personal data and require protection.

**Answer:**  
The key personal data elements collected during registration are:
- **Full name**  
- **Date of birth**  
- **Email address**

Under GDPR, **personal data** means any information relating to an identified or identifiable natural person. These fields are considered personal data because:

- A **full name** directly identifies an individual.  
- A **date of birth**, especially when combined with a name or email, significantly increases the chance of uniquely identifying someone.  
- An **email address** can be used to contact and distinguish one person from another, especially inside a service.

Because these data elements relate to identifiable individuals, they trigger GDPR protections such as **lawfulness, fairness, transparency, and purpose limitation**. The organisation must ensure that collecting and processing these fields is justified, limited to what is necessary, and protected appropriately.

---

## Q2: Assess the legal basis for processing

**Question:**  
Assess the legal basis for processing personal data in this mobile application project. Determine the most appropriate legal basis for collecting and processing users’ personal data and provide a justification for your choice.

**Answer:**  
The most appropriate legal basis for processing this data is **“performance of a contract” (Article 6(1)(b) GDPR)**.

**Justification:**  
By registering for the app, the user enters into a **contractual relationship** with the organisation to use its core features (e.g., profile creation, social interactions, content access). In this context:

- The user’s **full name** and **email address** are necessary to create and manage the account, authenticate sessions, and communicate with the user.  
- The **date of birth** may be used for age‑or‑eligibility checks or age‑appropriate content, if clearly stated as a purpose.

Other legal bases, such as **consent**, may be more appropriate for **optional** uses (e.g., marketing, advanced profiling) where the user must freely agree without blocking core functionality. For the **essential registration and account‑management steps**, contract is the stronger, more proportionate basis.

---

## Q3: Identify risks and GDPR‑aligned mitigations

**Question:**  
Analyze the potential risks to individuals’ privacy and data protection arising from the collection and processing of personal data in the mobile application. Identify at least three risks and explain how they can be mitigated under GDPR.

**Answer:**  
Three key risks to privacy and data protection in this mobile app are:

### 1. Unauthorized access or data breaches  
If the app’s backend or API is compromised, attackers could access users’ **names, email addresses, and date of birth**, leading to identity theft, phishing, or account takeover.

**GDPR‑aligned mitigations:**  
- Implement **encryption** for data at rest and in transit.  
- Enforce **strong authentication** (e.g., secure tokens, multi‑factor where appropriate).  
- Adopt **access controls and role‑based permissions** so that only necessary staff can view or use personal data.  
These measures support the GDPR principle of **integrity and confidentiality**.

### 2. Inadequate data security and oversight  
Weak security practices, such as logging PII in plain text, improper backups, or missing incident‑response procedures, can expose data over time and increase the risk of undetected breaches.

**GDPR‑aligned mitigations:**  
- Conduct **regular security audits and vulnerability assessments**.  
- Maintain **logging and monitoring** with clear incident‑response playbooks.  
- Carry out **Data Protection Impact Assessments (DPIAs)** for high‑risk processing, such as profiling or large‑scale data‑handling.  
This reflects the **accountability** principle: being able to demonstrate appropriate security and governance.

### 3. Potential misuse of personal data  
If personal data is used beyond the stated purposes (e.g., undisclosed sharing with advertisers, or secondary profiling without clear lawful basis), users’ rights and trust are undermined.

**GDPR‑aligned mitigations:**  
- Define and document **clear, specific purposes** for each data field (e.g., “use email for authentication and service‑related communication only”).  
- Ensure **purpose limitation** and **data minimisation** by not collecting or reusing data that is not strictly necessary.  
- Provide **transparent privacy notices** and obtain **explicit consent** for non‑core uses (e.g., personalized ads, analytics).  
- Implement **proper retention and deletion mechanisms** so data is not kept longer than needed.  
These actions align with GDPR principles such as **lawfulness, fairness, transparency, purpose limitation, and data minimisation**.

---

## Learning Outcome

Through this case study, learners practice:
- Identifying **personal data** in a real‑looking product context.  
- Choosing a **GDPR‑compliant legal basis** (contract vs consent) aligned with user expectations.  
- Mapping **real‑world risks** to **GDPR‑style mitigations** that reflect core principles (lawfulness, fairness, transparency, security, and accountability).
