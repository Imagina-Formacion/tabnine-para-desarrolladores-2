# Crear una función para realizar operaciones en una aplicación calculadora
def calculator_operations(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation =='subtract':
        return num1 - num2
    elif operation =='multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2!=0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"


