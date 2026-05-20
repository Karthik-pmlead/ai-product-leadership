# 05_solution_design/fallback-logic.md

# Fallback Logic

## Purpose
Define what happens when the system is uncertain.

## Fallback rules

| Situation | Fallback action |
|---|---|
| No aspect detected | Mark as uncategorized. |
| Multiple aspects found | Return multiple outputs. |
| Low confidence | Route to human review. |
| Conflicting sentiment | Flag for manual review. |
| Unsupported language | Hold for later processing or manual handling. |

## Fallback goal
Prevent overconfident or misleading outputs from reaching business users.

## Principle
A safe fallback is better than a false answer.
