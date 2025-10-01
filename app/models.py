from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(150), nullable=False, unique=True, index=True)
    fecha_registro = Column(TIMESTAMP(timezone=False), server_default=func.now())

    enrollments = relationship("Enrollment", back_populates="student", cascade="all, delete-orphan")

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(150), nullable=False)
    descripcion = Column(Text)
    fecha_creacion = Column(TIMESTAMP(timezone=False), server_default=func.now())

    enrollments = relationship("Enrollment", back_populates="course", cascade="all, delete-orphan")

class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    course_id  = Column(Integer, ForeignKey("courses.id", ondelete="CASCADE"))
    estado = Column(String(20), default="Activo")
    puntaje = Column(Integer, default=100)
    fecha_matricula = Column(TIMESTAMP(timezone=False), server_default=func.now())

    student = relationship("Student", back_populates="enrollments")
    course  = relationship("Course",  back_populates="enrollments")
