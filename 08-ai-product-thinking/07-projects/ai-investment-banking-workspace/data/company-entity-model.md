# Company Entity Model

---

# Purpose

The company entity model creates a unified representation of organizations and their relationships across internal and external data sources.

---

# Core Entity

Company

Attributes

- Legal Name
- Ticker
- LEI
- Industry
- Sector
- Country
- Exchange
- Market Capitalization
- Ownership Structure

---

# Related Entities

- Executive
- Board Member
- Investor
- Subsidiary
- Parent Company
- Advisor
- Transaction
- Security
- Research Report
- News Article

---

# Entity Relationships

Company

├── Owns → Subsidiary

├── Managed By → Executive

├── Advised By → Investment Bank

├── Participated In → Transaction

├── Covered By → Analyst

├── Mentioned In → News

├── Linked To → Research

└── Issues → Securities

---

# AI Applications

- Relationship Graph
- Client 360
- Similar Company Discovery
- Executive Network Analysis
- Opportunity Detection
