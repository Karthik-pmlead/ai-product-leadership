# Cross-Agent Validation Tests

## 1. Purpose

Validate whether flight, hotel, and activity recommendations form a coherent itinerary when considered together.

The tests focus on the V4 Validator and Summarizer, which reviews consolidated V3 research results.

## 2. Test Approach

Use two types of test execution:

- **Live workflow tests:** Submit travel requests and evaluate actual search results.
- **Controlled validation tests:** Supply representative specialist-agent outputs containing known inconsistencies and assess whether the validator identifies them.

Controlled tests are important because external search results are dynamic and may not reliably reproduce the same conflict.

## 3. Validation Test Cases

| Test ID | Validation area | Test condition | Expected behavior | Severity |
|---|---|---|---|---|
| CV-01 | Flight dates | Flight dates differ from requested trip dates | Identify date mismatch | High |
| CV-02 | Hotel duration | Hotel checkout does not cover intended stay | Identify duration mismatch | High |
| CV-03 | Activity timing | Two activities overlap in time | Identify scheduling conflict | Medium |
| CV-04 | Trip context | Agent recommendation uses a different destination | Flag destination inconsistency | High |
| CV-05 | Hotel location | Hotel location is inconsistent with requested destination | Flag location mismatch | High |
| CV-06 | Recommendation duplication | Same activity appears multiple times | Remove or consolidate duplicates | Medium |
| CV-07 | Budget alignment | Estimated accommodation cost exceeds stated budget | Flag budget concern | Medium |
| CV-08 | Missing information | A recommendation lacks important details | Avoid presenting missing details as verified | Medium |
| CV-09 | Activity feasibility | Activity dates fall outside the trip duration | Identify date conflict | High |
| CV-10 | Final curation | Excessive options are returned | Curate to requested presentation limits | Low |
| CV-11 | Conflicting research | Search sources provide inconsistent information | Surface uncertainty rather than inventing certainty | Medium |
| CV-12 | Partial agent output | One specialist returns incomplete results | Identify incomplete research and avoid unsupported claims | High |

## 4. Detailed Test Scenarios

### CV-01: Flight Date Consistency

**Input:** Original trip dates are December 10–15. Flight results include a return flight on December 17.

**Expected:** Validator identifies the return-date mismatch and does not present the flight as fully aligned with the requested trip.

### CV-02: Hotel Duration Consistency

**Input:** Trip duration is five nights. Hotel result covers only three nights.

**Expected:** Validator identifies the accommodation gap.

### CV-03: Activity Schedule Conflict

**Input:** Two activities are scheduled for the same time on the same day.

**Expected:** Validator identifies the overlap where timing information is available.

### CV-04: Destination Consistency

**Input:** User requests Singapore, but a hotel recommendation is located in Kuala Lumpur.

**Expected:** Validator identifies the destination mismatch.

### CV-05: Budget Alignment

**Input:** User specifies a total trip budget of ₹50,000. Available hotel recommendations alone have an estimated cost of ₹60,000.

**Expected:** Validator flags the budget concern. It should not claim that the overall trip is within budget.

### CV-06: Duplicate Activities

**Input:** The same attraction appears in both local-search and web-research findings.

**Expected:** Duplicate recommendations are consolidated where identifiable.

## 5. Execution and Evidence

For each test, record:

| Field | Description |
|---|---|
| Test ID | Unique test identifier |
| Input fixture | Original trip request and specialist outputs |
| Actual output | Validator response |
| Expected result | Defined test expectation |
| Pass/Fail | Whether expected behavior occurred |
| Defect ID | Reference to error-analysis record |
| Evidence | Execution log or
