# Observability

## 1. Purpose

Establish visibility into workflow execution, specialist-agent behavior, external search dependencies, and final itinerary quality.

The objective is to make failures diagnosable and system behavior measurable across the V4 Main Workflow and V3 Execution Workflow.

## 2. Observability Architecture

```text
User Request
     |
     v
V4 Main Workflow
     |
     |-- Coordinator
     |-- Planner
     |
     v
V3 Execution Workflow
     |
     |-- Travel Orchestrator
     |-- Flights Agent
     |-- Hotels Agent
     |-- Activities Agent
     |
     v
Consolidated Results
     |
     v
V4 Validator
     |
     v
Final Response

Observability Across Workflow Stages:
Execution Status | Latency | Errors | Result Quality
```

## 3. Key Observability Dimensions

| Dimension | What to monitor |
|---|---|
| Workflow execution | Successful and failed executions |
| Agent execution | Invocation status and output availability |
| External dependencies | SerpApi and Tavily failures |
| Latency | End-to-end and stage-level execution time |
| Input quality | Mandatory-field completeness |
| Output quality | Recommendation completeness and consistency |
| Validation | Detected conflicts and unresolved issues |

## 4. Proposed Metrics

| Metric | Definition |
|---|---|
| Workflow completion rate | Successful executions / total executions |
| Agent completion rate | Successful agent executions / attempted executions |
| End-to-end latency | Time from user request to final response |
| Agent latency | Time spent in each specialist-agent execution |
| External API failure rate | Failed external requests / total requests |
| Validation issue rate | Outputs containing identified inconsistencies / evaluated outputs |
| Incomplete result rate | Executions with missing specialist results / total executions |

These are proposed operational metrics, not currently measured production statistics.

## 5. Diagnostic Logging

Recommended execution metadata:

- Workflow execution ID.
- Chat session identifier.
- Workflow version.
- Agent name.
- Execution start and end timestamps.
- External tool status.
- Error category.
- Output completeness status.

Avoid logging unnecessary personal information or sensitive credentials.

## 6. Monitoring Strategy

Recommended monitoring layers:

**Workflow level**
- Track V4 and V3 execution outcomes.
- Identify incomplete workflow runs.

**Agent level**
- Track specialist execution status.
- Identify agents with recurring failures or poor output quality.

**Dependency level**
- Track SerpApi and Tavily errors.
- Monitor external API latency and availability.

**Product-quality level**
- Evaluate recommendation relevance.
- Track cross-agent conflicts.
- Monitor final itinerary acceptance.

## 7. Current Implementation

The system uses n8n workflows and connected execution nodes. The workflow configuration provides execution structure, but does not establish a complete centralized observability platform, distributed tracing system, or production monitoring dashboard.

## 8. Future Enhancements

- Centralized structured logs.
- Correlation IDs across V4 and V3.
- Agent-level execution dashboards.
- Latency and failure alerts.
- External dependency health monitoring.
- Automated quality evaluation.
- Execution-level audit trails.

**Design principle:** Measure the complete user journey, not just individual agent execution success.
