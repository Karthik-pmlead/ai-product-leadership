# Time Series & Recommender Systems Knowledge Base (TS_RS)

Welcome to the **Time Series & Recommender Systems Knowledge Base**, a curated collection of algorithms and patterns for sequential data analysis and personalized recommendations. Covers forecasting, anomaly detection, collaborative filtering, and hybrid recommenders.

This repository is useful for:
- Building production time series forecasting pipelines and recommendation engines.
- Implementing ARIMA, Prophet, and deep learning sequence models.
- Mastering evaluation metrics for ranking and sequential prediction tasks.

---

## Table of Contents

| Section | Description | Link |
|---------|-------------|------|
| Notes | ARIMA/SARIMA, Prophet, RNN/LSTM, Collaborative Filtering | [notes/README.md](notes/README.md) |
| Patterns | Cross-validation, stationarity tests, cold-start solutions | [patterns/README.md](patterns/README.md) |
| Projects | Stock prediction, sales forecasting, movie recommendations | [projects/README.md](projects/README.md) |
| Assignments | From-scratch ARIMA, matrix factorization | [assignments/README.md](assignments/README.md) |
| Repositories | Prophet, Surprise, TensorFlow Recommenders | [repos/README.md](repos/README.md) |
| Videos | StatQuest time series, Deep learning recsys | [videos/README.md](videos/README.md) |
| Templates | Forecasting pipelines, recommender boilerplates | [templates/README.md](templates/README.md) |
| Interview Prep | ACF/PACF interpretation, ALS vs Neural CF | [interview-prep/README.md](interview-prep/README.md) |

---

## Quick Start Matrix

## Core Coverage

Time Series:

    Stationarity (ADF test, differencing)

    ARIMA/SARIMA (p,d,q parameters)

    Exponential Smoothing

    Prophet (trend + seasonality + holidays)

    LSTM/GRU/Transformer

Recommender Systems:

    Collaborative Filtering (User/User, Item/Item)

    Matrix Factorization (SVD, NMF, ALS)

    Content-Based Filtering

    Hybrid Models

    Deep Learning (Neural CF, Autoencoders)

## Essential Metrics

Time Series:
MAE, RMSE, MAPE, MASE, sMAPE

Recommenders:
Precision@K, Recall@K, NDCG@K, MAP@K, Coverage, Serendipity

## Key Patterns

Time Series Pipeline:

    Stationarity test → 2. Decomposition → 3. Model selection

    Cross-validation (expanding window) → 5. Ensemble forecasts

Recommender Pipeline:

    Data prep (implicit/explicit) → 2. Split (temporal)

    Model train → 4. Ranking → 5. Evaluation @K

## Libraries

Time Series: statsmodels, Prophet, Darts, sktime
Recommenders: Surprise, Implicit, LightFM, TensorFlow Recommenders
Deep Learning: PyTorch Forecasting, Merlion
