import re
import random

def sum_even_numbers(numbers: list[int]) -> int:
    """
    Calcula la suma de los números pares en una lista de enteros.

    Args:
        numbers (list[int]): Una lista de números enteros.

    Returns:
        int: La suma de los números pares en la lista.
    """
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    return even_sum

numbers = [random.randint(1, 100) for _ in range(10)]
print(f"La suma de los números pares es: {sum_even_numbers(numbers)}")

def is_valid_email(email: str) -> bool:
    """
    Valida si un string tiene el formato de un correo electrónico válido.

    Args:
        email (str): El correo electrónico a validar.

    Returns:
        bool: True si el formato es válido, False en caso contrario.
    """
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        return False

emails = ['test@example.com', 'test@.com', 'test@example', 'test@example.', 'test@.com@', 'test@.com@.com', 'test@.com@example']
for email in emails:
    print(f"El email '{email}' es válido: {is_valid_email(email)}")

def find_errors_in_log(filepath: str) -> list[str]:
    """
    Lee un archivo de log y devuelve las líneas que contienen la palabra 'error'.

    Args:
        filepath (str): La ruta al archivo de log.

    Returns:
        list[str]: Una lista de líneas que contienen 'error'.
    """
    with open(filepath, 'r') as file:
        lines = file.readlines()
    error = []
    for line in lines:
        if 'error' in line.lower():
            error.append(line.strip())
    return error

filepath = 'ejercicios/modulo-4/debug.log'
print(f"Líneas que contienen la palabra 'error' en '{filepath}':")
for line in find_errors_in_log(filepath):
    print(line)

def get_full_name(first_name: str, last_name: str) -> str:
    """
    Concatena el nombre y el apellido para devolver el nombre completo.

    Args:
        first_name (str): El nombre de la persona.
        last_name (str): El apellido de la persona.

    Returns:
        str: El nombre completo.
    """
    return f"{first_name} {last_name}"