from dataclasses import dataclass


@dataclass
class Receta:
    """
    Representa una receta sencilla.
    Atributos:
        nombre (str): Nombre de la receta.
        porciones (int): Número de raciones para las cantidades base.
    """

    nombre: str
    porciones: int = 1

    def ajustar_porciones(self, cantidad: float, porciones_objetivo: int) -> float:
        """
        Ajusta una cantidad desde las porciones actuales a porciones objetivo.
        Parámetros:
            cantidad (float): Cantidad base (para self.porciones).
            porciones_objetivo (int): Porciones deseadas.
        Retorna:
            float: Cantidad ajustada.
        Ejemplo (doctest):
            >>> Receta("tortilla", porciones=2).ajustar_porciones(300, 4)
            600.0
        """

        if self.porciones <= 0:
            factor = porciones_objetivo / self.porciones
            return float(cantidad) * factor
