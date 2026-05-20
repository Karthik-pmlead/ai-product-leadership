# 06_data_and_risk

This folder captures the data requirements and risk controls for the aspect sentiment use case.

## Purpose

The purpose of this folder is to define what data the system needs, how data quality will be handled, and what risks must be managed before and during development.

## Why this matters

Aspect sentiment depends heavily on text quality, taxonomy consistency, and safe handling of customer feedback. The solution is only as good as the data and the safeguards around it. [web:56][web:119][web:121]

## Folder contents

| File | Purpose |
|---|---|
| [data-inventory](data-inventory.md) | Lists data sources and fields. |
| [data-quality](data-quality.md) | Defines checks for data completeness and consistency. |
| [privacy-and-security](privacy-and-security.md) | Describes how customer data will be protected. |
| [bias-and-fairness](bias-and-fairness.md) | Identifies fairness risks and mitigations. |
| [risk-register](risk-register.md) | Tracks risks, impact, likelihood, and mitigation. |

## Example use case

For aspect sentiment, the main data sources are usually surveys, reviews, support tickets, and chat transcripts, all of which can contain noisy but valuable feedback. [web:56][web:119]

## Output of this folder

By the end of this folder, the team should have:
- a clear data inventory,
- a usable pilot dataset,
- and a risk list with mitigation actions.
