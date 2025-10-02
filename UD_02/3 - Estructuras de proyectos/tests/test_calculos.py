from src.main import listar_ingredientes


def test_listar_ingredientes_devuelve_lista():
    filas = listar_ingredientes("tortilla")
    assert isinstance(filas, list)
    if filas:  # si hay datos, comprobamos claves mínimas
        assert {"receta", "ingrediente", "cantidad_unidad", "unidad"} <= set(
            filas[0].keys()
        )
