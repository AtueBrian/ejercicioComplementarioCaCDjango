# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una 
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero 
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el 
# ejercicio tanto de manera iterativa como recursiva.

# version iterativa

# def get_int():
#     while True:
#         try:
#             valor = int(input("Ingrese un valor entero: "))
#             return valor
#         except ValueError:
#             print("Error: No se pudo convertir el valor a entero. Intente nuevamente.")

# entero = get_int()
# print(f"Valor entero ingresado: {entero}")


# version recursiva

def get_int_recursivo():
    try:
        valor = int(input("Ingrese un valor entero: "))
        return valor
    except ValueError:
        print("Error: No se pudo convertir el valor a entero. Intente nuevamente.")
        return get_int_recursivo()

entero = get_int_recursivo()
print(f"Valor entero ingresado: {entero}")
