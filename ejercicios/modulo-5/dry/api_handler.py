# ej-m5-dry/api_handler.py
from utils import parse_user_data

def handle_api_user(data: dict):
    """Procesa un usuario que llega desde la API."""
    
    try:
        user = parse_user_data(data)
    except ValueError as e:
        return {"status": "error", "message": str(e)}
        print(f"API: Procesando usuario '{username}' con email '{email}'")