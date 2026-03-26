# Secure Coding – Lightning Talk for Engineers

This outline is for a **5–10 minute lightning talk** for developers, showing how to turn secure‑coding guidelines into everyday habits.

---

## 1. Why secure‑coding matters

- Every bug‑report or hotfix spends time and money.  
- Security‑bugs often have **higher impact**: data‑breaches, outages, regulatory‑fines, reputational‑damage.

Secure‑coding is:
- Part of **product‑quality**, not a separate “security” job.

---

## 2. Four golden rules at the gate

Tell the team to ask four questions before merging any code that touches auth, API, or user‑input:

- **1. Is all input validated and escaped?**  
  - Any user‑input (API, UI, CLI) must be:
    - Schema‑validated.  
    - Escaped when used in SQL / templates / OS‑commands.  

- **2. Are all sensitive endpoints authenticated and authorised?**  
  - No “just‑UI‑hide” security.  
  - Check RBAC on the backend.

- **3. Are secrets out of code and config?**  
  - No hardcoded passwords, tokens, or API‑keys.  
  - Use secrets‑management tools (Vault, Secrets Manager, etc.).

- **4. Are critical‑events logged?**  
  - Failed‑logins, admin‑actions, errors, and unusual‑patterns should be logged and monitored.

---

## 3. Secure‑coding in PR reviews

Suggest this **checklist** for PR‑reviewers:

- [ ] Schema‑validation on all user‑inputs?  
- [ ] Parameterized‑queries for SQL; no string‑based‑concatenation?  
- [ ] Auth‑and‑RBAC present on sensitive‑endpoints?  
- [ ] No secrets in source‑code or config‑files?  
- [ ] Logs capture security‑relevant‑events (without exposing secrets)?

Make this part of your **PR template**.

---

## 4. How to run this in 5–10 minutes

- **0–1 min** – Why secure‑coding matters.  
- **1–4 min** – Four golden rules explained with small examples.  
- **4–8 min** – How to use them in PR‑reviews.  
- **8–10 min** – Q&A; ask “What one secure‑coding‑rule do you want to enforce in your team from next week?”

This keeps the session **short and immediately actionable**.

---

## 5. Optional follow‑up

- Ask each team to:
  - Add the **four‑golden‑rules** checklist to their PR template.  
  - Run a “secure‑coding‑retro” in one sprint to review past‑security‑bugs.

This turns a lightning talk into a **visible change
