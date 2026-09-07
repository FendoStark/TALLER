from abc import ABC, abstractmethod

class Operacion(ABC):

    @abstractmethod
    def calcular(self, a: float, b: float) -> float:
        pass

class Suma(Operacion):

    def calcular(self, a: float, b: float) -> float:
        return a + b


class Resta(Operacion):

    def calcular(self, a: float, b: float) -> float:
        return a - b


class Multiplicacion(Operacion):

    def calcular(self, a: float, b: float) -> float:
        return a * b


class Division(Operacion):

    def calcular(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("No se puede dividir por cero")

        return a / b