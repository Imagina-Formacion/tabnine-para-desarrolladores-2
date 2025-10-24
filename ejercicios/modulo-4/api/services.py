# importamos el modelo User desde main.py
from main import User

# función que toma un objeto User y simula guardarlo en BBDD
def save_user_to_db(user: User) -> User:
    # Aquí iría la lógica para guardar el usuario en la base de datos
    print(f"Guardando usuario {user.name} en la base de datos...")
    # Simulamos que el usuario ha sido guardado y retornamos el mismo objeto
    return user

