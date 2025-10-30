#funcion que recibe una lista de productos (diccionarios) y devuelve solo los de la categoría "Electronics". El modelo sera: nombre, precio, categoria
from typing import List, Dict
def filter_electronics_products(products: List[Dict]) -> List[Dict]:
    electronics_products = [product for product in products if product.get("categoria") == "Electronics"]
    return electronics_products

# lista de 10 productos de ejemplo
products = [
    {"nombre": "Laptop", "precio": 1000, "categoria": "Electronics"},
    {"nombre": "Silla", "precio": 150, "categoria": "Furniture"},
    {"nombre": "Smartphone", "precio": 700, "categoria": "Electronics"},
    {"nombre": "Mesa", "precio": 300, "categoria": "Furniture"},
    {"nombre": "Televisor", "precio": 1200, "categoria": "Electronics"},
    {"nombre": "Camiseta", "precio": 20, "categoria": "Clothing"},
    {"nombre": "Auriculares", "precio": 100, "categoria": "Electronics"},
    {"nombre": "Zapatos", "precio": 80, "categoria": "Clothing"},
    {"nombre": "Tablet", "precio": 400, "categoria": "Electronics"},
    {"nombre": "Lámpara", "precio": 60, "categoria": "Furniture"},
]   

# llamada a la funcion con la lista de productos
filtered_products = filter_electronics_products(products)
filtered_products # devuelve solo los productos de la categoría "Electronics"
# Imprime el resultado
print(filtered_products)    
