# Introduction to Machine Learning Knowledge Base (IntroML)

Welcome to the **Introduction to Machine Learning Knowledge Base**, a curated collection of foundational ML algorithms, evaluation techniques, and practical implementation patterns. This repository covers essential supervised learning concepts from regression to classification metrics.

This repository is useful for:
- Building intuition for core ML algorithms (linear, logistic, polynomial regression).
- Mastering model evaluation through cross-validation and classification metrics.
- Transitioning from theory to production-ready ML pipelines and model selection.

---

## Table of Contents

| Section | Description | Link |
|---------|-------------|------|
| Notes | Core algorithms (linear/logistic regression, polynomial features, overfitting). | [notes/README.md](notes/README.md) |
| Patterns | ML workflows (preprocessing → train/test split → CV → evaluation → tuning). | [patterns/README.md](patterns/README.md) |
| Projects | End-to-end pipelines (house price prediction, customer churn, spam detection). | [projects/README.md](projects/README.md) |
| Assignments | Implementation challenges (from-scratch regression, CV implementation). | [assignments/README.md](assignments/README.md) |
| Repositories | Links to Scikit-learn examples, Kaggle kernels, MLfromScratch repos. | [repos/README.md](repos/README.md) |
| Videos | StatQuest series, Andrew Ng intro lectures, Sentdex tutorials. | [videos/README.md](videos/README.md) |
| Templates | Boilerplates (regression pipelines, classification workflows, CV utilities). | [templates/README.md](templates/README.md) |
| Interview Prep | Foundational questions (bias-variance, overfitting, metric selection). | [interview-prep/README.md](interview-prep/README.md) |

---

## Quick Start Algorithms

### Regression Progression
Linear Regression → Polynomial Features → Regularization (Ridge/Lasso)

## Essential Workflows

### 1. Complete ML Pipeline

    Data prep → 2. Train/test split → 3. Cross-validation

    Hyperparameter tuning → 5. Model evaluation → 6. Business decision

### 2. Cross-Validation Strategies
K-Fold CV: Split data into K folds, train on K-1, validate on 1
Stratified K-Fold: Preserve class distribution in each fold
Time Series CV: Expanding window or rolling window


### 3. Classification Metrics Framework

Binary: Accuracy, Precision, Recall, F1, AUC-ROC, Log-loss
Imbalanced: PR-AUC, F1-score, Cohen's Kappa
Multi-class: Macro/Micro F1, Confusion Matrix, Log-loss

## Key Algorithms Coverage

Linear Regression:
y = β₀ + β₁x₁ + β₂x₂ + ... + ε
Loss: MSE = (1/n)Σ(y - ŷ)²

Logistic Regression:
p(y=1|x) = 1/(1 + e^(-z)), z = β₀ + β₁x₁ + ...
Loss: Cross-Entropy = -[ylog(p) + (1-y)log(1-p)]

Polynomial Features:
x → [1, x, x², x³, x*x₂, ...] (degree control)

Confusion Matrix Layout:
          Predicted
        P    N
Actual P  TP   FN
       N  FP   TN

## Common Pitfalls & Solutions

Overfitting:

    Symptoms: Great train, poor test performance

    Solutions: Cross-validation, regularization, more data

Data Leakage:

    Problem: Using future info in training

    Solution: Proper train/test splits, Pipeline usage

Imbalanced Classes:

    Techniques: SMOTE, class weights, stratified CV

## Libraries & Tools

Core: Scikit-learn (algorithms, CV, metrics)
Visualization: Matplotlib, Seaborn (residual plots, ROC curves)
Preprocessing: Pandas, Scikit-learn preprocessing
Experiment Tracking: MLflow, Weights & Biases

