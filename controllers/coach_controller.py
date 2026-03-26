from fastapi import APIRouter
from services.coach_service import get_coaches, hire_coach

router = APIRouter(prefix="/coach", tags=["Coach"])

@router.get("/")
def list_all():
    return get_coaches()

@router.post("/hire/{user_id}")
def hire(user_id: int):
    coach = hire_coach(user_id)
    if not coach:
        return {"error": "Coach not found"}

    return {"message": f"Coach hired for ${coach.price}"}