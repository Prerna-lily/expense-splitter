from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

load_dotenv()

# Create PostgreSQL engine
engine = create_engine(
    os.getenv(
        "DATABASE_URL",
        "postgresql://" + 
        os.getenv("DB_USER", "postgres") + ":" +
        os.getenv("DB_PASSWORD", "postgres") + "@" +
        os.getenv("DB_HOST", "localhost") + ":" +
        os.getenv("DB_PORT", "5432") + "/" +
        os.getenv("DB_NAME", "expense_splitter")
    ),
    echo=True,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
