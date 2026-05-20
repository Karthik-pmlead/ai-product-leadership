# 07_eval_and_quality

This folder defines how the aspect sentiment solution will be evaluated and monitored.

## Purpose

The purpose of this folder is to define what “good enough” means for the pilot and how quality will be checked before and after launch.

## Why this matters

Aspect sentiment is useful only if the system can reliably identify aspects, classify sentiment, and surface outputs that users can trust. Human evaluation is especially important when outputs are ambiguous or business-critical. [web:56][web:116][web:119]

## Folder contents

| File | Purpose |
|---|---|
| [eval-plan](eval-plan.md) | Main evaluation plan for the use case. |
| [test-cases](test-cases.md) | Contains representative examples for testing. |
| [acceptance-criteria](acceptance-criteria.md) | Defines what must be true before launch. |
| [red-team-cases](red-team-cases.md) | Contains hard or risky examples to stress test the system. |
| [monitoring-metrics](monitoring-metrics.md) | Tracks quality after deployment. |

## Example use case

For aspect sentiment, evaluation should test whether the system can handle comments with multiple aspects, mixed sentiment, sarcasm, and short noisy feedback. [web:110][web:116]

## Output of this folder

By the end of this folder, the team should know:
- how to test the system,
- what quality threshold is acceptable,
- and how quality will be monitored after launch.
