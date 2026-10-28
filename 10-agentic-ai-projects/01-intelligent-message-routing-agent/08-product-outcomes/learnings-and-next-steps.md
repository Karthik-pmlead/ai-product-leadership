# Learnings and Next Steps

## 1. Key Learnings

### Product Design
- Clear routing rules are essential for consistent message classification.
- Mixed-intent and ambiguous messages need an explicit handling policy.
- Routing unmatched messages to Spam is simple but may misclassify legitimate inquiries.

### Agent Design
- Natural-language instructions guide tool selection but do not guarantee correct or exclusive tool execution.
- Structured output validation could improve consistency and field completeness.
- Prompt-injection scenarios should be included in evaluation.

### Workflow Reliability
- Successful classification does not guarantee a successful Google Sheets write.
- Repeated submissions need testing to identify potential duplicate records.
- Write failures, retries, and recovery behavior should be explicitly evaluated.

### Evaluation
- Expected outcomes must be defined before measuring performance.
- Accuracy targets are hypotheses until validated against executed test cases.
- Misclassifications should be categorized and used to improve routing rules and agent instructions.

## 2. Next Steps

| Priority | Action | Evidence of completion |
|---|---|---|
| P0 | Execute the prepared synthetic test cases | Actual results recorded against expected outcomes |
| P0 | Measure classification and routing accuracy | Completed metrics report with sample size |
| P0 | Test Google Sheets write failures | Documented observed failure behavior |
| P1 | Define policies for ambiguous and mixed-intent messages | Updated routing-decision logic |
| P1 | Test repeated submissions | Duplicate-write behavior documented |
| P1 | Test prompt-injection scenarios | Test outcomes and identified weaknesses recorded |
| P1 | Validate required fields for each destination | Field-completeness results |
| P2 | Assess structured-output validation and retry mechanisms | Documented design decision and implementation status |
| P2 | Review spreadsheet permissions and exported workflow data | Security checklist completed |

## 3. Success Measures

The following are proposed targets, not achieved results:

- Intent classification accuracy: ≥95%
- Routing accuracy: ≥99%
- Required-field completeness: ≥98%
- Duplicate-action rate: 0%
- Unhandled-message rate: 0%

Targets should be reviewed after establishing a baseline from executed tests.

## 4. Iteration Approach

1. **Measure:** Run the test suite and record actual outcomes.
2. **Analyze:** Group failures by classification, routing, extraction, and execution.
3. **Improve:** Update prompts, routing policies, or workflow controls based on evidence.
4. **Re-test:** Run regression tests to detect unintended changes.
5. **Document:** Update the metrics report, error analysis, and implementation status.

## 5. Portfolio Takeaway

This project demonstrates a practical approach to LLM-based intent classification and workflow orchestration using n8n and Google Sheets.

The next stage is to move from a working prototype to an evaluated, more reliable workflow by measuring performance, handling ambiguity explicitly, and validating failure and security behavior.

**Reporting principle:** Clearly distinguish implemented functionality, observed test results, proposed improvements, and unverified capabilities.
