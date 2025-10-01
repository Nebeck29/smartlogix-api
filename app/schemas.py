from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class StudentCreate(BaseModel):
    nombre: str
    correo: EmailStr

class StudentOut(BaseModel):
    id: int
    nombre: str
    correo: EmailStr
    class Config:
        from_attributes = True

class CourseCreate(BaseModel):
    titulo: str
    descripcion: Optional[str] = None

class CourseOut(BaseModel):
    id: int
    titulo: str
    descripcion: Optional[str] = None
    class Config:
        from_attributes = True

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

class EnrollmentUpdate(BaseModel):
    estado: str = Field(pattern="^(Activo|Inactivo)$")
    puntaje: Optional[int] = None

class EnrollmentOut(BaseModel):
    id: int
    student_id: int
    course_id: int
    estado: str
    puntaje: int
    class Config:
        from_attributes = True
