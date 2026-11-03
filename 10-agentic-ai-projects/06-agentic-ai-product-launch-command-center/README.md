# Agentic AI Product Launch Command Center

A multimodal (voice + text) AI command center that helps Product Managers and Technical Program Managers handle stakeholder questions during a product launch.

## The Problem

During a product launch, PMs and TPMs become the organization's human switchboard.

Engineering asks about technical readiness. Marketing asks about campaign timelines. Executives need status summaries. Sales needs competitive positioning.

PMs spend valuable time answering recurring questions instead of making decisions and resolving problems.

## The Solution

A multimodal AI agent built with **ElevenLabs** that acts as a Product Launch Command Center.

Stakeholders can interact through voice or text. A Greeter Agent understands the request and routes it to the appropriate specialist.

| Agent | Responsibility |
|---|---|
| Greeter Agent | Understands requests and routes conversations |
| Technical Readiness Specialist | Engineering, QA, deployment, infrastructure, and bugs |
| GTM & Marketing Specialist | Campaigns, press timelines, sales enablement, and competitive positioning |
| Executive Briefing Specialist | Executive summaries, launch risks, budget, and timelines |

## Architecture

The solution uses a multi-agent orchestration pattern with one entry point and specialized agents.

![Agent Workflow Architecture](06-demo-evidence/screenshots/workflow-architecture.png)

### Knowledge Scoping

Each specialist receives knowledge relevant to its responsibilities.

- **Technical Readiness:** Technical launch information.
- **GTM & Marketing:** Marketing and go-to-market information.
- **Executive Briefing:** Consolidated launch information across domains.

This separation helps prevent irrelevant cross-domain information from entering specialist responses while allowing the Executive Briefing Specialist to provide an overall view.

## Implementation

- **Platform:** ElevenLabs
- **Interaction:** Voice and text
- **Architecture:** Greeter and specialized agents
- **Scenario:** Fictional enterprise product launch

## Repository Structure

```text
01-product-definition/   # Problem, requirements, success metrics
02-system-design/        # Architecture and orchestration
03-agent-design/         # Agent responsibilities and prompts
04-knowledge-base/       # Domain-specific launch knowledge
05-implementation/       # ElevenLabs configuration
06-demo-evidence/        # Demo script, video, screenshots
```

## Demo

- **Video:** [Add demo video link]
- **Workflow screenshots:** [View screenshots](06-demo-evidence/screenshots/)

## Product Takeaway

The goal is not to replace the PM or TPM. It is to reduce repetitive stakeholder coordination so they can focus on decisions, execution, and launch outcomes.

This project demonstrates a practical multi-agent pattern: **one conversational entry point, specialized knowledge domains, and coordinated stakeholder support.**
