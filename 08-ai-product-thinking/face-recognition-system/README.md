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
```

# ⚙️ Tech Stack

| Layer             | Technology                             |
| ----------------- | -------------------------------------- |
| Frontend          | Streamlit                              |
| Backend           | FastAPI                                |
| ML Model          | InsightFace (Face Embeddings)          |
| Similarity Search | Cosine Similarity (FAISS-ready design) |
| Database          | SQLite                                 |
| Storage           | Local filesystem                       |
| Language          | Python                                 |

# 🔁 System Workflow

1. Enrollment Flow
   - User Image → Face Detection → Embedding Generation → Store in DB

2. Authentication Flow
    - Live Image → Embedding → Compare with DB → Match Found → Mark Attendance

3. Decision Flow
    - Similarity Score → Threshold Check → Success / Failure → Logging
  
# 📈 Metrics Tracked

1. Authentication success rate
2. Average confidence score
3. Failure rate (spoof / mismatch)
4. Employee recognition frequency

# 🧠 Design Highlights

🔹 Embedding-based architecture
Enables scalable identity matching without retraining models

🔹 Modular ML pipeline
Easy to replace similarity engine with FAISS / vector DB

🔹 Explainable AI outputs
Top-K similarity matches improve trust and debugging

🔹 API-first design
FastAPI enables production-grade extensibility

# ⚠️ Limitations (MVP Scope)
  - Uses linear similarity search (not FAISS yet)
  - Lightweight heuristic anti-spoofing only
  - No distributed storage layer
  - No GPU optimization / batching
  - Single-camera input only

# 🚀 Future Improvements

## 🧠 ML Enhancements

  1. FAISS-based vector search
  2. Deep liveness detection model
  3. Multi-face tracking
     
# 🏗️ System Enhancements

  1. Kafka-based event logging
  2. Cloud storage (S3 / GCS)
  3. Microservice decomposition
  4. 📡 Real-time Capabilities
  5. Video stream authentication
  6. Multi-camera support
  7. Edge deployment (Jetson / mobile)

# 🎯 Business Use Cases
  1. Corporate attendance systems
  2. Secure office access control
  3. Banking / fintech identity verification
  4. Airport passenger authentication (conceptual extension)

# 🧑‍💻 How to Run

#### Install dependencies
```
pip install -r requirements.txt
```
#### Start backend
```
uvicorn main:app --reload
```
#### Start frontend
```
streamlit run streamlit_app.py
```

# 🎥 Demo

This demo shows the full end-to-end flow of the system:
  - Employee enrollment via image upload / camera
  - Embedding generation using InsightFace
  - Real-time authentication against stored embeddings
  - Attendance logging with confidence score
  - Explainable top-K match visualization
    
  👉 Watch demo here: [Face Recognition Demo](https://drive.google.com/file/d/1XPPhIGygHuuv1DJTwd2UAVQDJkVUyq6B/view?usp=drive_link)

# 📌 Project Summary

This project demonstrates a real-world biometric AI system design, combining:

  - Computer Vision (Face Recognition)
  - Backend Engineering (FastAPI)
  - Product UI (Streamlit)
  - Lightweight MLOps thinking
  - Explainable AI design
