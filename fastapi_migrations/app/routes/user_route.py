from fastapi import HTTPException, Depends, status, AppRouter
from db import get_db
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Annotated, List
from ..models.user import user

app =AppRouter()

class UserModel(BaseModel):
    username:str
    email:str
    fullname:str
    status:str

db_dependency = Annotated[Session,Depends(get_db)]

@app.get("/")
async def read_Something():
    return "Server Activated"

@app.post("/users",status_code =status.HTTP_201_CREATED)
async def Create_user(users:UserModel,db:db_dependency):
    db_user=user.User(**users.dict())
    db.add(db_user)
    db.commit()
    return users
@app.get("/users/{user_id}",status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id:int,db:db_dependency):
    users = db.query(user.User).filter(user.User.id==user_id).first()
    if users is None:
        raise HTTPException(status_code=404,detail="User not found")
    return users

@app.put("/users/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: int,user_email:str, user_fullname:str,user_status:str, db: db_dependency):
    users = db.query(user.User).filter(user.User.id == user_id).first()
    if users is None:
        raise HTTPException(status_code=404, detail="User not found")

   # Update only provided fields using optional chaining
    if user_id:
        user.email = user_email if user_email else user.email
        user.fullname = user_fullname if user_fullname else user.fullname
        user.status = user_status if user_status else user.status

    db.commit()
    return users

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: db_dependency):
    users = db.query(user.User).filter(user.User.id == user_id).first()
    if users is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(users)
    db.commit()
    return None  # No content to return on successful deletion

@app.get("/users", response_model=List[UserModel])
async def get_all_users(db: db_dependency):
    users = db.query(user.User).all()
    return users

