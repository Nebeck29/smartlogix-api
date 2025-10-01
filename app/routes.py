from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from . import crud, schemas

router = APIRouter()

@router.post("/students", response_model=schemas.StudentOut)
def create_student(payload: schemas.StudentCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_student(db, payload)
    except Exception as e:

        raise HTTPException(status_code=400, detail=str(e))

@router.post("/courses", response_model=schemas.CourseOut)
def create_course(payload: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db, payload)

@router.post("/enrollments", response_model=schemas.EnrollmentOut)
def create_enrollment(payload: schemas.EnrollmentCreate, db: Session = Depends(get_db)):
    if not crud.get_student(db, payload.student_id):
        raise HTTPException(status_code=404, detail="Student not found")
    if not crud.get_course(db, payload.course_id):
        raise HTTPException(status_code=404, detail="Course not found")
    return crud.create_enrollment(db, payload)

@router.put("/enrollments/{enrollment_id}", response_model=schemas.EnrollmentOut)
def update_enrollment(enrollment_id: int, payload: schemas.EnrollmentUpdate, db: Session = Depends(get_db)):
    e = crud.update_enrollment(db, enrollment_id, payload)
    if not e:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return e

@router.get("/students/{student_id}/enrollments", response_model=list[schemas.EnrollmentOut])
def list_student_enrollments(student_id: int, db: Session = Depends(get_db)):
    if not crud.get_student(db, student_id):
        raise HTTPException(status_code=404, detail="Student not found")
    return crud.get_enrollments_by_student(db, student_id)
