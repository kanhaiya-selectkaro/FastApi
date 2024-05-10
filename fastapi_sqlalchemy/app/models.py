from .database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from fastapi_utils.guid_type import GUID

Base = declarative_base()  # Adjust import path if necessary

class Note(Base):
    __tablename__ = 'notes'
    id = Column(GUID, primary_key=True, default=func.uuid())  # MySQL-specific UUID generation
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    category = Column(String, nullable=True)
    published = Column(Boolean, nullable=False, default=True)
    createdAt = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())


