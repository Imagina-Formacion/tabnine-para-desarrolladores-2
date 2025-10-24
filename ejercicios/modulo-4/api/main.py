# importar FastAPI, Basemodel de pydantic y uvicorn para crear la API
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# crear una instancia de la app llamada 'app'
app = FastAPI()

# Crear el modelo Pydantic para los usuarios con username y email
class User(BaseModel):
    username: str
    email: str

# --- Endpoints ---
# Endpoint GET en la raíz que devuelva un saludo
@app.get("/")
async def read_root():
    return {"message": "Hola, bienvenido a la API de usuarios con Tabnine!"}

# Endpoint POST para crear un nuevo usuario en '/users/' que acepte un User y lo devuelva
@app.post("/users/")
async def create_user(user: User):
    return {"message": f"Usuario '{user.username}' creado con éxito!  Email: {user.email}"}

# Iniciar la API con uvicorn si es el script principal, y ejecutarlo en 127.0.0.1 en el puerto 8000
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

