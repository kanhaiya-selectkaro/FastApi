from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import pool
from .config import DATABASE_URL

# Optional connection pooling configuration (recommended for production)
poolclass = pool.QueuePool
pool_size = 5  # Adjust pool size based on your application's needs
max_overflow = 2  # Limit the number of queued connections

engine = create_engine(
    DATABASE_URL,
    echo=True,  # Enable logging for debugging (remove in production)
    poolclass=poolclass,
    pool_size=pool_size,
    max_overflow=max_overflow,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

