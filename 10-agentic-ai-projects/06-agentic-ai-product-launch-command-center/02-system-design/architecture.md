# System Architecture

## Overview

The Product Launch Command Center uses a multi-agent architecture built with ElevenLabs.

A single Greeter Agent acts as the entry point, identifies stakeholder intent, and routes requests to specialized agents.

## Architecture Diagram

![Multi-Agent Workflow](../06-demo-evidence/screenshots/workflow-architecture.png)

## Components

| Component | Responsibility |
|---|---|
| Start | Initiates the conversation. |
| Greeter Agent | Understands the request and selects the appropriate specialist. |
| Technical Readiness Specialist | Handles engineering and technical questions. |
| GTM & Marketing Specialist | Handles marketing and go-to-market questions. |
| Executive Briefing Specialist | Handles high-level and cross-functional questions. |
| End | Completes the interaction. |

## Interaction Flow

1. Stakeholder starts a voice or text conversation.
2. Greeter Agent interprets the request.
3. Request is routed to the relevant specialist.
4. Specialist responds using its assigned knowledge.
5. Conversation can continue through follow-up questions.

## Design Principles

- Single conversational entry point.
- Specialized agent responsibilities.
- Domain-specific knowledge access.
- Executive-level cross-functional visibility.
- Voice and text interaction support.
