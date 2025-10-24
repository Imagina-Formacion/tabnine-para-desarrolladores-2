# ej-m5-dry/web_handler.py
from utils import parse_user_data

# ej-m5-dry/web_handler.py
from utils import parse_user_data

def handle_web_user(form_data: dict):
    """Procesa un usuario que llega desde un formulario web."""
    try:
        user = parse_user_data(form_data)
    except ValueError as e:
        # Simplificamos el mensaje de error para la URL
        error_msg = 'invalid_data'
        if 'corto' in str(e):
            error_msg = 'username_corto'
        elif 'inválido' in str(e):
            error_msg = 'email_invalido'
        return {"redirect_to": f"/error?msg={error_msg}"}
    
    print(f"WEB: Procesando usuario '{user.username}' con email '{user.email}'")
    # ...
    # Lógica específica de la web (renderizar plantilla, etc.)...
    # ...
    return {"redirect_to": "/dashboard"}
