from fastapi import APIRouter
from database import users_db
from services.matchmaking_service import find_match

router = APIRouter(prefix="/matchmaking", tags=["Matchmaking"])

@router.get("/{user_id}")
def matchmaking(user_id: int, min_winrate: float = 0):
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        return {"error": "User not found"}

    return find_match(user, min_winrate)