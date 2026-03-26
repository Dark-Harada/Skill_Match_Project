from fastapi import APIRouter
from database import users_db
from services.reputation_service import rate_user

router = APIRouter(prefix="/reputation", tags=["Reputation"])

@router.post("/rate/{user_id}")
def rate(user_id: int, rating: float):
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        return {"error": "User not found"}

    return rate_user(user, rating)