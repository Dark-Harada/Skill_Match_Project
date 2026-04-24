from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="backend/frontend"), name="static")

players = [
    {"id": 1, "name": "Você", "rank": "Platinum", "winrate": 58},
    {"id": 2, "name": "SemNick", "rank": "Gold", "winrate": 52},
    {"id": 3, "name": "Marcão", "rank": "Gold", "winrate": 55},
    {"id": 4, "name": "TiroCerto", "rank": "Platinum", "winrate": 60},
    {"id": 5, "name": "Belinha", "rank": "Gold", "winrate": 57},
    {"id": 6, "name": "ShadowX", "rank": "Diamond", "winrate": 62},
    {"id": 7, "name": "GhostAim", "rank": "Platinum", "winrate": 59},
    {"id": 8, "name": "LunaFPS", "rank": "Gold", "winrate": 54},
]

@app.get("/", response_class=HTMLResponse)
def home():
    with open("backend/frontend/index.html", encoding="utf-8") as f:
        return f.read()


@app.get("/players")
def get_players():
    return players


@app.get("/matchmaking/{user_id}")
def matchmaking(user_id: int):
    user = next((p for p in players if p["id"] == user_id), None)

    if not user:
        return {"error": "User not found"}

    # Remove o próprio usuário da lista
    others = [p for p in players if p["id"] != user_id]

    # Escolhe 4 aleatórios
    team_random = random.sample(others, 4)

    # Usuário sempre primeiro
    team = [user] + team_random

    return team