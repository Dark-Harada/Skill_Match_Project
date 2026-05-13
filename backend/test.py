from database import players_collection

players = [
    {
        "name": "Melissa",
        "rank": "Platinum",
        "winrate": 58
    },
    {
        "name": "ShadowX",
        "rank": "Diamond",
        "winrate": 62
    },
    {
        "name": "Belinha",
        "rank": "Gold",
        "winrate": 57
    },
    {
        "name": "GhostAim",
        "rank": "Platinum",
        "winrate": 59
    },
    {
        "name": "LunaFPS",
        "rank": "Gold",
        "winrate": 54
    }
]

players_collection.insert_many(players)

print("Jogadores inseridos com sucesso!")
