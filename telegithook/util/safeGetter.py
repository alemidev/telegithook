def get_username(user):
    if 'username' in user:
        return user['username']
    return f"<a href={user['email']}>{user['name']}</a>"
