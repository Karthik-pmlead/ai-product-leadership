# Unsupervised Learning & Dimensionality Reduction Knowledge Base (UnsupervisedML)

Welcome to the **Unsupervised Learning Knowledge Base**, a curated collection of clustering, anomaly detection, and dimensionality reduction techniques. This repository covers essential algorithms for discovering patterns in unlabeled data and preprocessing high-dimensional datasets.

This repository is useful for:
- Implementing customer segmentation, anomaly detection, and data visualization.
- Understanding clustering evaluation metrics and dimensionality reduction tradeoffs.
- Mastering preprocessing pipelines for deep learning and interpretable analysis.

---

## Table of Contents

| Section | Description | Link |
|---------|-------------|------|
| Notes | Core algorithms (K-means, GMM, hierarchical, PCA, t-SNE, UMAP). | [notes/README.md](notes/README.md) |
| Patterns | Clustering workflows (elbow method, silhouette score, hierarchical dendrograms). | [patterns/README.md](patterns/README.md) |
| Projects | End-to-end applications (customer segmentation, fraud detection, visualization). | [projects/README.md](projects/README.md) |
| Assignments | Implementation challenges (from-scratch K-means, GMM parameter estimation). | [assignments/README.md](assignments/README.md) |
| Repositories | Links to Scikit-learn, HDBSCAN, UMAP-learn, PyClustering. | [repos/README.md](repos/README.md) |
| Videos | StatQuest clustering series, t-SNE/GMM explanations, UMAP webinars. | [videos/README.md](videos/README.md) |
| Templates | Boilerplates (clustering pipelines, dim reduction preprocessing). | [templates/README.md](templates/README.md) |
| Interview Prep | Questions (elbow method, silhouette score, t-SNE limitations). | [interview-prep/README.md](interview-prep/README.md) |

---

## Algorithm Taxonomy Matrix
Clustering:
Density-based ← Distance-based → Model-based
HDBSCAN ← K-means → GMM

Dimensionality Reduction:
Linear ← Non-linear
PCA ← t-SNE/UMAP

### Core Algorithms Coverage
Clustering (Partitioning):

    K-means: Centroid-based, hard assignment

    GMM: Probabilistic soft clustering

Clustering (Hierarchical):

    Agglomerative: Bottom-up merging

    Divisive: Top-down splitting

Anomaly Detection:

    Isolation Forest, One-Class SVM, LOF

Dimensionality Reduction:

    PCA: Linear variance maximization

    t-SNE: Non-linear probability preservation

    UMAP: Topology-preserving manifold learning


---

## Algorithm Comparison Table

| Algorithm | Speed | Scalability | Interpretability | Best For |
|-----------|-------|-------------|------------------|----------|
| K-means | Fast | High | Medium | Spherical clusters |
| GMM | Medium | Medium | High | Elliptical clusters |
| Hierarchical | Slow | Low | High | Dendrogram visualization |
| PCA | Very Fast | High | High | Linear dim reduction |
| t-SNE | Slow | Low | Low | 2D/3D visualization |
| UMAP | Fast | High | Medium | General-purpose reduction |

---

## Cluster Validation Methods

Elbow Method: Plot inertia vs k, find "elbow"
Silhouette Analysis: Average silhouette score per cluster
Gap Statistic: Compare log(W_k) vs expected under null
Dendrogram: Cut height determines number of clusters

text

---

## Common Pitfalls & Solutions

K-means:

    Sensitive to initialization → K-means++

    Assumes spherical clusters → GMM/DBSCAN

t-SNE:

    Non-deterministic → Fix random_state

    Only for visualization → UMAP for general use

    Crowding problem → UMAP/BH-tSNE

PCA:

    Linear only → Kernel PCA/UMAP

    Sensitive to scaling → Always standardize first
