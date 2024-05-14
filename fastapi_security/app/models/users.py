from sqlalchemy import Column, Integer, String, Boolean
from ..config.db import Base
import re
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.validator import validates

# Import for password hashing (replace with your chosen hashing library)
from passlib.hash import bcrypt


@as_declarative(mapper_class=Base)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    hashed_password = Column(String(128), nullable=False)
    fullname = Column(String(255))
    disabled = Column(Boolean, default=False)

    @validates('email')
    def validate_email(self, value):
        # Replace with your preferred email validation regex
        email_regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.[a-zA-Z]{2,}$"
        if not re.match(email_regex, value):
            raise ValueError("Invalid email format")

    @validates('hashed_password')
    def validate_password_length(self, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")


    def set_password(self, password):
        self.hashed_password = bcrypt.hash(password)

    def verify_password(self, password):
        return bcrypt.verify(password, self.hashed_password)

# Uncomment and call this line only once to create the tables in the database
# user.Base.metadata.create_all(bind=engine) 
