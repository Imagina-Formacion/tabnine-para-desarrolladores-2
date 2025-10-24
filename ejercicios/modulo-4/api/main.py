# importar FastAPI, Basemodel de pydantic y uvicorn para crear la API
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from services import User
from services import save_new_user
from services import edit_user

# crear una instancia de la app llamada 'app'
app = FastAPI()

# --- Endpoints ---
# Endpoint GET en la raíz que devuelva un saludo
@app.get("/")
async def read_root():
    return {"message": "Hola, bienvenido a la API de usuarios con Tabnine!"}

# Endpoint POST para crear un nuevo usuario en '/users/' que acepte un User y lo devuelva
@app.post("/users/")
async def create_user(user: User):
    # Guardar el nuevo usuario en la base de datos
    new_user = save_new_user(user)
    return {"message": "Usuario creado exitosamente", "new_user": new_user}

# Endpoint PUT para editar un usuario en '/users/{username}' que acepte un User y lo devuelva
@app.put("/users/{username}")
async def edited_user(username: str, user: User):
    # Editar el usuario en la base de datos
    edited_user = edit_user(user)
    return {"username": username, "edited_user": edited_user}


# Iniciar la API con uvicorn si es el script principal, y ejecutarlo en 127.0.0.1 en el puerto 8000
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

