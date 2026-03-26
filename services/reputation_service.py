def rate_user(user, rating):
    user.reputation_score = (user.reputation_score + rating) / 2
    return user