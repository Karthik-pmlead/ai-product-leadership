# Secure Coding Guidelines – Development Team Handbook

This document defines **secure coding guidelines** for product‑development teams (web, API, mobile, and IoT‑style code) aligned with **OWASP Top 10**, **ISO‑27001‑style security**, and **product‑safety thinking**. These rules are meant to be folded into coding standards, PR checklists, and engineering onboarding, not treated as a one‑off compliance exercise.

---

## 1. Core principles

Before diving into language‑specific rules, all engineers are expected to follow these principles:

- **Defensive default**: Treat all input as untrusted and assume failures will happen.  
- **Least privilege**: Services, APIs, and components should only have the permissions they strictly need.  
- **Fail‑safe default**: If security‑related logic fails, the system should default to a safe, restricted state.  
- **Log for security**: Treat logs as part of security‑monitoring; they must record user‑identifying actions, errors, and auth‑events without exposing secrets.  

These principles underpin every rule in the guidelines below.

---

## 2. Input validation and sanitization

Input‑related bugs are the root cause of injection, XSS, and many logic flaws. Treat **all input** (HTTP, API, CLI, files, environment variables) as untrusted.

### Do:

- **Enforce strict schema validation**  
  - Use JSON‑schema or typed contracts for APIs; reject malformed or extra fields.  
- **Validate at the perimeter**  
  - Enforce type, length, format, and allowed‑values (e.g., regex, enums) at API entrypoints.  
- **Escaping and encoding**  
  - HTML‑encode output going to the browser.  
  - Use parameterized queries or prepared statements for SQL; no string‑based concatenation of user‑input.  
- **Use allow‑lists, not block‑lists**  
  - Specify exactly what is allowed (e.g., allowed characters, allowed host‑names) rather than trying to filter “bad” patterns.

### Do not:

- Trust client‑side validation alone.  
- Concatenate user‑input into SQL, OS‑commands, or templates without strict escaping.

---

## 3. Authentication and session management

These rules apply to login, tokens, MFA, password‑handling, and sessions.

### Do:

- **Enforce strong passwords**  
  - Minimum length, complexity requirements, and disallow common or breached‑passwords.  
- **Use standard libraries**  
  - Prefer battle‑tested libraries for password‑hashing (e.g., bcrypt, scrypt, Argon2) and avoid home‑rolled crypto.  
- **Secure session handling**  
  - Use short‑lived session tokens; rotate tokens on login and privilege‑changes.  
  - Bind tokens to IP/user‑agent fingerprint if appropriate; invalidate sessions on logout.  
- **Implement MFA where applicable**  
  - Especially for admin, super‑user, or sensitive‑action endpoints.

### Do not:

- Store passwords in plaintext or weak hashes (e.g., MD5, SHA‑1).  
- Transmit credentials or tokens over non‑HTTPS.  
- Allow long‑lived “remember‑me” tokens without explicit expiry and revocation.

---

## 4. Access control and authorization

Access‑control flaws are among the top‑risk categories in OWASP Top 10.

### Do:

- **Use role‑based (or attribute‑based) access control**  
  - Define roles, permissions, and resource‑bindings clearly; enforce them in code, not just in UI.  
- **Enforce checks on every request**  
  - For each API endpoint, explicitly check:
    - Is the user authenticated?  
    - Does the user have permission for that resource and action?  
  - Avoid “decorator‑only” or “middleware‑only” checks that can be bypassed.  
- **Validate user‑ownership**  
  - For `GET /users/:id`, `PUT /users/:id`, ensure the caller is only modifying their own resource or has explicit higher‑level permission.  
- **Log and alert on privilege‑escalation attempts**  
  - Flag suspicious role‑change or permission‑override actions.

### Do not:

- Rely on UI‑only hiding of features; enforce server‑side checks.  
- Use “magic” admin‑flags or backdoor‑accounts in production.

---

## 5. Cryptography and secrets handling

Poor crypto and secrets‑management are common sources of data‑breaches.

### Do:

- **Use standard, vetted algorithms**  
  - For symmetric encryption: AES‑256; for hashing: SHA‑256 or SHA‑3; for signatures: EdDSA or RSA‑with‑PKCS#1 v2.  
- **Store secrets securely**  
  - Use secrets‑management tools (e.g., Hashicorp Vault, AWS Secrets Manager, Azure Key Vault).  
  - Never hardcode secrets in source code or config files in Git.  
