from db import Base
from sqlalchemy import TIMESTAMP, Column, String,Integer, Boolean

class User(Base):
    __tablename__ ='users'

    id = Column(Integer,primary_key=True, index=True)
    username=Column(String(50),unique=True)
    email=Column(String(50))
    fullname=Column(String(50))
    status=Column(String(50))