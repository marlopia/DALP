def sumar_iva(precio, iva):
    """Devuelve el precio con IVA aplicado

    Args:
        precio (float): precio sin IVA
        iva (float): porcentaje de IVA

    Returns:
        float: precio con IVA

    Examples:
    >>> sumar_iva(100.0,21.0) == 121.0
    """
    return precio + precio * (iva / 100)
