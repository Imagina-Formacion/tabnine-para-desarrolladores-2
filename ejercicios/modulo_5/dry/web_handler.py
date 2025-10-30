# ej-m5-dry/web_handler.py

def handle_web_user(form_data: dict):
    """Procesa un usuario que llega desde un formulario web."""
    
    # --- INICIO DE LÓGICA DUPLICADA ---
    # Validación y normalización de datos de usuario
    if 'username' not in form_data or not form_data['username']:
        username = 'guest'
    else:
        username = form_data['username'].strip().lower()
    
    if 'email' in form_data:
        email = form_data['email'].strip().lower()
    else:
        email = None
    
    if len(username) < 3:
        return {"redirect_to": "/error?msg=username_corto"}
    # --- FIN DE LÓGICA DUPLICADA ---
    
    print(f"WEB: Procesando usuario '{username}' con email '{email}'")
    # ...
    # Lógica específica de la web (renderizar plantilla, etc.)...
    # ...
    return {"redirect_to": "/dashboard"}