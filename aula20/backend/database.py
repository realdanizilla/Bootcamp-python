# esse arquivo vai criar a conexao com o postgres

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_DATABASE_URL = "postgresql://user:password@postgres/mydatabase"

engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() # ORM

def get_db():
    db = SessionLocal()
    try:
        yield db # yield náo morre a funcao quando ela roda, como um return, posso chamar varias vezes
    finally:
        db.close()