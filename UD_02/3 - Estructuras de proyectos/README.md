# Calculadora de Recetas
Ajusta cantidades de ingredientes según el número de comensales.

## Requisitos
- Python 3.x
- Instalar dependencias:
- Instalación (pip install -r requirements.txt).
- Instalar dependencias:
pip install -r requirements.txt

## Ejemplo de uso
```bash
python src/main.py
```

## Estructura del proyecto
src/ — código del proyecto
data/ — archivos de datos (CSV)
docs/ — documentación
tests/ — pruebas

calculadora_recetas/
├── src/
│   ├── main.py
│   └── receta.py
├── data/
│   └── recetas.csv
├── docs/
│   └── instrucciones.md
├── tests/
│   └── test_calculos.py
├── requirements.txt
└── README.md

## Como ejecutar
```bash
python src/main.py
```

## Pruebas (pytest):
python -m pytest tests -q

## Ejemplo de salida
Bienvenido a la Calculadora de Recetas
Ingredientes para tortilla:
- huevo: 2 unidad
- patata: 300 gramos
- cebolla: 100 gramos
