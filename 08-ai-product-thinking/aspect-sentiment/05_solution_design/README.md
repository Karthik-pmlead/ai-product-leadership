# 05_solution_design

This folder defines how the aspect sentiment solution should work from a product and technical perspective.

## Purpose

The purpose of this folder is to convert the product definition into a concrete solution approach. It explains the architecture, model choice, input-output contracts, human review logic, and fallback behavior.

## Why this matters

Aspect sentiment is a fine-grained text problem, so the team needs to be clear about what the system will do, how it will do it, and what should happen when confidence is low. [web:56][web:101][web:112]

## Folder contents

| File | Purpose |
|---|---|
| [sol-arch](sol-arch.md) | Defines the solution architecture end to end. |
| [model-sel-rationale](model-sel-rationale.md) | Explains why a specific model approach is chosen. |
| [input-output-contracts](input-output-contracts.md) | Defines the input schema and expected output schema. |
| [human-in-the-loop](human-in-the-loop.md) | Describes when humans should review system outputs. |
| [fallback-logic](fallback-logic.md) | Describes what happens when the system is uncertain. |
| [architecture-notes](architecture-notes.md) | Stores additional design decisions and future improvements. |

## Example use case

For aspect sentiment, the solution usually splits the problem into aspect detection and sentiment classification, then routes uncertain outputs to human review. [web:101][web:104][web:110]

## Output of this folder

By the end of this folder, the team should have:
- a clear solution architecture,
- a model choice rationale,
- defined input and output contracts,
- and fallback behavior for low-confidence cases.
