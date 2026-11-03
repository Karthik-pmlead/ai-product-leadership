# Workflow Configuration

## Workflow Overview

The ElevenLabs workflow uses a Greeter Agent as the entry point and specialist agents for domain-specific conversations.

## Interaction Flow

1. Stakeholder initiates a voice or text conversation.
2. Greeter Agent receives the request.
3. Greeter identifies the question category.
4. Request is handed off to the relevant specialist.
5. Specialist responds using assigned knowledge.
6. Stakeholder can continue the conversation.

## Agent Handoffs

| Source | Destination |
|---|---|
| Greeter | Technical Readiness |
| Greeter | GTM & Marketing |
| Greeter | Executive Briefing |

## Knowledge Configuration

| Agent | Assigned Knowledge |
|---|---|
| Technical Readiness | Technical launch knowledge |
| GTM & Marketing | Marketing launch knowledge |
| Executive Briefing | Consolidated launch knowledge |

## Validation Checklist

- [ ] Voice interaction works.
- [ ] Text interaction works.
- [ ] Technical questions reach the correct specialist.
- [ ] Marketing questions reach the correct specialist.
- [ ] Executive questions reach the correct specialist.
- [ ] Responses use relevant knowledge.
- [ ] Follow-up questions work as expected.

*Document the actual tested configuration and update this file if the workflow changes.*
