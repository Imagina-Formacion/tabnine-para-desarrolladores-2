from pydantic import BaseModel  # BaseModel de pydantic

# Crear el modelo Pydantic para los usuarios con username y email
class User(BaseModel):
    username: str
    email: str

#función que toma un objeto User y simula guardarlo en BBDD
def save_new_user(user: User):
    # Simulamos la guardado en BBDD
    print(f"Guardando el usuario: {user.username} con email: {user.email} en la base de datos.")

    return user

# función que simula editar un usuario en BBDD
def edit_user(user: User):
    # Simulamos la edición en BBDD
    print(f"Editando el usuario: {user.username} con email: {user.email} en la base de datos.")

    return user