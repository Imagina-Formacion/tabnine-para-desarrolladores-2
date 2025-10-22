
# Importaciones necesarias para el proyecto.
import os  # Para interactuar con el sistema operativo, como crear carpetas.
import json  # Para trabajar con archivos y datos en formato JSON.
import time  # Para obtener marcas de tiempo (timestamps).
from flask import Flask, request, jsonify, render_template  # Clases y funciones de Flask para crear la aplicación web.
from faker import Faker  # Librería para generar datos falsos (fake data).

# Inicialización de la aplicación Flask.
app = Flask(__name__)
# Inicialización de Faker con localización en español para generar datos más realistas.
fake = Faker('es_ES')

# Nombre de la carpeta donde se guardarán los archivos JSON generados.
DATA_FOLDER = 'data'
# Comprueba si la carpeta de datos no existe y, en ese caso, la crea.
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

@app.route('/')
def index():
    """Ruta principal que renderiza la página de inicio."""
    # Devuelve el archivo 'index.html' que se encuentra en la carpeta 'templates'.
    return render_template('index.html')

@app.route('/generate-users', methods=['POST'])
def generate_users_route():
    """
    Ruta para generar usuarios falsos. Acepta peticiones POST con un JSON
    que especifica la cantidad de usuarios a crear.
    """
    try:
        # Obtiene los datos JSON enviados en la petición POST.
        data = request.get_json()
        # Obtiene el valor de 'count' del JSON, o usa 10 por defecto si no se proporciona.
        # Convierte el valor a entero.
        num_users = int(data.get('count', 10))

        # Valida que el número de usuarios esté en el rango permitido (1 a 20).
        if not 1 <= num_users <= 20:
            # Si no es válido, devuelve un error 400 (Bad Request).
            return jsonify({"error": "El número de usuarios debe estar entre 1 y 20."}), 400

        # Lista para almacenar los diccionarios de usuarios generados.
        users = []
        # Bucle para crear la cantidad de usuarios especificada.
        for _ in range(num_users):
            # Crea un diccionario con datos de usuario falsos.
            user = {
                "nombre": fake.first_name(),
                "apellido": fake.last_name(),
                "email": fake.email(),
                "localidad": fake.city(),
                "fechaDeNacimiento": fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat()
            }
            # Añade el usuario a la lista.
            users.append(user)

        # Genera un timestamp para crear un nombre de archivo único.
        timestamp = int(time.time())
        # Construye la ruta completa del archivo JSON.
        filename = os.path.join(DATA_FOLDER, f'usuarios_{timestamp}.json')
        # Abre el archivo en modo escritura ('w') con codificación UTF-8.
        with open(filename, 'w', encoding='utf-8') as f:
            # Escribe la lista de usuarios en el archivo en formato JSON.
            # 'ensure_ascii=False' permite guardar caracteres como 'ñ' o tildes.
            # 'indent=4' formatea el JSON para que sea legible.
            json.dump(users, f, ensure_ascii=False, indent=4)

        # Devuelve la lista de usuarios generados como respuesta JSON.
        return jsonify(users)

    except (ValueError, TypeError):
        # Captura errores si la entrada no es un número válido.
        return jsonify({"error": "Entrada inválida. Se esperaba un número."}), 400
    except Exception as e:
        # Captura cualquier otro error inesperado en el servidor.
        return jsonify({"error": f"Ha ocurrido un error en el servidor: {e}"}), 500

# Punto de entrada para ejecutar la aplicación.
if __name__ == '__main__':
    # Inicia el servidor de desarrollo de Flask en modo debug.
    # El modo debug permite ver errores detallados y recarga el servidor automáticamente con cada cambio.
    app.run(debug=True)
