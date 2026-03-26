from fastapi import APIRouter
from database import users_db
from services.vip_service import activate_vip

router = APIRouter(prefix="/vip", tags=["VIP"])

@router.post("/subscribe/{user_id}")
def subscribe(user_id: int):
    user = next((u for u in users_db if u.id == user_id), None)
    if not user:
        return {"error": "User not found"}

    return activate_vip(user)