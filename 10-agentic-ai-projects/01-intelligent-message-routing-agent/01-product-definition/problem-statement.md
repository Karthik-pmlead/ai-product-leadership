# Problem Statement

Incoming customer messages often mix sales inquiries, demo requests, support issues, and irrelevant content. Manually reviewing and categorizing these messages can delay responses and create inconsistent routing.

The goal is to build an **LLM-powered message-routing agent** using n8n that classifies incoming messages, extracts relevant details, and routes them to the appropriate Google Sheets destination: Demo, Support, or Spam.

**Objective:** Reduce manual triage while improving routing consistency and information capture.

**Key challenge:** Handle ambiguous or mixed-intent messages reliably without misclassifying legitimate customer inquiries.

**Success measures:** Classification accuracy, routing accuracy, required-field completeness, duplicate-action rate, and unhandled-message rate. Targets will be validated through testing rather than assumed to be achieved.
