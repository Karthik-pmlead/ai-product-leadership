# 01_problem_and_context

This folder defines the business problem, users, assumptions, and constraints for the aspect sentiment use case.

## Purpose

The goal of this folder is to clearly frame the problem before any solution or model design begins. It helps the team agree on what needs to be solved, why it matters, and what boundaries should shape the first version.

## Why this matters

Aspect sentiment analysis is useful only if the business problem is clearly defined. Without a shared problem statement, teams can end up optimizing the model without solving the real business need. [web:125][web:127]

## Folder contents

| File | Purpose |
|---|---|
| [problem-statement](problem-statement.md) | Defines the business problem and desired outcome. |
| [user-research](user-research.md) | Captures who the users are and what they need. |
| [assumptions](assumptions.md) | Lists the beliefs the team is making for the first version. |
| [constraints](constraints.md) | Describes the technical, business, and governance limits. |

## Example use case

The aspect sentiment use case focuses on customer feedback such as reviews, surveys, support tickets, and comments. The system should identify business aspects like delivery, support, pricing, and product quality, then assign sentiment to each aspect. Aspect-based sentiment analysis is especially useful when one comment contains both positive and negative feedback about different parts of the experience. [web:56][web:119]

## Output of this folder

By the end of this folder, the team should agree on:
- what problem is being solved,
- who the users are,
- what is assumed,
- and what limits shape the first version.
