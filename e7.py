# 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una 
# persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es 
# opcional. Crear los siguientes métodos para la clase: 
#  Un constructor, donde los datos pueden estar vacíos. 
#  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
# directamente, sólo ingresando o retirando dinero. 
#  mostrar(): Muestra los datos de la cuenta. 
#  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
# negativa, no se hará nada. 
#  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números 
# rojos.


class Persona:
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def get_dni(self):
        return self.__dni

class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad
    
    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            print("Error: La cantidad no puede ser negativa.")
    
    def get_cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        print("Datos de la cuenta:")
        print(f"Titular: {self.__titular.get_nombre()}")
        print(f"Edad del titular: {self.__titular.get_edad()}")
        print(f"DNI del titular: {self.__titular.get_dni()}")
        print(f"Cantidad en la cuenta: {self.__cantidad}")
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        self.__cantidad -= cantidad

# Ejemplo de uso
titular = Persona("Juan Pérez", 30, "12345678")
cuenta = Cuenta(titular, 1000)

cuenta.mostrar()
cuenta.ingresar(500)
cuenta.retirar(200)

cuenta.mostrar()
