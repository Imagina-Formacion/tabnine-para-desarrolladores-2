
import pytest
from ejercicios.modulo_4.api.main import User
from ejercicios.modulo_4.api.services import save_user_to_db

@pytest.fixture
def sample_user():
    """Fixture que proporciona un objeto User de prueba."""
    return User(username='testuser', email='test@example.com')

def test_save_user_to_db_logs_message(mocker, sample_user):
    """
    Prueba que se imprime el mensaje correcto al guardar un usuario.
    Verifica el efecto secundario (logging/print).
    """
    mock_print = mocker.patch('ejercicios.modulo_4.api.services.print')
    
    save_user_to_db(sample_user)
    
    mock_print.assert_called_once_with(f"Guardando usuario {sample_user.username} en la base de datos...")

def test_save_user_to_db_returns_same_object(sample_user):
    """
    Prueba que la función devuelve el mismo objeto de usuario que se le pasó.
    Verifica la integridad del objeto de retorno.
    """
    returned_user = save_user_to_db(sample_user)
    
    assert returned_user is sample_user
    assert returned_user.username == sample_user.username
    assert returned_user.email == sample_user.email

@pytest.mark.parametrize("user_to_save", [
    User(username="john.doe", email="john.doe@example.com"),
    User(username="jane_doe_123", email="jane_doe_123@company.org"),
    User(username="user-with-hyphen", email="test-user@domain.co.uk"),
    User(username="", email="empty_username@test.com") # Caso extremo: username vacío
])
def test_save_user_with_various_valid_data(mocker, user_to_save):
    """
    Prueba la función con múltiples variantes de datos de usuario válidos.
    Asegura que la función es robusta ante diferentes formatos de datos.
    """
    mock_print = mocker.patch('ejercicios.modulo_4.api.services.print')
    
    returned_user = save_user_to_db(user_to_save)
    
    mock_print.assert_called_once_with(f"Guardando usuario {user_to_save.username} en la base de datos...")
    assert returned_user is user_to_save

@pytest.mark.parametrize("invalid_input", [
    None,
    {"username": "test", "email": "test@test.com"},
    "a simple string",
    12345
])
def test_save_user_with_invalid_input_type(invalid_input):
    """
    Prueba que la función lanza un error si el input no es un objeto User.
    Verifica el manejo de tipos de datos incorrectos.
    """
    with pytest.raises(AttributeError):
        save_user_to_db(invalid_input)

# test para save_user_logs_message_with_fixture usando mock y fixture
def test_save_user_logs_message_with_fixture(mocker, sample_user):
    # 1. Configurar el mock para print
    mock_print = mocker.patch("ejercicios.modulo_4.api.services.print")
    # 2. Ejecutar la función con un usuario de prueba
    save_user_to_db(sample_user)

    # 3. Verificar que se llamó a print con el mensaje esperado
    mock_print.assert_called_once_with(f"Guardando usuario {sample_user.username} en la base de datos...")
