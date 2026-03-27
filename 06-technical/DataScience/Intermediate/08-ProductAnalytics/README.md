# Product Analytics Knowledge Base (DAV_ProductAnalytics)

Welcome to the **Product Analytics Knowledge Base**, a curated collection of business frameworks, metrics, experimentation patterns, and analysis techniques for driving product-led growth. This repository bridges technical analysis with business strategy for data-informed product decisions.

This repository is useful for:
- Building product roadmaps aligned with key business metrics and customer behavior.
- Designing statistically valid A/B tests, customer segmentation, and growth experiments.
- Conducting root cause analysis (RCA) and market sizing (guesstimates) for strategic decisions.

---

## Table of Contents

| Section | Description | Link |
|---------|-------------|------|
| Notes | Core concepts (North Star Metric, AARRR funnel, cohort analysis, LTV/CAC). | [notes/README.md](notes/README.md) |
| Patterns | Experiment frameworks (A/B testing, bandit algorithms, sequential testing). | [patterns/README.md](patterns/README.md) |
| Projects | End-to-end analytics (funnel optimization, retention cohorts, pricing analysis). | [projects/README.md](projects/README.md) |
| Assignments | Business challenges (guesstimate markets, RCA drop-offs, segment profitability). | [assignments/README.md](assignments/README.md) |
| Repositories | Links to Mixpanel, Amplitude, PostHog, and growth analytics toolkits. | [repos/README.md](repos/README.md) |
| Videos | Talks on product-led growth, experimentation systems, metrics that matter. | [videos/README.md](videos/README.md) |
| Templates | Boilerplates (AARRR dashboards, experiment tracking, RCA frameworks). | [templates/README.md](templates/README.md) |
| Interview Prep | PM/DA questions (market sizing, funnel analysis, experimentation design). | [interview-prep/README.md](interview-prep/README.md) |

---

## Quick Start Frameworks

### AARRR Pirate Metrics
Acquisition → Activation → Retention → Referral → Revenue


### Core Product Metrics

Health: DAU/MAU, Retention D1/D7/D30, Churn Rate
Growth: LTV, CAC, Magic Number, Rule of 40
Engagement: Session depth, Feature adoption, Power user ratio

### Customer Segmentation Matrix
Segment	Behavior	Value	Action
New Users	Exploratory	Low	Onboarding
Power Users	High engagement	High	Retention/Expansion
At-Risk	Declining	Medium	Win-back
Lost	Churned	Low	Reacquisition

### 1. A/B Testing Framework

    Define North Star → 2. Segment users → 3. Power analysis

    Randomize → 5. Monitor → 6. Statistical significance → 7. Business decision


### 2. Root Cause Analysis (RCA) Pipeline

    Identify problem metric → 2. Funnel decomposition

    Segment analysis → 4. Cohort analysis → 5. User journey mapping

    Qualitative research → 7. Prioritized experiments


### 3. Customer Segmentation Strategy

RFM (Recency, Frequency, Monetary) → Behavioral clusters
→ Lifecycle stages → Value-based tiers → Personalized strategies

## Key Libraries & Tools

Analytics: Mixpanel, Amplitude, PostHog, Segment
Visualization: Metabase, Looker, Tableau, Plotly Dash
Experimentation: Optimizely, GrowthBook, Eppo
SQL: dbt, Dataform for product analytics pipelines

## Business Frameworks Coverage
Metrics:

    North Star Metric selection

    Funnel conversion optimization

    Cohort retention analysis

    LTV/CAC modeling

Experiments:

    A/B + Multivariate testing

    Bandit algorithms

    Sequential testing

    Holdout groups

Strategy:

    PRD writing frameworks

    Roadmap prioritization (RICE, ICE)

    Market sizing (guesstimates)

    Go-to-market analytics

