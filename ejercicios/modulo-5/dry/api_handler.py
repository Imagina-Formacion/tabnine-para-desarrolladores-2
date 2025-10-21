# ej-m5-dry/api_handler.py

def handle_api_user(data: dict):
    """Procesa un usuario que llega desde la API."""
    
    # --- INICIO DE LÓGICA DUPLICADA ---
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
    # --- FIN DE LÓGICA DUPLICADA ---
    
    print(f"API: Procesando usuario '{username}' con email '{email}'")
    # ...
    # Lógica específica de la API...
    # ...
    return {"status": "success", "user": username}