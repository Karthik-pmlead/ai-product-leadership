# Results Summary

## 1. Current Status

The Intelligent Message Routing Agent is a working prototype built with n8n, an LLM, and Google Sheets. It classifies incoming messages and routes them to the Demo, Support, or Spam worksheet.

**Status:** Prototype implemented; evaluation results pending.

## 2. Expected Behavior

| Area | Expected outcome |
|---|---|
| Demo routing | Sales inquiries, pricing questions, and demo requests go to Demo |
| Support routing | Bugs, login problems, billing issues, and help requests go to Support |
| Spam routing | Promotional, irrelevant, and unmatched messages go to Spam under the current prompt |
| Data extraction | Relevant message details are written to the destination sheet |
| Tool selection | The agent is instructed to use one relevant Google Sheets tool |
| Completion response | The agent replies with a short confirmation after the action |

## 3. Evaluation Status

Synthetic test cases have been prepared to evaluate routing, extraction, ambiguity handling, prompt-injection attempts, repeated submissions, and write failures.

| Evaluation area | Status |
|---|---|
| Test-case preparation | Prepared |
| Expected outcomes | Documented |
| Execution against workflow | Pending |
| Routing accuracy | Not yet measured |
| Field completeness | Not yet measured |
| Duplicate-write behavior | Not yet verified |
| Error recovery | Not yet verified |

## 4. Success Criteria

The following are proposed targets, not measured results:

- Intent classification accuracy: ≥95%
- Routing accuracy: ≥99%
- Required-field completeness: ≥98%
- Duplicate-action rate: 0%
- Unhandled-message rate: 0%

## 5. Known Limitations

- Unmatched messages currently fall back to Spam, which may misclassify legitimate inquiries.
- Mixed-intent messages need an explicit routing policy.
- Exactly-once execution and duplicate-write prevention have not been established.
- Structured-output validation and robust retry/recovery require verification.
- Security and prompt-injection defenses require testing.

## 6. Next Steps

1. Execute the prepared test cases against the active workflow.
2. Record actual outcomes and compare them with expected results.
3. Calculate routing accuracy and field completeness from observed results.
4. Document misclassifications, failed writes, and duplicate actions.
5. Update this summary only with verified measurements.

**Portfolio note:** Report this as an implemented workflow prototype with a documented evaluation plan. Do not present proposed targets as achieved results.
