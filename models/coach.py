from pydantic import BaseModel

class Coach(BaseModel):
    user_id: int
    price: float
    rating: float = 5.0