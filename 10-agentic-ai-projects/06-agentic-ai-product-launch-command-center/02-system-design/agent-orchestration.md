# Agent Orchestration

## Overview

The Greeter Agent coordinates stakeholder interactions by identifying intent and routing requests to the appropriate specialist.

## Agent Routing

| Request Type | Destination |
|---|---|
| Engineering, QA, infrastructure, deployment, bugs | Technical Readiness Specialist |
| Campaigns, press, sales enablement, competitors | GTM & Marketing Specialist |
| Launch summaries, risks, budgets, timelines | Executive Briefing Specialist |

## Orchestration Flow

1. Receive stakeholder question.
2. Identify the primary information need.
3. Select the appropriate specialist.
4. Transfer the conversation to that specialist.
5. Provide a relevant response.
6. Handle follow-up questions within the conversation.

## Specialist Responsibilities

**Technical Readiness**
- Technical launch status.
- Engineering and QA readiness.
- Deployment and rollback plans.

**GTM & Marketing**
- Campaign execution plans.
- Press and launch timelines.
- Sales messaging and competitive positioning.

**Executive Briefing**
- Overall launch status.
- Cross-functional risks and dependencies.
- Budget and timeline summaries.

## Design Principle

Use specialist agents for domain-specific questions and the Executive Briefing Specialist for broader cross-functional questions.

This keeps the interaction simple for stakeholders while separating specialist responsibilities.
