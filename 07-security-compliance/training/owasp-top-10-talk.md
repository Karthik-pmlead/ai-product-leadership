# OWASP Top 10 – Engineer Lightning Talk

This outline is for a **10–15 minute lightning talk** for web and API‑engineers, running through OWASP‑Top‑10 in a product‑relevant way.

---

## 1. Why OWASP matters for product

- OWASP‑Top‑10 are **the 10 most critical security risks for web and API‑applications**.  
- For product‑teams, OWASP is a **checklist** to bake security into:
  - PRDs,  
  - Design‑reviews,  
  - Code‑reviews,  
  - Testing and VAPT.

---

## 2. Quick tour of OWASP‑Top‑10 (2021)

Call out the top‑level name and a 1‑sentence example:

- **A01: Broken Access Control**  
  - “Can a user access someone else’s data or admin‑functions?”  
- **A03: Injection**  
  - “Are SQL/commands built via unsafe‑string‑concatenation?”  
- **A07: Identification and Authentication Failures**  
  - “Are logins and MFA weak?”  
- **A10: SSRF**  
  - “Can server‑side‑code be tricked into internal‑requests?”  

Pick 3–4 categories that are most relevant to your stack and explain them in more detail.

---

## 3. How to use OWASP in your daily workflow

- **In PRDs**  
  - Tag each feature with relevant OWASP‑categories (e.g., “A01, A07”).  

- **In design‑reviews**  
  - Ask:
    - “Where is access‑control checked?”  
    - “Where is user‑input used in SQL/commands?”  

- **In PRs**  
  - Use a **security‑checklist**:
    - “Is this endpoint authenticated and authorised?”  
    - “Are all inputs parameterized?”  

- **In testing**  
  - Run OWASP‑style tests:
    - Auth‑bypass.  
    - Injection‑type checks.  
    - SSRF‑style payloads.

---

## 4. Example secure‑coding patterns

- **Access control**  
  - Use RBAC; enforce checks on every sensitive‑endpoint, not just the UI.

- **Injection**  
  - Never concatenate user‑input into SQL; use parameterized‑queries or ORMs with safe‑bindings.

- **Auth**  
  - Use strong‑password‑rules, MFA for admins, and short‑lived tokens.

- **Logging**  
  - Log failed‑login attempts and admin‑actions; avoid logging secrets.

---

## 5. How to run this session (10–15 min)

- **0–2 min** – Why OWASP matters for product and security.  
- **2–7 min** – Quick‑tour of 3–5 most‑relevant OWASP‑categories.  
- **7–12 min** – How to use OWASP in PRDs, PR reviews, and testing.  
- **12–15 min** – Q&A; ask “What OWASP‑category is most relevant to your current feature?”

This keeps the talk **practical** and directly tied to engineers’ current work.

---

## 6. Optional follow‑up

- Ask the team to:
  - Tag OWASP‑categories on JIRA‑tickets for the next sprint.  
  - Run a mini‑threat‑model on one feature and share it in the next retro.

This bridges the talk directly into **product‑and‑engineering work**.
