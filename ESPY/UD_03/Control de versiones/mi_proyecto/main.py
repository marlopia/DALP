# Cambiar idioma del print
print("Hello World!")

# Despedirse del usuario
print("Goodbye World!")
# Awa de mayo
# AwA de OwO


class Empleado:
    def __init__(self, salario):
        self.salario = salario  # Digamos que es por jornal de 8h

    def calcular_salario(self):
        pass


class EmpleadoTiempoCompleto(Empleado):
    def calcular_salario(self):
        print(f"Tu salario es de {self.salario}€")


class EmpleadoTiempoParcial(Empleado):
    def calcular_salario(self):
        horas = 4  # Media jornada
        salario_final = (self.salario / 8) * horas
        print(f"Tu salario para {horas}h son {salario_final}€")


emp_1 = EmpleadoTiempoCompleto(120)
emp_2 = EmpleadoTiempoParcial(120)

emp_1.calcular_salario()

emp_2.calcular_salario()
