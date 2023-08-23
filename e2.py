#2. Escribir una función que calcule el mínimo común múltiplo entre dos números

def multiplicacion(numero1,numero2):
    return numero1 * numero2


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

resultado = multiplicacion(numero1, numero2)
print(f"el Mutiplo {numero1} y {numero2} es {resultado}.")