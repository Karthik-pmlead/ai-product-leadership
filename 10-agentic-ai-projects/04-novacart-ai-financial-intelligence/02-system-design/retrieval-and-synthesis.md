# Retrieval and Synthesis

## Objective
Combine internal business performance information with external market intelligence to generate the Monthly Financial Standing Report.

## Workflow

1. The monthly schedule trigger initiates the AI Agent.
2. The agent receives access to two Pinecone retrieval tools.
3. It queries the `internal` namespace for financial and product performance information.
4. It queries the `external` namespace for relevant market intelligence.
5. Retrieved evidence is combined to analyze performance and market context.
6. The agent generates a structured HTML report.
7. Gmail delivers the report to the designated stakeholder.

## Retrieval Sources

| Retrieval Tool | Pinecone Namespace | Information |
|---|---|---|
| Internal Vector Store | `internal` | Financial and product performance |
| External Vector Store | `external` | Market trends and industry intelligence |

## Report Structure

The generated report contains:

1. Executive Summary
2. KPI Dashboard
3. Performance Deep Dive
4. Market Context
5. Drivers & Correlations
6. Risks, Opportunities & Recommendations
7. Sources

## Agent Quality Rules

- Retrieve information from both configured knowledge sources.
- Base findings on retrieved evidence.
- Do not invent financial figures or market statistics.
- Identify unavailable information.
- Avoid unsupported estimates.
- Include source information in the report.
- Generate concise, executive-friendly HTML.

## Output and Delivery

| Parameter | Configuration |
|---|---|
| Trigger | Monthly schedule |
| Report format | HTML |
| Delivery mechanism | Gmail |
| Output | Monthly Financial Standing Report |
