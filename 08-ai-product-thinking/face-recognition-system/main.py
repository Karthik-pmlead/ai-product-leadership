import os
import uuid
import shutil
from datetime import datetime

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base, Employee, Attendance

from recognition import (
    extract_embedding,
    save_embedding,
    load_embedding,
    compare_embeddings
)

from metrics import log_auth, get_metrics

# =========================================================
# APP INIT
# =========================================================

app = FastAPI(title="Face Recognition Attendance System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# =========================================================
# PATHS
# =========================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

UPLOAD_DIR = os.path.join(BASE_DIR, "data/images")
EMBEDDING_DIR = os.path.join(BASE_DIR, "data/embeddings")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(EMBEDDING_DIR, exist_ok=True)

# =========================================================
# HEALTH
# =========================================================

@app.get("/")
def health():
    return {"status": "running"}

# =========================================================
# ENROLL
# =========================================================

@app.post("/enroll")
def enroll_employee(
    name: str = Form(...),
    employee_id: str = Form(...),
    file: UploadFile = File(...)
):

    db: Session = SessionLocal()

    try:
        image_filename = f"{uuid.uuid4()}.jpg"
        image_path = os.path.join(UPLOAD_DIR, image_filename)

        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        try:
            embedding = extract_embedding(image_path)
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

        embedding_path = os.path.join(
            EMBEDDING_DIR,
            f"{uuid.uuid4()}.pkl"
        )

        save_embedding(embedding, embedding_path)

        employee = Employee(
            name=name,
            employee_id=employee_id,
            image_path=image_path,
            embedding_path=embedding_path
        )

        db.add(employee)
        db.commit()

        return {
            "status": "SUCCESS",
            "message": "Employee enrolled successfully"
        }

    except Exception as e:
        return {"status": "ERROR", "message": str(e)}

    finally:
        db.close()

# =========================================================
# AUTHENTICATE + EXPLAINABILITY
# =========================================================

@app.post("/authenticate")
def authenticate_employee(file: UploadFile = File(...)):

    db: Session = SessionLocal()

    try:
        image_filename = f"auth_{uuid.uuid4()}.jpg"
        image_path = os.path.join(UPLOAD_DIR, image_filename)

        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        try:
            auth_embedding = extract_embedding(image_path)
        except Exception as e:
            return {"status": "ERROR", "message": str(e)}

        employees = db.query(Employee).all()

        if not employees:
            return {"status": "ERROR", "message": "No employees enrolled"}

        candidates = []

        for emp in employees:

            stored_embedding = load_embedding(emp.embedding_path)

            score = compare_embeddings(auth_embedding, stored_embedding)

            candidates.append({
                "employee_id": emp.employee_id,
                "name": emp.name,
                "score": float(score)
            })

        candidates.sort(key=lambda x: x["score"], reverse=True)

        best = candidates[0]
        best_score = best["score"]

        threshold = 0.55

        # SUCCESS
        if best_score >= threshold:

            attendance = Attendance(
                employee_id=best["employee_id"],
                employee_name=best["name"],
                confidence=float(best_score),
                status="SUCCESS",
                timestamp=datetime.utcnow()
            )

            db.add(attendance)
            db.commit()

            log_auth(True, best_score)

            return {
                "status": "SUCCESS",
                "employee_name": best["name"],
                "employee_id": best["employee_id"],
                "confidence": round(best_score * 100, 2),
                "top_matches": candidates[:3]
            }

        # FAILURE
        attendance = Attendance(
            employee_id="UNKNOWN",
            employee_name="UNKNOWN",
            confidence=float(best_score),
            status="FAILED",
            timestamp=datetime.utcnow()
        )

        db.add(attendance)
        db.commit()

        log_auth(False, best_score)

        return {
            "status": "FAILED",
            "message": "No matching employee found",
            "confidence": round(best_score * 100, 2),
            "top_matches": candidates[:3]
        }

    except Exception as e:
        return {"status": "ERROR", "message": str(e), "type": "ANTISPOOF_FAILED"}

    finally:
        db.close()

# =========================================================
# ATTENDANCE
# =========================================================

@app.get("/attendance")
def get_attendance():

    db: Session = SessionLocal()

    try:
        records = db.query(Attendance).order_by(Attendance.id.desc()).all()

        return [
            {
                "id": r.id,
                "employee_id": r.employee_id,
                "employee_name": r.employee_name,
                "confidence": round(r.confidence * 100, 2),
                "status": r.status,
                "timestamp": str(r.timestamp)
            }
            for r in records
        ]

    finally:
        db.close()

# =========================================================
# METRICS
# =========================================================

@app.get("/metrics")
def metrics():
    return get_metrics()
