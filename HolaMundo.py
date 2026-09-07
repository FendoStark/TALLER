from Calculadora import Calculadora
from Operacion import Suma, Resta, Multiplicacion, Division

calculadora = Calculadora()

print("CALCULADORA")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Seleccione una operación: ")

numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese otro númeoro: "))

operaciones = {
    "1": Suma(),
    "2": Resta(),
    "3": Multiplicacion(),
    "4": Division()
}

if opcion in operaciones:

    try:
        resultado = calculadora.ejecutar(
            operaciones[opcion],
            numero1,
            numero2
        )

        print("Resultado:", resultado)

    except ValueError as error:
        print("Error:", error)

else:
    print("Opción no válida")