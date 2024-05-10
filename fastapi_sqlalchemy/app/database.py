from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import pool

# Replace with your MySQL connection details
MYSQL_DATABASE_URL = "mysql+mysqlconnector://root:testing012@127.0.0.1/fastapidb"

# Optional connection pooling configuration (recommended for production)
poolclass = pool.QueuePool
pool_size = 5  # Adjust pool size based on your application's needs
max_overflow = 2  # Limit the number of queued connections

engine = create_engine(
    MYSQL_DATABASE_URL,
    echo=True,  # Enable logging for debugging (remove in production)
    connect_args={"check_same_thread": False},
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


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLITE_DATABASE_URL = ""

engine = create_engine(
    SQLITE_DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
