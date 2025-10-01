## Ejercicio 1
def suma(num1, num2):
    """Devuelve la suma de dos números

    Args:
        num1 (int): Primer número de la suma
        num2 (int): Segundo número de la suma

    Returns:
        int: La suma de num1 con num2

    Example:
    >>> suma(3 + 4) = 7
    """    
    return num1 + num2


X = 10
Y = 20

resultado = suma(X, Y)
print(resultado)


## Ejercicio 2

PI = 3.1416
radio = 5

area = radio * PI ** 2
print(area)


## Ejercicio 3
precio = 10

# Aplica un descuento del 10%
precio_final = precio * 0.9

lista = [1, 2, 3, 4]


## Ejercicio 4

def total_compra(cantidad, precio):
    """Calcula el importe total de la compra

    Args:
        cantidad (int): Cantidad de artículos de un mismo importe
        precio (float): Precio por unidad de artículo

    Returns:
        float: Multiplicación del precio unitario
            por cantidad de artículos
    """
    return cantidad * precio


total = total_compra(3, 12.5)
print(total)


## Ejercicio 5
mensaje = "Este es un mensaje muy " \
    "largo que debería dividirse en varias " \
    "líneas para cumplir con PEP8 y que sea " \
    "más fácil de leer por cualquiera"

resultado = calcular_precio_final(precio_base, # type: ignore
    impuestos,descuento,comision_extra, # type: ignore
    coste_envio, recargo_urgente); # type: ignore


## Ejercicio 6
def convertir(celsius):
    f = (celsius * 9 / 5) + 32
    return f


valores = [0, 10, 20, 30, 40, 100]
for v in valores:
    print(convertir(v))
