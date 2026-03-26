from models.user import User
from models.coach import Coach

users_db = [
    User(id=1, nickname="Player1", rank=3, winrate=55, role="support"),
    User(id=2, nickname="Player2", rank=4, winrate=60, role="dps"),
    User(id=3, nickname="Player3", rank=2, winrate=48, role="tank"),
]

coaches_db = [
    Coach(user_id=2, price=30.0, rating=4.8)
]