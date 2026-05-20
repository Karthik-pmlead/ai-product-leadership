# Core Business Metrics

## North Star Metric

| Metric | What it measures | Typical use | Notes |
|---|---|---|---|
| North Star Metric | The single metric that best reflects customer value and long-term business success [web:182][web:184]. | Strategy, alignment, prioritization. | Should be customer-centric, actionable, and tied to sustainable business value. |

## How to derive a North Star Metric

A good North Star Metric should reflect the value customers receive, act as a leading indicator of long-term success, and be something the product team can influence directly [web:182][web:184][web:190].

### Tips for deriving it

1. Identify the business model.
   - Ask whether the product is mainly a transaction product, attention product, productivity product, or subscription/business platform [web:194][web:188].

2. Define the core user value.
   - What is the main outcome the customer wants?
   - Examples: buy something, spend time, complete work, learn faster.

3. Map the value chain.
   - Start from the business outcome and break it into smaller product behaviors.
   - Example: watch time can be broken into users, sessions per user, and time per session [web:192].

4. Choose a metric that is:
   - Easy to understand.
   - Customer-centric.
   - Quantitative.
   - Actionable.
   - A leading indicator of success [web:194][web:184].

5. Avoid vanity metrics.
   - Do not choose a metric just because it is large or easy to track.
   - The metric should correlate with real customer value and revenue [web:182].

6. Test whether teams can act on it.
   - If product changes can move the metric, it is more useful.
   - If the metric is too far upstream or downstream, it may be too weak as an NSM [web:196].

### Simple framework

| Step | Question to ask | Output |
|---|---|---|
| 1 | What business are we in? | Transaction, attention, productivity, or subscription/business model. |
| 2 | What value do users get? | Main user outcome. |
| 3 | What behavior shows that value? | Observable user action or usage pattern. |
| 4 | What single metric best represents it? | Candidate North Star Metric. |
| 5 | Can product teams move it? | Final validation. |

### Examples

| Product type | Possible North Star Metric | Why it works |
|---|---|---|
| Transaction product | Completed successful transactions per active user. | Shows value delivery and repeat usage. |
| Attention product | Time spent in meaningful sessions per active user. | Captures engagement and habitual use. |
| Productivity product | Tasks completed successfully per user per week. | Reflects real work outcome. |
| Marketplace | Successful matches or completed orders. | Represents platform value creation. |
| SaaS / B2B product | Weekly active teams completing key workflows. | Connects usage to business value. |

## Core business metrics

| Metric | What it measures | Typical use | Notes |
|---|---|---|---|
| NPS | Customer loyalty and willingness to recommend. | Brand and satisfaction. | Best used as a directional sentiment metric. |
| CSAT | Customer satisfaction after a specific interaction. | Support, onboarding, checkout. | Good for transaction-level feedback. |
| CAC | Cost to acquire a customer. | Growth and marketing efficiency. | Pair with LTV or CLV. |
| LTV / CLV | Revenue expected from a customer over time. | Retention and profitability. | CLV and LTV are often used interchangeably. |
| ARPU | Average revenue per user. | Monetization. | Useful across consumer and SaaS products. |
| ARR | Annual recurring revenue. | SaaS planning. | Annualized recurring revenue. |
| MRR | Monthly recurring revenue. | SaaS growth tracking. | Useful for subscription businesses. |
| ROAS | Revenue generated per unit of ad spend. | Paid acquisition. | Marketing efficiency metric. |
| CPA | Cost per acquisition or cost per action. | Paid growth. | Use the exact definition in each repo entry. |
| AARRR | Acquisition, Activation, Retention, Revenue, Referral. | Growth framework. | A framework, not a single metric. |
| RFM | Recency, Frequency, Monetary value. | Segmentation. | Useful for lifecycle and CRM analysis. |
| CRM | Customer relationship management. | Sales, retention, account management. | System/category rather than one metric. |

## Notes for use

| Topic | Guidance |
|---|---|
| Single source of truth | Keep the North Star Metric in this file, near the top. |
| Segment-specific metrics | Add supporting metrics in category files. |
| Metric hierarchy | Use North Star Metric for strategy, then supporting KPIs for diagnosis. |
| Review cadence | Re-check the NSM when strategy, business model, or customer value changes. |
| Avoid confusion | A metric can be important without being the North Star Metric. |
