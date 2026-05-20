# PRD Canvas

## Product summary
A document extraction system that reads business documents and outputs structured data fields for downstream workflows.

## Product vision
Make document data easy to capture, validate, and reuse without manual re-entry.

## Problem
Users need important fields from documents, but reading and entering them manually is slow and error-prone.

## Target users
- Operations teams.
- Finance teams.
- Legal teams.
- HR teams.
- Support teams.

## Scope
- In scope: document ingestion, field extraction, validation, review, export.
- Out of scope: full document understanding for every possible document type.

## Core extraction elements
- source document.
- target field schema.
- extracted values.
- confidence score.
- review status.

## Success metrics
- field-level accuracy.
- document-level accuracy.
- manual effort saved.
- processing time.
- review rate.

## Assumptions
- Document types are repeatable.
- The field schema is known.
- Business users can review uncertain outputs.

## Constraints
- Formatting may vary.
- Scans may be low quality.
- Sensitive content must be protected.

## Non-goals
- automatic interpretation of all document intent.
- replacing human review for high-risk documents.
