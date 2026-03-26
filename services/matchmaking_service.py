from database import users_db

def find_match(user, min_winrate=0):
    results = []
    for player in users_db:
        if player.id == user.id:
            continue

        if abs(player.rank - user.rank) <= 1:
            if user.is_vip:
                if player.winrate >= min_winrate:
                    results.append(player)
            else:
                results.append(player)

    return results