from Operacion import Operacion

class Calculadora:

    def ejecutar(
        self,
        operacion: Operacion,
        a: float,
        b: float
    ) -> float:

        return operacion.calcular(a, b)