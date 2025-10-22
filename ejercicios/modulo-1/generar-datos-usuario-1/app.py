from flask import Flask, jsonify, render_template
from faker import Faker
import random

app = Flask(__name__)
fake = Faker('es_ES') # Use Spanish localization for more relevant data

@app.route('/')
def index():
    """Renders the main page."""
    return render_template('index.html')

@app.route('/generate-users')
def generate_users():
    """Generates and returns a list of 10 random users."""
    users = []
    for _ in range(10):
        user = {
            "nombre": fake.first_name(),
            "apellido": fake.last_name(),
            "email": fake.email(),
            "localidad": fake.city(),
            "fechaDeNacimiento": fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat()
        }
        users.append(user)
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)