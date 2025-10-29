
# Proceso de Testing para `services`

Este documento detalla el proceso de testing llevado a cabo para las funciones dentro del módulo `services`, específicamente para `save_user_to_db`.

## 1. Procedimiento Inicial

El objetivo inicial era verificar la funcionalidad básica de la función `save_user_to_db`. Para ello, se crearon pruebas unitarias utilizando `pytest` con los siguientes propósitos:

-   **Verificar el efecto secundario**: Se utilizó `pytest-mock` para "mockear" la función `print` y asegurar que se llamaba con el mensaje de log esperado al guardar un usuario.
-   **Verificar el valor de retorno**: Se comprobó que la función devolvía exactamente el mismo objeto `User` que se le pasaba como argumento, garantizando la integridad de los datos.

## 2. Resultados y Mejoras

Las pruebas iniciales confirmaron que la función se comportaba como se esperaba en los escenarios básicos. Sin embargo, para mejorar la calidad y robustez del conjunto de pruebas, se implementaron las siguientes mejoras:

-   **Uso de Fixtures (`@pytest.fixture`)**: Se introdujo la fixture `sample_user` para proporcionar una instancia reutilizable del objeto `User`. Esto eliminó la duplicación de código en múltiples pruebas y centralizó la creación de datos de prueba, haciendo el código más limpio y fácil de mantener.

-   **Pruebas Parametrizadas (`@pytest.mark.parametrize`)**:
    -   Se añadió una prueba parametrizada (`test_save_user_with_various_valid_data`) para validar el comportamiento de la función con una variedad de datos de usuario válidos, incluyendo casos extremos como un `username` vacío.
    -   Se creó otra prueba parametrizada (`test_save_user_with_invalid_input_type`) para asegurar que la función maneja correctamente entradas de tipo incorrecto (como `None`, diccionarios o strings), esperando que se lance una excepción `AttributeError`.

Estas mejoras permitieron crear un conjunto de pruebas más completo y robusto, que no solo valida el "camino feliz", sino que también asegura que la función es resistente a diferentes formatos de datos y maneja los errores de forma predecible.
