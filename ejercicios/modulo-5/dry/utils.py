# función para normalizar los datos del usuario
def normalize_user_data(data):
    # Validación y normalización de datos de usuario
    if 'username' not in data or not data['username']:
        username = 'guest'
    else:
        username = data['username'].strip().lower()
    
    if 'email' in data:
        email = data['email'].strip().lower()
    else:
        email = None

    if len(username) < 3:
        return {"status": "error", "message": "Username demasiado corto"}
    