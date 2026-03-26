# Information Security Policy

This policy defines the **overall security expectations** for systems, data, networks, and software across our organisation. It is aligned with **ISO‑2701‑style principles** and with **OWASP‑Top‑10** expectations for web and API‑based products.

---

## 1. Scope

This policy applies to:
- All **production, staging, and development environments** that host or process organisational or user data.  
- All **employees, contractors, and third‑parties** who access, build, or operate these environments.

---

## 2. Core security principles

- **Confidentiality**  
  - Protect data from unauthorised access.  
  - Apply least‑privilege access‑control and encryption where appropriate.

- **Integrity**  
  - Ensure data and systems are not tampered with.  
  - Use hashing, digital signatures, and version‑control to protect code and configuration.

- **Availability**  
  - Ensure critical systems remain available to authorised users.  
  - Use redundancy, monitoring, and incident‑response processes to minimise downtime.

- **Accountability**  
  - Log and audit key actions (login, privilege‑change, sensitive data‑access).  
  - Ensure logs are retained for the required period and are tamper‑resistant.

---

## 3. Protected assets

The following are considered **protected assets** and must be secured accordingly:

- User personal data (as defined in the Data Protection Policy).  
- Product‑source‑code and configuration.  
- Customer‑configurable data and settings.  
- Administrative‑credentials and secrets.

---

## 4. General security expectations

- **Access control**  
  - All access to systems and data must be authenticated and explicitly authorised.  
  - Strong passwords and MFA are required for admin and privileged‑access accounts.

- **Network and infrastructure security**  
  - Use firewalls, segmentation, and network‑monitoring tools to protect environments.  
  - Follow the organisation’s network‑segmentation policy to isolate sensitive systems.

- **Patch and vulnerability management**  
  - All operating‑systems, libraries, and applications must be kept up‑to‑date.  
  - Vulnerabilities classified as “high” or “critical” must be remediated within defined SLAs.

- **Incident response**  
  - Any security‑incident must be reported immediately to the security‑team.  
  - Follow the incident‑response playbook (e.g., in `security-compliance/incident-response/`) to contain, analyse, and remediate.

---

## 5. Roles and responsibilities

- **Product‑leaders**  
  - Ensure security‑expectations are baked into product‑requirements and SDLC.  
  - Treat security‑debt as first‑class technical‑debt in roadmap planning.

- **Engineering teams**  
  - Follow secure‑coding‑guidelines and OWASP‑Top‑10‑aligned practices.  
  - Avoid hardcoding secrets and enforce scanning of dependencies.

- **Security / Compliance leads**  
  - Monitor security‑metrics and run periodic audits and assessments.  
  - Coordinate with legal and management on high‑risk‑incidents and regulatory‑requests.
