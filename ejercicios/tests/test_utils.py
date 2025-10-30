import pytest 
import sys
import os
from ejercicios.modulo_4.utils import is_valid_email

""" # test para sum_even_numbers con una lista de números pares
def test_sum_even_numbers_pares():

    assert sum_even_numbers([2,4,6,8]) == 20

# test para sum_even_numbers con una lista de números impares
def test_sum_even_numbers_impares():

    assert sum_even_numbers([1,3,5,7]) == 0

# test para sum_even_numbers con una lista vacía
def test_sum_even_numbers_vacia():

    assert sum_even_numbers([]) == 0

# test para sum_even_numbers con una lista mixta
def test_sum_even_numbers_mixta():
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12

# test para sum_even_numbers con números negativos
def test_sum_even_numbers_negativos():
    assert sum_even_numbers([-1, -2, -3, -4, -5, -6]) == -12

# test para sum_even_numbers con cero
def test_sum_even_numbers_cero():
    assert sum_even_numbers([0, 1, 2, 3, 4, 5]) == 6 """

# Tests para is_valid_email
@pytest.mark.parametrize("email, expected", [
    ("test@example.com", True),
    ("test.name@example.co.uk", True),
    ("test-name@example.com", True),
    ("test_name@example.com", True),
    ("123@example.com", True),
])
def test_is_valid_email_validos(email, expected):
    """Prueba con correos electrónicos válidos."""
    assert is_valid_email(email) == expected

@pytest.mark.parametrize("email, expected", [
    ("testexample.com", False),
    ("test@", False),
    ("@example.com", False),
    ("test@.com", False),
    ("test@example.", False),
    ("test@example..com", False),
    ("test @example.com", False),
    ("", False),
    ("test@localhost", False),
    (".test@example.com", False),
    ("test.@example.com", False),
    ("..test@example.com", False),
    ("tést@example.com", False),
    ("test$@example.com", False),
    ("test@@example.com", False),
])
def test_is_valid_email_invalidos(email, expected):
    """Prueba con correos electrónicos inválidos."""
    assert is_valid_email(email) == expected