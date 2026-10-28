# Results Summary

## 1. Current Status

The Intelligent Message Routing Agent is a working prototype built with n8n, an LLM, and Google Sheets. It classifies incoming messages and routes them to the Demo, Support, or Spam worksheet.

**Status:** Prototype implemented; 15/15 test cases passed.

## 2. Expected Behavior

| Area | Expected outcome |
|---|---|
| Demo routing | Sales inquiries, pricing questions, and demo requests go to Demo |
| Support routing | Bugs, login problems, billing issues, and help requests go to Support |
| Spam routing | Promotional, irrelevant, and unmatched messages go to Spam under the current prompt |
| Data extraction | Relevant message details are written to the destination sheet |
| Tool selection | The agent is instructed to use one relevant Google Sheets tool |
| Completion response | The agent replies with a short confirmation after the action |

## 3. Evaluation Results

| Evaluation area | Status |
|---|---|
| Test cases prepared | Complete |
| Expected outcomes documented | Complete |
| Test cases executed | 15 |
| Test cases passed | 15 |
| Test cases failed | 0 |
| Test-suite pass rate | 100% |
| Broader routing accuracy | Not established |
| Field completeness | Not independently measured |
| Duplicate-write prevention | Not established |
| Error recovery | Not established |

## 4. Success Criteria

Proposed targets for broader evaluation:

- Intent classification accuracy: ≥95%
- Routing accuracy: ≥99%
- Required-field completeness: ≥98%
- Duplicate-action rate: 0%
- Unhandled-message rate: 0%

These targets are not equivalent to the observed 100% test-suite pass rate.

## 5. Known Limitations

- Unmatched messages currently fall back to Spam, which may misclassify legitimate inquiries.
- Mixed-intent messages need an explicit routing policy.
- Exactly-once execution and duplicate-write prevention have not been established.
- Structured-output validation and robust retry/recovery require verification.
- Security and prompt-injection defenses require further evaluation.

## 6. Next Steps

1. Preserve actual outcomes and execution evidence for all 15 tests.
2. Measure routing accuracy and field completeness separately.
3. Verify duplicate-write behavior and recovery from failed writes.
4. Expand testing with additional representative messages and regression cases.
5. Update reliability claims as further evidence becomes available.

**Portfolio note:** The prototype passed all 15 prepared test cases, demonstrating successful behavior against this test set. Broader reliability and production readiness remain to be established.
