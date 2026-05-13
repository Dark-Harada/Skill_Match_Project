from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import random

from backend.database import players_collection

app = FastAPI()

# CORS (permite frontend acessar)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Arquivos estáticos
app.mount("/static", StaticFiles(directory="backend/frontend"), name="static")


# HOME
@app.get("/", response_class=HTMLResponse)
def home():
    with open("backend/frontend/index.html", encoding="utf-8") as f:
        return f.read()


# LISTAR JOGADORES
@app.get("/players")
def get_players():

    players = []

    for player in players_collection.find():
        players.append({
            "id": str(player.get("_id", "")),
            "name": player.get("name"),
            "rank": player.get("rank"),
            "winrate": player.get("winrate"),
            "role": player.get("role")
        })

    return players


# CRIAR JOGADOR
@app.post("/players")
def create_player(player: dict):

    # validações básicas
    if "name" not in player or "password" not in player:
        return {"error": "Nome e senha são obrigatórios"}

    # valor padrão
    if "winrate" not in player:
        player["winrate"] = 50

    players_collection.insert_one(player)

    return {"message": "Player criado com sucesso"}


# LOGIN REAL
@app.post("/login")
def login(data: dict):

    name = data.get("name")
    password = data.get("password")

    user = players_collection.find_one({
        "name": name,
        "password": password
    })

    if not user:
        return {"error": "Nome ou senha inválidos"}

    return {
        "message": "Login realizado com sucesso",
        "name": user["name"]
    }


# MATCHMAKING
@app.get("/matchmaking/{player_name}")
def matchmaking(player_name: str):

    user = players_collection.find_one({"name": player_name})

    if not user:
        return {"error": "Usuário não encontrado"}

    others = list(players_collection.find({
        "name": {"$ne": player_name}
    }))

    if len(others) < 4:
        return {"error": "Jogadores insuficientes"}

    team_random = random.sample(others, 4)

    team = [{
        "name": user["name"],
        "rank": user["rank"],
        "winrate": user["winrate"],
        "role": user.get("role", "N/A")
    }]

    for p in team_random:
        team.append({
            "name": p["name"],
            "rank": p["rank"],
            "winrate": p["winrate"],
            "role": p.get("role", "N/A")
        })

    return team