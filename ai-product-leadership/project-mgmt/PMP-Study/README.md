# PMP / PMBOK Study Repository

This Git‑based repo organizes your PMP‑PMBOK study notes into:
- 10 classic chapters (you can adapt to PMBOK 7/8 later).
- Process‑group domains.
- Templates, MCQs, and case studies.

## Quick navigation table

| Section        | Folder / Description                                                                 |
|----------------|--------------------------------------------------------------------------------------|
| [Chapters](./chapters/) | Chapter‑wise notes (Introduction, Environment, Scope, Schedule, Cost, Quality, Resources, Communications, Risk, Stakeholders). |
| [Domains](./domains/)   | Process‑group views: Initiating, Planning, Executing, Monitoring & Controlling, Closing. |
| [Templates](./templates/) | Reusable artifacts: charters, risk registers, issue logs, WBS, etc. |
| [Quizzes](./quizzes/)   | MCQs by chapter, by domain, and full mock exams. |
| [Case Studies](./case_studies/) | Scenario‑based problems and solutions. |

---
## Repository layout

## Repository layout (list style)

- `README.md`
- `LICENSE`
- `.gitignore`
- `chapters/`
  - `ch01_introduction/`
  - `ch02_environment/`
  - ...
- `domains/`
  - `initiating/`
  - `planning/`
  - ...
- `templates/`
  - `charters/`
  - `project_management_plans/`
  - ...
- `quizzes/`
  - `by_chapter/`
  - `by_domain/`
  - `fake_exams/`
  - `answers/`
- `case_studies/`
  - `agile_scenario_01/`
  - `hybrid_scenario_01/`
  - `templates_used/`
- `books/`
  - `pmbok_guide/`
  - `agile_practice_guide/`
  - `third_party_books/`
- `utils/`
  - `checklist_generator.py`
  - `quick_review.sh`
- `docs/`
  - `index.md`
  - `study_plan_2026.md`


---

## How to use each section

### [Chapters](./chapters/)

Each chapter folder (e.g., `chapters/ch04_scope/`) should contain:

- `summary.md` – one‑page overview of the chapter.
- `processes.md` – key processes, inputs/outputs, tools.
- `cheatsheet.md` – bullet‑style quick‑review points.
- `links.md` – external links (PMI, articles, videos).

Example:  
- `chapters/ch04_scope/summary.md`  
- `chapters/ch10_risk/processes.md`

### [Domains](./domains/)

These mirror process groups:

- `initiating/`, `planning/`, `executing/`, `monitoring_controlling/`, `closing/`.
- Each has:
  - `overview.md` – key concepts and typical KPIs.
  - `process_mapping.md` – links back to relevant chapters.

### [Templates](./templates/)

Each subfolder is a **reusable artifact**:

- Markdown or YAML files, e.g., `templates/charters/project_charter_template.md`.
- Keep them generic so you can adapt for different scenarios.

Use these in `case_studies/` and `quizzes/` to reference real‑world artifacts.

### [Quizzes](./quizzes/)

Organized for flexible revision:

- `by_chapter/` – e.g., `by_chapter/ch04_mcq.md`.
- `by_domain/` – e.g., `by_domain/planning_mcq.md`.
- `fake_exams/` – full mock exams.
- `answers/` – answer keys with explanations.

### [Case Studies](./case_studies/)

Each scenario is a folder:

- `scenario.md` – project narrative and problem.
- `solution.md` – reasoning, selected process, and template used.
- Optional: `reflection.md` – what you’d improve next time.

---

## Naming conventions

- Folders: snake‑case, prefixed with `ch01_`, `ch02_`, etc.  
- Files:  
  - `summary.md`, `processes.md`, `cheatsheet.md`, `scenario.md`, `solution.md`.  
  - MCQs: `by_chapter/ch04_mcq.md`, `by_domain/planning_mcq.md`.

---

## Recommended workflow

1. Edit locally in VS Code / Vim with Git.
2. Commit small, focused changes, e.g.:
   - `git add chapters/ch04_scope/summary.md`
   - `git commit -m "ch04: refine scope definition and WBS notes"`
3. Use branches for content updates and exam‑prep modes.

