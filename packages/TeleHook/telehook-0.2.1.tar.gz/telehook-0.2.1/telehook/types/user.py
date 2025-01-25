# Users


class User:
    def __init__(self, user_data):
        self.id = user_data.get('id')
        self.first_name = user_data.get('first_name')
        self.last_name = user_data.get('last_name', None)
        self.username = user_data.get('username', None)

    def __str__(self):
        return f"User(id={self.id}, username='{self.username}', first_name='{self.first_name}')"
