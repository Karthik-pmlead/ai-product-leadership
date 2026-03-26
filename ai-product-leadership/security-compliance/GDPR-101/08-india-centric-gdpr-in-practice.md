# GDPR 101 – India‑Centric GDPR in Practice

This document explains how GDPR applies in practice to India‑based product, engineering, and AI‑product teams, including common pitfalls and good practices.

---

## 1. Where Indian organisations touch GDPR

Indian companies often fall under GDPR because they process personal data of individuals in the EU/EEA, even if:

- HQ and engineering are in India.  
- Product is sold or used by EU customers or users.  
- Global parent or clients host EU data in India‑based systems.

Typical roles include:

- **SaaS / B2B products** (HR, analytics, marketing, collaboration).  
- **IT services and outsourcing** (developing or maintaining EU‑customer systems).  
- **Data‑analytics and AI platforms** that profile or train models on EU data. [web:114][web:111]

---

## 2. India‑specific challenges and pitfalls

### 1. Cloud‑hosting and data flows

Indian teams often use global cloud regions (e.g., Mumbai, Singapore, US) for EU data, which can create **international transfers** that need SCCs and sometimes TIAs.

- **Risk**  
  Storing EU data in a non‑EU region without documented transfer‑safeguards.

### 2. Vendor and BPO relationships

Global controllers often treat Indian teams as **data processors** (e.g., payroll, support, analytics). PMs must ensure:

- Clear **Data Processing Agreements (DPA)** with DPAs, SCCs, and security expectations.  
- Role‑based access and logging for EU data. [web:114][web:111]

### 3. Over‑reliance on “consent for everything”

Using vague consents for marketing, profiling, or remarketing makes bases fragile and easy to challenge.

- **Risk**  
  Large‑scale ad‑tech or profiling campaigns that rely on non‑specific consents attract fines. [web:117][web:124]

---

## 3. GDPR‑in‑practice for India‑based teams

### 1. Design‑time discipline

- **Choose and document lawful basis** (contract, legitimate interest, or explicit consent) for every EU‑related feature in the PRD.  
- **Map EU data flows** (what data, where stored, who accesses it, where it’s transferred) and update it regularly. [web:114][web:111]

### 2. Data‑subject request workflows

- Build **access, export, rectify, delete, restrict, and object** flows into the product, not just via support tickets.  
- Respect the **one‑month** deadline for EU‑data‑subject requests even if local law has different timelines. [web:79][web:82]

### 3. Security and governance

- Implement **encryption at rest and in transit**, **RBAC**, logging, and incident‑response playbooks for EU data.  
- Maintain **Records of Processing Activities (RoPA)** and integrate **DPIA triggers** into feature design (e.g., profiling, biometrics, large‑scale monitoring). [web:117][web:105]

### 4. Align with global standards

- Leverage **ISO 27001, GDPR‑style frameworks, and DPDP‑adjacent thinking** to satisfy both GDPR and domestic expectations.  
- Run a **data‑protection committee** or DPO‑supported cadence to review new features, high‑risk transfers, and incident responses. [web:110][web:115]

---

> **Wrap‑up**  
This folder (`ai-product-leadership/security-compliance/GDPR-101/`) is now a coherent sequence of 8 markdown files for GDPR 101 aimed at product leaders and AI‑product teams. You can further extend it with role‑specific checklists (e.g., “GDPR‑by‑design for AI products”) while keeping this structure intact.
