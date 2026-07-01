# Agent Flow — Dynamic Execution System

## Purpose

Defines how the system dynamically selects and executes agents based on user intent.

---

## Step 1: Router Agent

Input:
- User query

Output:
```json
{
  "intent": "company_analysis",
  "company": "Tesla"
}
```
Step 2: Dynamic Planner

Converts intent into execution graph:

Example
company_analysis
Risk → Opportunity → Recommendation
competitor_analysis
Competitor → Risk → Opportunity → Recommendation
Step 3: Execution Layer

Agents execute in planned order:

Risk Agent
Identifies business, market, regulatory risks
Opportunity Agent
Identifies growth vectors and expansion areas
Recommendation Agent
Synthesizes actionable strategy
Competitor Agent (optional)
Performs comparative analysis
Step 4: Memory Injection

Before agent execution:

Past company context is retrieved
Injected into prompts
Step 5: Streaming Output

Each agent emits:
```
{
  "agent": "Risk",
  "status": "done",
  "trace": {...}
}
```
Step 6: Final Aggregation

Final response includes:

Risks
Opportunities
Recommendations
Evaluation scores
Full trace log
Key Property

The system is not static pipeline-based, it is:

A dynamic execution graph driven by planner decisions
