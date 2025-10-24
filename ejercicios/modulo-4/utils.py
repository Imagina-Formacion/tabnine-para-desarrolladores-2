

def get_full_name(first_name: str, last_name: str) -> str:
    """
    Genera y devuelve el nombre completo de un usuario.

    :param first_name: Nombre del usuario.
    :param last_name: Apellido del usuario.
    :return: Nombre completo del usuario.
    """

    # Valida que el nombre y el apellido no estén vacíos.
    if not first_name or not last_name:
        raise ValueError("Los nombres y apellidos deben ser no vacíos.")
    # Genera y devuelve el nombre completo.
    return f"{first_name} {last_name}"


# Prueba de la función
print(get_full_name("John", "Doe"))  # Output: "John Doe"
print(get_full_name("", "Smith"))  # Raises ValueError: Los nombres y apellidos deben ser no vacíos.
