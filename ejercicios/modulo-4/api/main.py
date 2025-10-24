# importar FastAPI y BaseModel de pydantic
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

# Crear una instancia de la app llamada "app"
app = FastAPI()

#crear un modelo pydantic 'User' con username (str) y email (str)
class User(BaseModel):
    username: str
    email: str


# --- ENDPOINTS ---

# crear un endpoint GET en la ruta '/' que devuelva un saludo
@app.get('/')
async def root():
    return {'message': 'Hila, buenvenid@ a la API con Tabnine!'}

# crear un endpoint POST en la ruta '/users/' que acepte 'User' en el cuerpo de la petición y devuelva un mensaje de bienvenida
@app.post('/users/')
async def create_user(user: User):
    return {'message': f'Bienvenido {user.username}!'}

# bloque para ejecutar la app de uvicorn si es el script principal
if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
