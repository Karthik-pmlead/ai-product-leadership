# Example GDPR‑Style Risk Register

This file shows a **GDPR‑aligned risk register** for a product‑team shipping a web and mobile app that processes user personal data (e.g., name, email, phone, device‑ID, activity logs). It aligns with GDPR‑principles and feeds into your product‑backlog and compliance‑documentation.

---

## Risk Register Table

| Risk ID   | Subject / Title                                           | Asset                                | Threat                              | Vulnerability                                                          | Likelihood (1–5) | Impact (1–5) | Risk score | Risk level   | Risk‑owner            | Mitigation plan                                                                                              | Due date    | Status        | Evidence / notes |
|-----------|-----------------------------------------------------------|--------------------------------------|-------------------------------------|------------------------------------------------------------------------|------------------|--------------|------------|--------------|------------------------|----------------------------------------------------------------------------------------------------------------|-------------|---------------|------------------|
| GDPR‑001  | Consent not collected for marketing emails                | User email, consent flags            | Marketing team / automation misuse  | No explicit opt‑in mechanism for marketing communications              | 4                | 4            | 16         | High         | po-marketing@company  | Implement explicit consent checkbox for marketing emails; default to “off”; add audit‑log of user‑consent‑changes | 2026‑05‑15  | In‑progress   | PRD‑section‑GDPR‑consent, JIRA‑ID‑MARK‑001 |
| GDPR‑002  | No user‑facing way to delete account data                 | User PII, activity logs              | Data‑subject exercising “right to be forgotten” | No self‑service delete‑account flow; delete only via support ticket    | 3                | 5            | 15         | High         | po-product@company    | Implement “Delete my account” UI; backend script to erase PII; enforce within 30 days as per GDPR               | 2026‑06‑01  | Open          | GDPR‑data‑retention‑policy, JIRA‑ID‑PRIV‑002 |
| GDPR‑003  | Logs accidentally capturing full request payloads with PII | Server logs, debug logs              | Insider‑employee or attacker with log access | Debug logging at `INFO`/`DEBUG` level includes raw request bodies      | 3                | 4            | 12         | High         | eng-lead-backend@company | Mask PII in logs; move PII‑heavy debug‑logs behind RBAC; enforce structured logging without raw‑bodies          | 2026‑05‑20  | Open          | OWASP‑logging‑guidelines, JIRA‑ID‑SEC‑003 |
| GDPR‑004  | No formal data‑retention policy for activity logs         | Activity logs, session‑analytics     | Regulatory‑audit or data‑breach     | Logs are kept indefinitely; no automated retention‑or‑deletion‑cycle   | 2                | 4            | 8          | Medium       | eng-lead-data@company   | Define data‑retention‑periods (e.g., 90 days for logs, 365 days for fraud‑logs); implement auto‑delete‑jobs     | 2026‑07‑15  | Open          | Internal‑data‑policy‑draft, JIRA‑ID‑OPS‑004 |
| GDPR‑005  | Third‑party analytics service has PII‑like data without DPA | Device‑ID, IP‑derived location, events | Regulator / data‑protection‑authority | No Data Processing Agreement (DPA) signed with analytics vendor        | 3                | 3            | 9          | Medium       | comms‑lead-legal@company | Review vendor’s DPA; sign or replace; ensure only anonymised‑or‑pseudonymised‑data is sent                    | 2026‑06‑30  | Open          | Vendor‑privacy‑policy, DPA‑template‑link |
| GDPR‑006  | Consent‑logs not tied to specific user‑sessions           | Consent‑event logs, timestamps       | Regulatory‑audit or breach‑investigation | Consent‑events are stored without session‑ID or device‑context        | 2                | 3            | 6          | Low          | eng-lead-frontend@company | Add session‑ID and device‑type to consent‑events; link to user‑ID in secure‑way                             | 2026‑08‑15  | Open          | Consent‑schema‑diagram, JIRA‑ID‑PRIV‑006 |

---

## How this ties into product‑work

- **Product‑owners** use this register to:
  - Prioritise GDPR‑related tickets alongside feature‑work.  
  - Ensure PRDs explicitly address the “Mitigation plan” items above.  

- **Engineering teams** use this register to:
  - Pull GDPR‑risks into their sprint‑planning as **security‑and‑compliance tickets**.  
  - Reference “Evidence / notes” (e.g., JIRA‑IDs, PRDs, policies) when implementing controls.  

- **Security‑/compliance‑leads** use this register to:
  - Demonstrate a **systematic risk‑assessment** during GDPR‑audits or ISO‑27001‑style reviews.  
  - Track that high‑risk items (GDPR‑001, GDPR‑002, GDPR‑003) are on a clear roadmap.

You can reuse this structure for any new GDPR‑launch or product‑variant; just copy the table and update the rows with your concrete risks.
