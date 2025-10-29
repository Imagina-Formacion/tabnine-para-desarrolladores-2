# función que toma una lista de números y devuelve la suma de los números pares
import re # Tabnine puede incluso sugerir esta importación

# función que toma un string de email y valida si es un formato de email válido usando regex
def is_valid_email(email: str) -> bool:
    # Agrega validación para cuando el nombre o dominio tengan puntos consecutivos
    # Expresión regular mejorada para validar el formato del email, evitando puntos consecutivos,
    # y que no empiece o termine con punto antes del @.
    pattern = r"^[a-zA-Z0-9_+-]+(\.[a-zA-Z0-9_+-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return True
    else:
        return False