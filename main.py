from fastapi import FastAPI
from controllers import users_controller, matchmaking_controller, vip_controller, coach_controller, reputation_controller

app = FastAPI(title="Competitive Matchmaking MVP")

app.include_router(users_controller.router)
app.include_router(matchmaking_controller.router)
app.include_router(vip_controller.router)
app.include_router(coach_controller.router)
app.include_router(reputation_controller.router)