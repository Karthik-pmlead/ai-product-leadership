# Security and Data Handling

## Objectives
Protect checkout data, credentials, spreadsheet access, and webhook integrations.

## Data Handling
- Store only fields required for incident detection and audit.
- Restrict access to checkout events and command records.
- Avoid exposing customer-identifiable or payment-sensitive data in logs.
- Define retention and deletion policies.

## Credentials and Endpoints
- Store API credentials and webhook URLs securely in n8n credentials or environment configuration.
- Do not commit live webhook URLs, spreadsheet identifiers, secrets, or sensitive sample data to a public repository.
- Sanitize exported workflow JSON before publishing.
- Rotate any exposed credentials or webhook endpoints as appropriate.

## Access Control
Apply least-privilege access to Google Sheets, n8n workflows, and the receiving webhook. Separate development and production configurations.

## Validation Checklist
- [ ] Remove secrets and sensitive identifiers from repository files.
- [ ] Verify access permissions.
- [ ] Confirm logs exclude sensitive data.
- [ ] Document retention and credential-rotation procedures.
- [ ] Test authentication and unauthorized-request handling.

**Status:** These are recommended controls; implementation and compliance have not been independently verified.
