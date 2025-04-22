from fastapi import APIRouter, HTTPException
from passlib.hash import bcrypt
from pydantic import BaseModel
from config import database
from models.user import user_table

router = APIRouter()

class UserIn(BaseModel):
    email: str
    password: str
    mobile: str

@router.post("/signup")
async def signup(user: UserIn):
    existing_user = await database.fetch_one(user_table.select().where(user_table.c.email == user.email))
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_password = bcrypt.hash(user.password)
    query = user_table.insert().values(
        email=user.email,
        password=hashed_password,
        mobile=user.mobile
    )
    await database.execute(query)
    return {"message": "Signup successful"}
