# Access Control Policy

This policy defines how **access to systems, data, and administrative functions** is granted, managed, and reviewed. It is aligned with **least‑privilege, role‑based‑access‑control, and accountability** principles used in ISO‑27001 and similar frameworks.

---

## 1. Scope

This policy applies to:
- All **production and pre‑production systems** that store or process sensitive data or perform critical functions.  
- All **users, service‑accounts, and third‑party integrations** that require access.

---

## 2. Core principles

- **Least privilege**  
  - Users and services must have only the permissions necessary to perform their job functions.  
  - Broader‑privilege roles (e.g., “super‑admin”) must be justified and tightly controlled.

- **Role‑based access control (RBAC)**  
  - Define roles at a product‑or‑system‑level (e.g., “Reader”, “Writer”, “Admin”).  
  - Assign users to roles rather than granting ad‑hoc permissions on individual objects.

- **Need‑to‑know**  
  - Access to sensitive data (e.g., raw PII, admin‑APIs) must be justified by a clear business‑need.  
  - Avoid “all‑seeing” dashboards or admin‑UIs by default.

- **Separation of duties**  
  - Separate critical functions (e.g., development, deployment, and production‑operation) where appropriate.  
  - Prevent a single individual from having unchecked control over both code and production‑changes.

---

## 3. User‑access lifecycle

- **Onboarding**  
  - New users are granted access based on a documented role within the product‑organisation.  
  - Prefer group‑based or SSO‑based entitlements rather than per‑user‑manual‑grants.

- **Changes**  
  - Any change in role or responsibilities triggers a review of access‑rights.  
  - Access‑reviews are performed at least quarterly (or more often for high‑risk‑roles).

- **Offboarding**  
  - Access for departing users must be revoked immediately upon exit.  
  - Automated deprovisioning workflows are preferred over manual‑removal.

---

## 4. Privileged and admin access

- **Principle of temporary admin access**  
  - Use just‑in‑time (JIT) or time‑boxed admin‑access where possible.  
  - Prefer structured approvals (e.g., PR‑approvals for infra‑changes, ticket‑approvals for admin‑actions).

- **Monitoring and logging**  
  - All admin‑actions must be logged with:
    - User‑identity.  
    - Timestamp.  
    - Command / API‑call context (where feasible).  
  - Logs must be retained for the required audit period and are tamper‑resistant.

---

## 5. Third‑party and service‑account access

- **Third‑party integrations**  
  - Third‑party tools must be evaluated for security‑and‑compliance.  
  - Access‑grants (e.g., OAuth scopes, API keys) must be scoped to the minimum required.

- **Service accounts**  
  - Avoid “personal” service‑account keys; prefer short‑lived tokens or managed‑identities.  
  - Rotate credentials regularly and revoke them when no longer needed.
