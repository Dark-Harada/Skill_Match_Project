from pydantic import BaseModel

class User(BaseModel):
    id: int
    nickname: str
    rank: int
    winrate: float
    role: str
    is_vip: bool = False
    reputation_score: float = 5.0