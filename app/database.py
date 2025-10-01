import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_USER = os.getenv("DB_USER", "apiuser")
DB_PASS = os.getenv("DB_PASS", "Nebeck#2001")
DB_NAME = os.getenv("DB_NAME", "smartlogix")
DB_HOST = os.getenv("DB_HOST", "/cloudsql/gen-lang-client-0127419199:us-central1:smartlogix-sql")
DB_PORT = os.getenv("DB_PORT", "5432")

def build_db_url() -> str:
    """
    Construye la URL de conexión a la base de datos.
    - En Cloud Run ↔ Cloud SQL (UNIX socket):
      postgresql+psycopg2://USER:PASSWORD@/DBNAME?host=/cloudsql/PROJECT:REGION:INSTANCE

    - En local (VS Code con IP pública):
      postgresql+psycopg2://USER:PASSWORD@HOST:PORT/DBNAME
    """
    if DB_HOST.startswith("/cloudsql/"):

        return f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@/{DB_NAME}?host={DB_HOST}"

    return f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


DATABASE_URL = build_db_url()


engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  
    pool_size=5,          
    max_overflow=10,      
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