- **Protect at rest and in transit**  
  - Encrypt sensitive data at rest (databases, logs, backups) and in transit (TLS‑1.2+).  
  - Use mutual‑TLS for service‑to‑service communication where feasible.

### Do not:

- Invent your own crypto algorithms or protocols.  
- Commit `.env`, `config-secret`, or similar files to version control.  
- Use default or weak cipher suites in production.

---

## 6. Logging, monitoring, and error handling

Logs are critical for security response; but they must not leak sensitive data.

### Do:

- **Log security‑relevant events**  
  - Login attempts (success/failure), password‑changes, MFA‑changes, privilege‑changes, and admin‑actions.  
- **Avoid logging sensitive data**  
  - Do not log passwords, tokens, PII, or full request payloads. Use masking or hashing when absolutely necessary.  
- **Use structured logging**  
  - Ensure logs are machine‑readable so they can be ingested by SIEM or alerting tools.  
- **Fail gracefully and without information leakage**  
  - Return generic error messages to users (e.g., “Invalid credentials”), not detailed stack‑trace or DB‑errors.

### Do not:

- Expose stack traces or SQL‑errors to end users.  
- Log raw tokens or credentials, even “temporarily”.

---

## 7. API and microservices security

Modern products are built on APIs and microservices; treat them as first‑class security assets.

### Do:

- **Enforce API‑level authentication and rate‑limiting**  
  - Use tokens, API keys, or OAuth‑style flows; enforce rate‑limits per‑user/IP to prevent abuse.  
- **Validate and sanitize all inputs**  
  - Treat API payloads like any other input; enforce schema and clean output.  
- **Use versioned APIs with clear deprecation**  
  - Avoid leaving old, insecure versions of endpoints exposed indefinitely.  
- **Implement service‑to‑service authentication**  
  - Use mTLS or service‑mesh‑style identity; ensure each service has a minimal‑permission identity.

### Do not:

- Expose internal APIs or admin endpoints without authentication.  
- Allow overly‑permissive CORS policies (e.g., `Access-Control-Allow-Origin: *` on sensitive endpoints).

---

## 8. Third‑party dependencies and supply chain

Using vulnerable libraries is a major OWASP‑Top‑10 category.

### Do:

- **Maintain a bill‑of‑materials (SBOM)**  
  - Track all direct and transitive dependencies for your services.  
- **Enforce dependency‑scanning**  
  - Use tools that scan for known‑vulnerabilities (e.g., SCA tools) and integrate them into CI/CD.  
- **Patch or replace vulnerable components**  
  - Prioritise critical‑ and high‑risk vulnerabilities; have a clear patching‑and‑upgrade policy.  
- **Minimise dependencies**  
  - Avoid “megabundles”; prefer small, well‑maintained libraries.

### Do not:

- Use dependencies from unknown or untrusted sources.  
- Ignore “dev‑only” or “test‑only” dependencies that end up in production.

---

## 9. Code reviews and security checks

Secure coding should be part of the normal development workflow.

### Do:

- **Add security checks to PR templates**  
  - For each PR touching auth, API, or user‑input, explicitly verify:
    - Input validation and escaping.  
    - Access control checks.  
    - Secrets handling.  
- **Use static‑analysis and SAST tools**  
  - Integrate tools that flag common vulnerabilities (e.g., hardcoded secrets, weak crypto, insecure‑deserialization) into CI.  
- **Run periodic security‑focused reviews**  
  - Quarterly or per‑release, perform a “security‑sweep” on high‑risk components.

### Do not:

- Allow “security‑only” audits to be entirely separate from regular development.  
- Merge high‑risk security‑debt without explicit ownership and a remediation plan.

---

## 10. Product‑level secure‑coding culture

As a product leader, you can reinforce these rules by:

- **Embedding security‑guidelines into PRDs**  
  - For features that touch auth, payments, or PII, explicitly call out required secure‑coding rules (e.g., “Must follow OWASP‑A01, A03, A07”).  
- **Running threat‑modeling workshops**  
  - Use OWASP‑Top‑10‑style categories to identify and document risks for each product area.  
- **Measuring and improving**  
  - Track metrics like:
    - % of critical vulnerabilities fixed in the last 90 days.  
    - Time‑to‑patch for high‑risk libraries.  
    - # of security‑related PR comments per sprint.

By treating **secure coding** as a continuous, cross‑functional practice—not a one‑time checklist—you can systematically reduce the attack‑surface of your web, API, and IoT‑based products.
