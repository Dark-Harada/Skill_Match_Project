from database import coaches_db

def get_coaches():
    return coaches_db


def hire_coach(user_id):
    coach = next((c for c in coaches_db if c.user_id == user_id), None)
    return coach