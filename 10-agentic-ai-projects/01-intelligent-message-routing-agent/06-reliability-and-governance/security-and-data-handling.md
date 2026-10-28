# Security and Data Handling

## 1. Current Design

The workflow receives messages through an n8n Chat Trigger, processes them using an AI Agent and an OpenRouter chat model, and appends extracted information to Google Sheets.

## 2. Security Considerations

- **Prompt injection:** Treat incoming message content as untrusted input. Test attempts to override routing instructions.
- **Credential management:** Store API keys and service credentials securely in n8n credentials, not in prompts or public files.
- **Spreadsheet access:** Restrict access to authorized users who need it.
- **Data privacy:** Use synthetic or anonymized messages in testing and portfolio demonstrations.
- **Workflow export:** Review JSON files before publishing; remove secrets, personal information, and unnecessary environment-specific identifiers.
- **Public links:** Do not expose private spreadsheet links or real customer records.

## 3. Pre-Publication Checklist

- [ ] Check workflow JSON for API keys, tokens, and secrets.
- [ ] Review spreadsheet IDs, URLs, and credential references.
- [ ] Verify Google Sheets sharing permissions.
- [ ] Test prompt-injection examples and inspect routing outcomes.
- [ ] Ensure sample data and screenshots contain no sensitive information.

## 4. Known Limitations

The exported JSON alone does not establish that formal prompt-injection defenses, data-retention controls, access reviews, or compliance controls are implemented.

Verify these separately before claiming them as implemented capabilities.
