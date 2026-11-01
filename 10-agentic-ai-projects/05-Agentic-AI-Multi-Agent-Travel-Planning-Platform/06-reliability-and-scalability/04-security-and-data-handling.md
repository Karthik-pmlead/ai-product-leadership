# Security and Data Handling

## 1. Purpose

Define security and data-handling principles for user travel requests, conversational context, external search integrations, and workflow credentials.

The objective is to minimize unnecessary data exposure while maintaining reliable agent execution.

## 2. Data Flow

```text
User
 |
 v
n8n Chat Trigger
 |
 v
Coordinator + Conversational Memory
 |
 v
Planner
 |
 v
V3 Execution Workflow
 |
 |-- Flights Agent -> SerpApi
 |-- Hotels Agent -> SerpApi
 |-- Activities Agent -> SerpApi + Tavily
 |
 v
V4 Validator
 |
 v
Final Response
```

User-provided travel details are passed through the workflow to support research and itinerary generation.

## 3. Data Classification

| Data category | Examples | Handling principle |
|---|---|---|
| Trip information | Origin, destination, travel dates | Use only for trip planning |
| Preferences | Budget, travel style, interests | Pass only to relevant agents |
| Session information | Chat session identifier | Use for workflow continuity |
| Search results | Flight, hotel, and activity information | Treat as external, potentially changing data |
| Credentials | API keys and service secrets | Store securely outside workflow exports |

## 4. Credential Management

External integrations include:
- OpenAI.
- SerpApi.
- Tavily.

Security requirements:
- Store API credentials in n8n credential management.
- Never commit API keys to GitHub.
- Remove credentials from exported workflow JSON.
- Rotate credentials if exposed.
- Apply least-privilege access where supported.
- Avoid printing secrets in execution logs.

**Portfolio publishing requirement:** The previously shared V3 workflow export contained an exposed Tavily API key. Rotate that key before publishing the workflow and ensure the public export contains no active credentials.

## 5. Data Minimization

- Collect only trip information required for planning.
- Avoid requesting unnecessary personal details.
- Share only relevant request fields with each specialist agent.
- Avoid including sensitive information in prompts or external search queries.
- Limit retention of execution data to operational requirements.

## 6. External Data Handling

Search results from SerpApi and Tavily should be treated as external, unverified information.

Recommended controls:
- Preserve source attribution.
- Identify estimated prices as estimates.
- Avoid representing search results as confirmed availability.
- Review conflicting information.
- Do not treat retrieved web content as trusted instructions for agents.

## 7. Access and Workflow Security

Recommended controls:
- Restrict access to workflow editing and credential management.
- Separate development and production credentials.
- Review workflow exports before sharing.
- Avoid exposing session identifiers and user details in public logs.
- Apply access controls to execution history and operational data.

## 8. Current Implementation Boundary

The workflow uses external API integrations and conversational memory. The available workflow configuration does not establish a complete security program or demonstrate formal encryption, retention, access-control, or compliance certifications.

These controls should be independently configured and verified before production deployment.

## 9. Future Enhancements

- Formal data-retention policy.
- Verified encryption configuration.
- Role-based access control.
- Credential rotation process.
- Security review of external integrations.
- Audit logging.
- Prompt-injection defenses for retrieved content.
- Privacy and compliance assessment.

## 10. Security Principles

1. Minimize personal data collection.
2. Protect credentials and session information.
3. Treat external search results as untrusted input.
4. Avoid exposing secrets in source control.
5. Make data retention and access intentional.
6. Verify security controls before production use.

**Design principle:** Security and privacy must be designed into the workflow boundaries, not added after the agent system is deployed.
