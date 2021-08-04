def get_username(user):
    if "username" in user:
        return user["username"]
    if "name" in user:
        return user["name"]
    if "login" in user:
        return user["login"]
    if "email" in user:
        return user["email"]
    return user["id"]
