# Security & Compliance Pre‑Launch Checklist

Use this checklist before **launching a product, feature, or major version** to ensure minimum security, privacy, and, where applicable, product‑safety expectations are met.

---

## 1. Who runs this checklist

- **Product‑owner** (overall owner of the checklist).  
- **Engineering lead** (verification of technical items).  
- **Security / compliance‑lead** (sign‑off on higher‑risk items).  

---

## 2. Data‑protection (GDPR‑style)

- [ ] Define **data‑map** for the feature:  
  - What personal data is collected?  
  - Where is it stored?  
  - Who has access?

- [ ] Specify **lawful‑basis** (e.g., consent, contractual‑necessity) and **purpose**.  

- [ ] Implement **consent‑management** UI (opt‑in / opt‑out) where needed.  

- [ ] Implement **data‑retention** and **deletion** flows for user‑rights (e.g., “Delete my account”).  

- [ ] Confirm **logging‑of‑consent‑events** and **audit‑trail** for data‑access‑requests.

---

## 3. Access control and authentication

- [ ] All **sensitive endpoints** are authenticated.  

- [ ] Role‑based‑access‑control (RBAC) is enforced (e.g., user vs admin).  

- [ ] **Admin‑functions** require MFA or strong‑authentication.  

- [ ] There are **no hard‑coded credentials** or secrets in code.  

- [ ] **API‑keys or tokens** are scoped to minimum‑required permissions.

---

## 4. Secure‑coding and OWASP‑alignment

- [ ] All **user‑inputs** are validated and sanitized (schema‑validation, escaping, etc.).  

- [ ] No **SQL‑injection**‑style patterns (only parameterized‑queries).  

- [ ] All **critical‑endpoints** are logged and monitored (failed‑login, admin‑actions).  

- [ ] Dependencies are **scanned** and no critical‑vulnerabilities are present.  

- [ ] **OWASP‑Top‑10‑style** risks are reviewed in `risk-management/registers/example-owasp-risk-register.md` and all high‑and‑critical items are mitigated or accepted‑with‑rationale.

---

## 5. Infrastructure and configuration

- [ ] All **production‑environments** use TLS‑1.2+.  

- [ ] Firewalls and network‑segmentation follow org‑policy.  

- [ ] **Secrets** are stored in secrets‑management tools (Vault, Secrets Manager, etc.).  

- [ ] **Backups** exist and are tested periodically.  

- [ ] **Disaster‑recovery** plan is documented (even if short).

---

## 6. Product‑safety and CE‑style (IoT / connected‑products)

- [ ] **Hazard‑analysis** and **risk‑assessment** completed (see `risk-management/registers/example-ce-risk-register.md`).  

- [ ] **Safe‑default‑state** defined for key failure‑modes (e.g., low‑battery, comms‑loss, firmware‑bricked).  

- [ ] **Physical‑and‑environmental‑tests** completed (e.g., IP‑rating, heat‑test, mechanical‑stress).  

- [ ] **User‑manuals and safety‑instructions** updated to reflect new features.  

---

## 7. Sign‑off and documentation

- [ ] **Risk‑register** updated with any new risks or changes.  

- [ ] **Incident‑response** and **RCA** templates ready if needed.  

- [ ] **Pre‑launch‑sign‑off** by:
  - Product‑owner.  
  - Engineering‑lead.  
  - Security‑/compliance‑lead (for high‑risk features).  

This checklist can be turned into a **per‑feature template** (e.g., in JIRA / Notion) and reused for every major release.
