# Risk Management – Core Concepts

This document defines the **core concepts** you can use in product‑level risk‑management aligned with GDPR, ISO‑27001, OWASP, and CE‑Marking‑style practices.

---

## 1. What is a “risk”?

In product‑security and compliance, a **risk** is:

> *The chance that a hazard or threat will lead to a negative impact on people, data, systems, or the business.*

Key elements of a risk:

- **Asset** – what is being protected (e.g., PII, payment‑data, admin‑APIs, IoT‑device‑safety).  
- **Threat** – who or what might cause harm (e.g., attacker, insider, misconfiguration, malfunction).  
- **Vulnerability** – what weakness the threat can exploit.  
- **Impact** – what bad outcome could happen (e.g., data‑breach, device‑harm, financial‑loss, reputational‑damage).  
- **Likelihood** – how probable the event is, given current controls.

---

## 2. Risk matrix and ratings

Most teams use a **risk matrix** based on:

- **Likelihood** (e.g., Rare, Unlikely, Possible, Likely, Almost‑Certain).  
- **Impact** (e.g., Negligible, Low, Medium, High, Critical).  

Resulting risk levels:

- **Low / Medium / High / Critical**  
  - High‑risk items drive **immediate action** (e.g., “must‑fix‑before‑launch”).  
  - Medium‑risk items are tracked and scheduled.  
  - Low‑risk items may be accepted with monitoring.

Many organisations use **semi‑quantitative** scoring:

- Assign `1–5` to Likelihood and Impact.  
- Compute **Risk Score = Likelihood × Impact**.  

Example:

| Likelihood | Impact | Risk Level |
|------------|--------|------------|
| 4          | 5      | Critical   |
| 3          | 3      | Medium     |
| 2          | 2      | Low        |

---

## 3. Risk‑treatment types

For each risk, you choose a **treatment**:

- **Accept**  
  - Keep the risk but document it; usually for low‑risk items.  
- **Mitigate**  
  - Reduce Likelihood and/or Impact (e.g., add access‑control, encryption, logging).  
- **Transfer**  
  - Shift risk (e.g., via insurance, SLA‑with‑vendor).  
- **Avoid**  
  - Remove the feature or design pattern causing the risk.  

For product‑leaders, **mitigation** is the default; **avoid** is used when the business‑value does not justify the risk.

---

## 4. Roles in risk‑management

- **Risk‑owner**  
  - Typically a **product‑owner or engineering‑lead** who owns the risk and makes trade‑off decisions.  
- **Risk‑manager**  
  - Often a **security‑or‑compliance‑lead** who structures the risk‑framework and provides guidance.  
- **Reporter / reviewer**  
  - Individual engineers, testers, or auditors who raise or review risks.
