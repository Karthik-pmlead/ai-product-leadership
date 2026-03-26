# GDPR 101 – AI Product Leadership

This is a **GDPR‑101** guide tailored for **AI‑product leaders, product managers, and engineering teams**. It distills core GDPR concepts into practical, product‑level understanding rather than pure legal theory.

---

## What this collection is for

- **Product leaders** who ship AI, data‑intensive, or SaaS products that touch personal data of individuals in the EU/EEA.  
- **Engineering and data‑science leaders** who design systems, pipelines, and analytics that store or process EU‑resident data.  
- **AI‑focused teams** that build recommendation engines, personalization, profiling, or automated decision‑making systems.

The goal is to help you **embed GDPR into product design**, data flows, and architecture decisions, not treat it as a “compliance‑only” afterthought.

---

## How to use this folder

| File name                                 | Purpose (what it covers)                                                                 | How to use it                                                                 |
|-------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [`01-basics-and-terminologies.md`][01]   | Core GDPR terms: personal data, processing, controller, processor, breach, etc.          | Quick glossary for onboarding, decks, or PRD definitions.                    |
| [`02-gdpr-key-principles.md`][02]        | GDPR’s 7 core principles (lawfulness, data minimisation, accountability, etc.).         | Reference for feature‑level “GDPR‑by‑design” checklists.                     |
| [`03-privacy-by-design.md`][03]          | “Privacy by design and by default” in product terms.                                    | Template for baking privacy into product specs and architecture decisions.     |
| [`04-data-controller-processor.md`][04]  | Who is responsible: controller vs processor and their roles.                             | Clarify roles with vendors, BPOs, and SaaS providers.                        |
| [`05-data-subject-rights.md`][05]        | 8 rights of data subjects and product‑level implications.                               | Guide for designing DSAR flows (access, delete, export, object, etc.).      |
| [`06-lawful-bases-security.md`][06]      | Lawful bases (consent, contract, legitimate interest) and security/compliance techniques.| Use in PRDs to justify data‑collection and security requirements.            |
| [`07-international-transfers-enforcement.md`][07]| International data transfers and GDPR enforcement/fines.                             | Align data‑residency and cross‑border flows with product‑level safeguards.   |
| [`08-india-centric-gdpr-in-practice.md`][08]| GDPR‑in‑practice for India‑based product and engineering teams.                         | Tailor global GDPR patterns to India‑based SaaS, IT‑services, and AI products.|

---

## Target audience

- **AI‑product leaders** who want to understand GDPR as a **product constraint and driver**, not just a legal risk.  
- **India‑based** PMs, EMs, and architects whose products serve or process data from EU residents.  
- **Data, ML, and security leaders** who translate GDPR into data‑minimisation, pseudonymization, consent‑management, and DSAR workflows.

---

## Contributing and extending

If you are building on this collection, consider adding:

- Role‑specific checklists (e.g., “GDPR‑by‑design for AI recommendations”).  
- Feature‑specific templates (e.g., “GDPR‑checklist for profiling or automated decision‑making”).  
- Local‑law bridges (e.g., GDPR ↔ India’s DPDP‑Act mapping sections).

This repo is structured so each `.md` file can stand alone, yet they form a coherent **GDPR 101 module** for AI‑product leadership.  

---

[01]: 01-basics-and-terminologies.md  
[02]: 02-gdpr-key-principles.md  
[03]: 03-privacy-by-design.md  
[04]: 04-data-controller-processor.md  
[05]: 05-data-subject-rights.md  
[06]: 06-lawful-bases-security.md  
[07]: 07-international-transfers-enforcement.md  
[08]: 08-india-centric-gdpr-in-practice.md
