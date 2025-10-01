from sqlalchemy.orm import Session
from . import models, schemas

def create_student(db: Session, payload: schemas.StudentCreate):
    s = models.Student(nombre=payload.nombre, correo=payload.correo)
    db.add(s); db.commit(); db.refresh(s)
    return s

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def create_course(db: Session, payload: schemas.CourseCreate):
    c = models.Course(titulo=payload.titulo, descripcion=payload.descripcion)
    db.add(c); db.commit(); db.refresh(c)
    return c

def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()

def create_enrollment(db: Session, payload: schemas.EnrollmentCreate):
    e = models.Enrollment(
        student_id=payload.student_id,
        course_id=payload.course_id,
        estado="Activo",
        puntaje=100
    )
    db.add(e); db.commit(); db.refresh(e)
    return e

def update_enrollment(db: Session, enrollment_id: int, payload: schemas.EnrollmentUpdate):
    e = db.query(models.Enrollment).filter(models.Enrollment.id == enrollment_id).first()
    if not e:
        return None
    if payload.estado is not None:
        e.estado = payload.estado
    if payload.puntaje is not None:
        e.puntaje = payload.puntaje
    db.commit(); db.refresh(e)
    return e

def get_enrollments_by_student(db: Session, student_id: int):
    return db.query(models.Enrollment).filter(models.Enrollment.student_id == student_id).all()
