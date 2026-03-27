# Supervised Learning Algorithms Knowledge Base (SupervisedAlgos)

Welcome to the **Supervised Learning Algorithms Knowledge Base**, a curated collection of intermediate ML algorithms, ensemble methods, and tree-based techniques. This repository covers KNN, Decision Trees, Bagging, Boosting, SVM, Naive Bayes, and ensemble strategies for production ML systems.

This repository is useful for:
- Understanding tree-based models, ensemble methods, and kernel methods.
- Implementing bagging/boosting from scratch and model blending strategies.
- Mastering model selection and hyperparameter tuning for Kaggle competitions.

---

## Table of Contents

| Section | Description | Link |
|---------|-------------|------|
| Notes | Core algorithms (KNN, DT, ensembles, SVM kernels, Naive Bayes). | [notes/README.md](notes/README.md) |
| Patterns | Ensemble workflows (stacking, blending, early stopping). | [patterns/README.md](patterns/README.md) |
| Projects | End-to-end competitions (Kaggle tabular, customer propensity). | [projects/README.md](projects/README.md) |
| Assignments | Implementation challenges (from-scratch DT, boosting rounds). | [assignments/README.md](assignments/README.md) |
| Repositories | Links to XGBoost, LightGBM, CatBoost, scikit-learn contrib. | [repos/README.md](repos/README.md) |
| Videos | StatQuest trees/boosting, CampusX Hindi series, Kaggle Grandmaster talks. | [videos/README.md](videos/README.md) |
| Templates | Boilerplates (ensemble pipelines, hyperparameter grids). | [templates/README.md](templates/README.md) |
| Interview Prep | Algorithm questions (tree splits, boosting math, SVM dual). | [interview-prep/README.md](interview-prep/README.md) |

---

## Algorithm Progression Matrix
Instance-based → Tree-based → Ensemble → Kernel Methods
KNN → Decision Tree → Bagging/RF → Boosting → SVM

### Core Algorithms Coverage
Instance-based:

    KNN (k-Nearest Neighbors): Distance-weighted prediction

Tree-based:

    Decision Tree: Greedy splits (Gini/Entropy)

    Random Forest: Bagging + feature randomness

Ensemble Methods:

    Bagging: Bootstrap aggregation (variance reduction)

    Boosting: Sequential error correction (bias reduction)

    Stacking: Meta-learner on base predictions

Probabilistic:

    Naive Bayes: Independence assumption, fast baseline

Kernel Methods:

    SVM: Maximum margin + kernel trick (RBF, Polynomial)

## Essential Workflows

### 1. Ensemble Pipeline

    Base models → 2. Cross-validation predictions → 3. Meta-features

    Stacking → 5. Blending → 6. Model averaging


### 2. Tree-Based Hyperparameter Tuning

Decision Tree: max_depth, min_samples_split, min_samples_leaf
Random Forest: n_estimators, max_features, bootstrap
Gradient Boosting: learning_rate, n_estimators, subsample, colsample_bytree


### 3. Boosting Stages

Round 1: Fit to original data
Round 2: Fit to residuals/errors of Round 1
...
Final: Weighted sum of all trees


---

## Algorithm Comparison Table

| Algorithm | Speed | Interpretability | Overfitting Risk | Best For |
|-----------|-------|------------------|------------------|----------|
| KNN | Slow | Low | High | Small datasets |
| Decision Tree | Fast | High | Very High | Feature importance |
| Random Forest | Medium | Medium | Low | Tabular data |
| XGBoost/LGBM | Medium | Medium | Low | Competitions |
| Naive Bayes | Very Fast | High | Low | Text classification |
| SVM | Slow | Low | Medium | Small, separable data |

---

## Key Implementation Patterns
KNN with Distance Weighting:

python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5, weights='distance')

Random Forest Feature Importance:

python
rf = RandomForestClassifier(n_estimators=100, max_features='sqrt')
rf.fit(X, y)
importances = rf.feature_importances_

XGBoost Early Stopping:

python
xgb = XGBClassifier(n_estimators=1000, learning_rate=0.1)
xgb.fit(X_train, y_train, 
        eval_set=[(X_val, y_val)], 
        early_stopping_rounds=50, verbose=False)

SVM Kernel Comparison:

python
from sklearn.svm import SVC
kernels = ['linear', 'poly', 'rbf', 'sigmoid']
for kernel in kernels:
    svm = SVC(kernel=kernel, C=1.0, gamma='scale')
    scores = cross_val_score(svm, X, y, cv=5)

Naive Bayes Pipeline:

python
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.pipeline import Pipeline
pipe = Pipeline([('nb', GaussianNB()), ('scale', StandardScaler())])


---

## Mathematical Foundations

Decision Tree Split Criteria:
Gini: 1 - Σp_i²
Entropy: -Σp_i*log(p_i)

SVM Optimization:
min(1/2||w||² + CΣξ_i)
s.t. y_i(w·x_i + b) ≥ 1 - ξ_i

AdaBoost Weights Update:
w_{t+1,i} = w_{t,i} * exp(α_t * I(y_i ≠ h_t(x_i)))

## Ensemble Techniques Coverage

Bagging (Bootstrap AGGregatING):

    Random subsets with replacement

    Parallel training

    Variance reduction

Boosting Variants:

    AdaBoost: Reweight misclassified samples

    Gradient Boosting: Fit to negative gradient

    XGBoost: Regularized GBM + histogram optimization

Advanced Ensembling:

    Stacking: CV predictions → meta-model

    Blending: Holdout predictions → linear weights

## Hyperparameter Tuning Guide

Grid Search: Exhaustive (slow)
Random Search: Sample space (faster)
Bayesian Opt: Gaussian processes (smart)
Optuna/Hyperopt: Production-grade automation

## Common Pitfalls & Solutions

KNN:

    Curse of dimensionality → Feature selection

    Slow prediction → KD-tree/Ball-tree

Decision Trees:

    Overfitting → Pruning, min_samples_leaf

    Unstable splits → Random Forest

Boosting:

    Overfitting → Early stopping, learning_rate

    Slow training → Histogram binning (LightGBM)

SVM:

    Memory intensive → LinearSVC, SGDClassifier

## Libraries & Tools

Trees/Ensembles: Scikit-learn, XGBoost, LightGBM, CatBoost
KNN/SVM: Scikit-learn, Faiss (fast KNN)
Naive Bayes: Scikit-learn
Tuning: Optuna, Hyperopt, Ray Tune
Feature Importance: SHAP, LIME
