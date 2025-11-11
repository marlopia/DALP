import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from functions import sumar_iva


def test_sum():
    assert sum([1, 2, 3]) == 6


@pytest.mark.parametrize(
    "precio,iva,resultado",
    [
        (100, 21, 121.0),  # 21% IVA
        (200, 10, 220.0),  # 10% IVA
        (50, 5, 52.5),  # 5% IVA
        (0, 21, 0.0),  # precio base 0
        (150, 0, 150.0),  # sin IVA
    ],
)
def test_sumar_iva(precio, iva, resultado):
    assert sumar_iva(precio, iva) == resultado
