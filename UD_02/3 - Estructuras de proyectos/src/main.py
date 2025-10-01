"""
Calculadora de Recetas
Ajusta cantidades de ingredientes según número de comensales.
"""

import csv

print("Bienvenido a la Calculadora de Recetas")


def listar_ingredientes(receta):
    with open("data/recetas.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [fila for fila in reader if fila["receta"] == receta]


if __name__ == "__main__":
    print("Ingredientes para tortilla:")
    for fila in listar_ingredientes("tortilla"):
        print(f"- {fila['ingrediente']}: {fila['cantidad_unidad']} {fila['unidad']}")
