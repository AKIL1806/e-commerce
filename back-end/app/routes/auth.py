from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserCreate, UserOut, UserLogin
from app.models.user import user_table  # Corrected import
from app.database import database
from passlib.context import CryptContext

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/signup", response_model=UserOut)
async def signup(user: UserCreate):
    # Check if user already exists
    query = user_table.select().where(user_table.c.email == user.email)
    existing_user = await database.fetch_one(query)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    # Hash the password
    hashed_password = pwd_context.hash(user.password)

    # Insert new user
    query = user_table.insert().values(email=user.email, password=hashed_password)
    user_id = await database.execute(query)

    return UserOut(id=user_id, email=user.email)
