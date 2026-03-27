# Secure Development Policy

This policy defines how **security and compliance** are integrated into the **software development lifecycle (SDLC)** and product‑design process. It aligns with **OWASP‑Top‑10‑style thinking**, **GDPR‑privacy‑by‑design**, and **ISO‑27001‑style controls**.

---

## 1. Scope

This policy applies to:
- All **product‑development teams** (web, mobile, API, IoT, embedded‑software).  
- All **stages** of the SDLC: idea, design, implementation, testing, deployment, and maintenance.

---

## 2. Security‑by‑design expectations

- **Threat‑model early**  
  - For each significant feature or system, product‑leaders and architects must perform a lightweight threat‑model.  
  - Use OWASP‑Top‑10‑style categories (e.g., Broken Access Control, Injection, SSRF) as a checklist.

- **Secure‑requirements in PRDs**  
  - Each PRD that touches:
    - Authentication, authorisation, or PII,  
    - Payment‑processing or credentials,  
    - IoT‑or‑safety‑related functions,  
    must explicitly state:
    - Required security‑and‑privacy‑controls.  
    - Logging and monitoring‑requirements.  
    - Data‑retention‑and‑deletion‑logic.

- **Privacy‑by‑design and‑by‑default**  
  - Minimise data collection and retention.  
  - Design user‑consent‑flows and data‑deletion‑flows as first‑class features, not afterthoughts.

---

## 3. Development‑time security practices

- **Input validation and escaping**  
  - Treat all input as untrusted and enforce strict schema‑validation and type‑checking.  
  - Use parameterized‑queries or prepared‑statements for all database‑interaction.

- **Authentication and session management**  
  - Use standard libraries for password‑hashing (e.g., bcrypt, scrypt).  
  - Implement short‑lived tokens and enforce MFA for admin‑roles.

- **Cryptography and secrets**  
  - Avoid custom crypto; use well‑known algorithms and libraries.  
  - Never hardcode secrets in source‑code; use secrets‑management tools (e.g., Vault, Secrets Manager).

---

## 4. Testing and verification gates

- **Static‑analysis and SAST**  
  - All code must pass SAST checks in CI/CD (e.g., hardcoded‑secrets, known‑vulnerability‑patterns).  
- **OWASP‑Top‑10‑aligned manual / VAPT testing**  
  - High‑risk features (auth, payments, admin‑functions) must undergo:
    - Code‑review checks for security‑anti‑patterns.  
    - Penetration‑testing or VAPT as per product‑risk‑level.  
- **Dependency‑scanning**  
  - All third‑party libraries must be scanned for known‑vulnerabilities and kept up‑to‑date.

---

## 5. Roles and responsibilities

- **Product‑leaders**  
  - Ensure security‑and‑privacy‑requirements are part of the product‑definition.  
  - Prioritise security‑debt and remediation‑tickets alongside feature‑work.

- **Engineering teams**  
  - Follow secure‑coding‑guidelines and security‑playbooks for the product.  
  - Fix security‑issues with the same rigor as functional‑bugs.

- **Security / Compliance leads**  
  - Define and maintain secure‑development‑policy and secure‑coding‑guidelines.  
  - Provide training and hands‑on support to product‑teams on threat‑modeling and secure‑design.
