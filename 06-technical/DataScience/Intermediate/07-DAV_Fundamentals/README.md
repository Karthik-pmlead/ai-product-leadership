# Data Analysis & Visualization Fundamentals Knowledge Base (DAV_Fundamentals)

Welcome to the **DAV Fundamentals Knowledge Base**, a curated collection of essential statistical methods, feature engineering techniques, and core data analysis workflows. This repository covers the foundational building blocks required for robust data analysis and trustworthy insights.

This repository is useful for:
- Mastering hypothesis testing frameworks (t-tests, ANOVA, Chi-Square, non-parametric tests).
- Building production-ready feature engineering pipelines with proper statistical validation.
- Establishing reproducible analysis workflows for business-critical decisions.

---

## Table of Contents

| Section | Description | Link |
|---------|-------------|------|
| Notes | Core statistical tests (t-test, ANOVA, Chi-Square, correlation, non-parametric). | [notes/README.md](notes/README.md) |
| Patterns | Analysis workflows (preprocessing → testing → visualization → interpretation). | [patterns/README.md](patterns/README.md) |
| Projects | Complete analysis pipelines (customer segmentation, A/B testing, quality control). | [projects/README.md](projects/README.md) |
| Assignments | Statistical challenges (power analysis, multiple testing correction, effect sizes). | [assignments/README.md](assignments/README.md) |
| Repositories | Links to Statsmodels, Pingouin, Scikit-posthocs, and analysis toolkits. | [repos/README.md](repos/README.md) |
| Videos | Tutorials on statistical assumptions, test selection, interpretation pitfalls. | [videos/README.md](videos/README.md) |
| Templates | Boilerplates (statistical test frameworks, feature engineering pipelines). | [templates/README.md](templates/README.md) |
| Interview Prep | Fundamental questions (test selection, assumptions, p-value interpretation). | [interview-prep/README.md](interview-prep/README.md) |

---

## Quick Start Libraries

### Statistical Testing Stack
SciPy.stats (t-test, ANOVA, Chi-Square) → Statsmodels (regression diagnostics) → Pingouin (effect sizes)


### Feature Engineering Stack

Pandas (encoding, scaling) → Scikit-learn (preprocessing) → Featuretools (automated FE)

### Test Selection Matrix
Data Type	Groups	Test
Continuous	2	t-test
Continuous	>2	ANOVA
Categorical	Any	Chi-Square
Non-normal	Any	Mann-Whitney/Kruskal-Wallis


### 2. Feature Engineering Pipeline

    Missing values → 2. Encoding (one-hot, target, frequency) → 3. Scaling/normalization

    Feature selection (correlation, mutual info, RFE) → 5. Validation split
    
## Core Test Coverage

Parametric Tests:

    t-test (independent, paired)

    ANOVA (one-way, two-way, repeated measures)

    Pearson correlation

Non-Parametric Tests:

    Mann-Whitney U

    Kruskal-Wallis

    Wilcoxon signed-rank

    Spearman correlation

Categorical Tests:

    Chi-Square (independence, goodness-of-fit)

    Fisher's exact test

    McNemar's test
