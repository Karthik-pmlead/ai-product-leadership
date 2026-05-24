# 👤 Face Recognition Attendance System (AI + MLOps MVP)

A lightweight end-to-end **AI-powered biometric attendance system** using face recognition, built with **FastAPI + Streamlit + InsightFace embeddings**, designed to simulate real-world enterprise attendance and identity verification systems.

---

# 🚀 Overview

This project demonstrates a production-style **face recognition pipeline** that can be extended to:

- Employee attendance systems
- Biometric authentication systems
- Access control systems (enterprise / fintech / security)
- Identity verification workflows

It follows a **modular AI system design approach**:
> Image → Face Embedding → Similarity Matching → Decision Engine → Logging

---

# 🧠 Key Features

## 👤 Face Enrollment
- Register employees with image input (upload or camera)
- Generate face embeddings using InsightFace
- Store embeddings locally (pickle / file-based storage)
- Persist metadata in SQLite

---

## 🔐 Face Authentication
- Capture or upload live image
- Extract embedding in real-time
- Compare with stored embeddings using similarity scoring
- Return:
  - Identity match
  - Confidence score
  - Top-K matches (explainability)

---

## 🛡️ Anti-Spoofing (Lightweight MVP)
- Basic heuristics:
  - blur detection
  - brightness validation
  - face presence validation
- Blocks low-quality / invalid inputs

---

## 📊 Metrics Layer
- Total authentications
- Success vs failure rate
- Confidence distribution
- System usage tracking

---

## 🧾 Explainability Layer
- Top-K closest matches shown
- Confidence score transparency
- Decision traceability for each prediction

---

# 🏗️ System Architecture

```text
Streamlit UI
    ↓
FastAPI Backend
    ↓
Face Embedding Model (InsightFace)
    ↓
Embedding Store (Local Files)
    ↓
Similarity Engine (Cosine Similarity)
    ↓
SQLite (Employee + Attendance Logs)
    ↓
Metrics + Explainability Layer
