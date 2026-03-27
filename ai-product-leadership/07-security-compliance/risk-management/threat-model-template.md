# Threat‑Model Template – For Product Teams

Use this template in design‑reviews for any feature that touches:
- Authentication, PII, payments,  
- Admin‑functions, IoT‑or‑safety‑related behaviour, or  
- New external APIs or integrations.

---

## 1. Step 1 – Define the scope

- **System / feature name**  
- **Description** (1–2 lines):  
- **Boundaries** (what is in scope, what is not):  

---

## 2. Step 2 – Identify assets and trust boundaries

| Asset                  | Description |
|------------------------|-----------|
| User PII               | e.g., name, email, phone |
| Payment data           | e.g., tokenised card‑ID, not PAN |
| API endpoints          | e.g., `/users`, `/payments` |
| Admin dashboard        | e.g., internal‑tool‑for‑support |

**Trust boundaries**  
- External‑users vs authenticated‑users.  
- Frontend vs backend.  
- Your service vs 3rd‑party APIs.

---

## 3. Step 3 – List threats (use OWASP‑style categories)

Use the OWASP‑Top‑10‑style categories as a checklist:

- **A01: Broken Access Control**  
  - Can a user access someone else’s data or functions?

- **A02: Cryptographic Failures**  
  - Are tokens, passwords, or secrets stored or transported securely?

- **A03: Injection**  
  - Is any user‑input used in SQL/commands/templates without escaping?

- **A04: Insecure Design**  
  - Is there no clear safe‑default‑state for failure‑modes?

- **A05: Security Misconfiguration**  
  - Are default credentials, verbose errors, or exposed admin‑panels present?

- **A06: Vulnerable and Outdated Components**  
  - Are dependencies up‑to‑date?

- **A07: Identification and Authentication Failures**  
  - Are logins and MFA weak?

- **A08: Software and Data Integrity Failures**  
  - Can deserialisation or untrusted code‑sources be exploited?

- **A09: Security Logging and Monitoring Failures**  
  - Are critical‑events logged and monitored?

- **A10: SSRF**  
  - Can server‑side APIs be tricked into internal‑or‑external‑requests?

For each threat you identify, add a short line in Step‑4.

---

## 4. Step 4 – Map threats to risks and controls

For each threat raised in Step‑3:

- **Threat description**  
- **Attack vector** (how an attacker would exploit it)  
- **Likelihood / Impact** (qualitative or 1–5)  
- **Existing controls** (what already mitigates it)  
- **Gaps** (what is missing)  
- **Required controls** (what must be added)  
- **Owner and deadline**  

Repeat this for each significant threat until you have a short list of “must‑fix” items.

---

## 5. Step 5 – Output to backlog

- Convert each “must‑fix” item into a **ticket or backlog item**.  
- Link this threat‑model file to the related PRD or JIRA‑epic.  
- Revisit the threat‑model at major design‑changes or redesigns.
