from fastapi import APIRouter
from database import users_db
from models.user import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def list_users():
    return users_db

@router.post("/")
def create_user(user: User):
    users_db.append(user)
    return user