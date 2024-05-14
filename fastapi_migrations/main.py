from fastapi import FastAPI,HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from db import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Annotated, List
import user

user.Base.metadata.create_all(bind=engine)

app =FastAPI()

origins = [
    "http://127.0.0.1:8000/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(note.router, tags=['Notes'], prefix='/api/notes')

