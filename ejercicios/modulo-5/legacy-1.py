def get_greeting_legacy(name, age):
    return "Hola, %s. Tienes %d años." % (name, age)

# convierte la misma función get_greeting_legacy a una función moderna utilizando f-strings
def get_greeting_modern(name, age):
    return f"Hola, {name}. Tienes {age} años."