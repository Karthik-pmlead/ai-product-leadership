# Product Requirements Document (PRD)

## 1. Product Overview
**Product:** Intelligent Message Routing Agent  
**Platform:** n8n, LLM via OpenRouter, Google Sheets

An LLM-powered agent that classifies incoming messages, extracts relevant information, and routes them to the appropriate destination.

## 2. Problem
Manual message triage can delay responses and lead to inconsistent categorization and information capture.

## 3. Goals
- Automate message classification and routing.
- Capture relevant details in structured spreadsheet records.
- Reduce manual triage effort.
- Evaluate routing accuracy and workflow reliability.

## 4. Functional Requirements

| ID | Requirement |
|---|---|
| FR1 | Receive incoming messages through the chat trigger. |
| FR2 | Classify messages as Demo, Support, or Spam. |
| FR3 | Extract relevant fields for the selected category. |
| FR4 | Append records to the corresponding Google Sheets tab. |
| FR5 | Return a completion response after the action. |

## 5. Non-Functional Requirements
- Consistent classification and field extraction.
- Secure handling of credentials and message data.
- Observable failures and testable workflow behavior.
- Protection against unintended duplicate writes.

*These requirements are goals; not all are verified in the current prototype.*

## 6. Success Metrics
Proposed targets, pending evaluation:
- Classification accuracy: ≥95%
- Routing accuracy: ≥99%
- Required-field completeness: ≥98%
- Duplicate-action rate: 0%
- Unhandled-message rate: 0%

## 7. Out of Scope
- CRM or ticketing-system integration.
- Automated replies to customers beyond workflow confirmation.
- Production-grade monitoring and compliance certification.

## 8. Acceptance Criteria
- Representative messages route to the expected destination.
- Required fields are correctly populated.
- Ambiguous messages and write failures are tested.
- Actual results are recorded against expected outcomes before performance claims are made.
