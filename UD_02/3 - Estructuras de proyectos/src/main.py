"""
Módulo principal de Calculadora de Recetas.
Descripción:
    Lee un archivo CSV de recetas e imprime ingredientes de una receta dada.
Uso:
    python src/main.py

Autor: Mario
Fecha: 2025-08-13
"""

import sys
import csv
from pathlib import Path

# TODO: validar número de comensales > 0 cuando se añada esa funcionalidad
# FIXME: si el archivo CSV no existe, ahora mismo lanzará FileNotFoundError (gestionar try/except)
# Nota: usamos csv.DictReader por legibilidad; no es óptimo para archivos gigantes

DATA_FILE = Path("data/recetas.csv")


def listar_ingredientes(receta: str) -> list[dict]:
    """
    Devuelve una lista de diccionarios con los ingredientes de una receta específica.

    Parámetros:
        receta (str): Nombre de la receta (ej. "tortilla").

    Retorna:
        list[dict]: Lista de filas con claves: receta, ingrediente, cantidad_unidad, unidad.

    Ejemplo (doctest):
        >>> filas = listar_ingredientes("tortilla")
        >>> isinstance(filas, list)
        True
        >>> set(filas[0].keys()) >= {"receta", "ingrediente", "cantidad_unidad", "unidad"}
        True
    """

    ingredientes = []
    with DATA_FILE.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            if fila["receta"] == receta:
                ingredientes.append(fila)
    return ingredientes


def imprimir_ingredientes(receta: str) -> None:
    """
    Imprime por pantalla los ingredientes de la receta indicada.

    Parámetros:
        receta (str): Nombre de la receta.
    """

    filas = listar_ingredientes(receta)
    if not filas:
        print(f"No hay ingredientes para la receta: {receta}")
        return
    print(f"Ingredientes para {receta}:")  # comentario al final de línea
    for fila in filas:
        print(f"- {fila['ingrediente']}: {fila['cantidad_unidad']} {fila['unidad']}")


if __name__ == "__main__":

    # Mensaje de bienvenida e ingredientes impresos
    print("Bienvenido a la Calculadora de Recetas")
    if len(sys.argv) <= 1:
        print("Por favor introduce una receta como argumento")
    else:
        imprimir_ingredientes(sys.argv[1])
