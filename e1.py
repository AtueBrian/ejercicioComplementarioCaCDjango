# 1. Escribir una función que calcule el máximo común divisor entre dos números.


def division(numero1,numero2):
    return numero1 / numero2


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

resultado = division(numero1, numero2)
print(f"El Máximo Común Divisor entre {numero1} y {numero2} es {resultado}.")