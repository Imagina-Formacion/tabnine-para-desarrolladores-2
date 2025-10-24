# Crear un función llamada parse_user_data que exporta los datos validados y normalizados de u usuario.
class User:
    def __init__(self, username: str, email: str):
        self.username = username.strip().lower()
        self.email = email  
        if len(username) < 3:
            raise ValueError('Username demasiado corto')
        if email and not email.endswith('@example.com'):
            raise ValueError('Email inválido')


def parse_user_data(user_data: dict):
    username = user_data.get('username', 'guest')
    email = user_data.get('email', None)

    return User(username, email)


