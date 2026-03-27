# Mathematics for Machine Learning Knowledge Base (MathsML)

Welcome to the **Mathematics for Machine Learning Knowledge Base**, a curated collection of essential mathematical foundations powering modern ML algorithms. This repository demystifies the math behind data science, from linear algebra fundamentals to optimization theory.

This repository is useful for:
- Understanding the mathematical intuition behind ML algorithms and neural networks.
- Implementing optimization algorithms from scratch (gradient descent, PCA).
- Excelling in ML interviews requiring mathematical derivations and proofs.

---

## Table of Contents

| Section | Description | Link |
|---------|-------------|------|
| Notes | Core concepts (vectors, matrices, loss functions, gradients, eigenvalues). | [notes/README.md](notes/README.md) |
| Patterns | Optimization workflows (convexity, convergence proofs, regularization). | [patterns/README.md](patterns/README.md) |
| Projects | From-scratch implementations (PCA, gradient descent, SVD, neural net forward pass). | [projects/README.md](projects/README.md) |
| Assignments | Mathematical challenges (matrix decompositions, optimization proofs, derivations). | [assignments/README.md](assignments/README.md) |
| Repositories | Links to NumPy, SciPy, JAX, and mathematical computing projects. | [repos/README.md](repos/README.md) |
| Videos | 3Blue1Brown series, Andrew Ng lectures, fast.ai math lessons. | [videos/README.md](videos/README.md) |
| Templates | Boilerplates (optimization loops, linear algebra utilities, loss functions). | [templates/README.md](templates/README.md) |
| Interview Prep | ML math questions (matrix calculus, PCA derivation, convexity proofs). | [interview-prep/README.md](interview-prep/README.md) |

---

## Quick Start Matrix

### Linear Algebra Stack
Vectors → Matrices → Eigenvalues → SVD → PCA → Neural Network layers


### Optimization Stack

Loss Function → Gradient → Gradient Descent → Momentum → Adam → Constraint Opt


### Core Concepts Coverage

Linear Algebra (40% ML):

    Vector spaces, basis, span, linear independence

    Matrix operations, inverses, determinants

    Eigenvalues/eigenvectors, spectral theorem

    SVD, QR decomposition, matrix factorization

Calculus for ML (30%):

    Partial derivatives, gradients, Hessians

    Chain rule for backpropagation

    Taylor series for optimization analysis

Optimization (30%):

    Convexity, local/global minima

    Gradient descent variants

    Constraint optimization (Lagrange multipliers)

    Stochastic gradient descent

  ## Essential Workflows

### 1. PCA Mathematical Pipeline

    Center data → 2. Covariance matrix → 3. Eigen decomposition

    Select top-k eigenvectors → 5. Project data → 6. Explained variance


### 2. Gradient Descent Framework

θ_new = θ_old - α * ∇J(θ)
Where: α = learning rate, ∇J = gradient of loss


### 3. Loss Function Taxonomy

Regression: MSE, MAE, Huber loss, Quantile loss
Classification: Cross-entropy, Hinge loss, Focal loss
Regularization: L1 (Lasso), L2 (Ridge), Dropout

## Mathematical Implementation Patterns

Matrix Operations:
# Forward pass: y = Xw + b
# Gradient: dL/dw = X^T * dL/dy
# Update: w = w - α * dL/dw

PCA from Scratch:
cov_matrix = X.T @ X / n_samples
eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
top_k = eigenvectors[:,-k:]
X_pca = X @ top_k

Gradient Descent Loop:
while not converged:
    grad = compute_gradient(params, data)
    params -= learning_rate * grad
    loss = compute_loss(params, data)

while not converged:
    grad = compute_gradient(params, data)
    params -= learning_rate * grad
    loss = compute_loss(params, data)
