from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True)
    name = Column(String)
    image_path = Column(String)
    embedding_path = Column(String)


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String)
    employee_name = Column(String)
    confidence = Column(Float)
    status = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
