# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los 
# siguientes métodos para la clase: 
#  Un constructor, donde los datos pueden estar vacíos. 
#  Los setters y getters para cada uno de los atributos. Hay que validar las entradas de 
# datos. 
#  mostrar(): Muestra los datos de la persona.

class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    
    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print("Error: El nombre debe ser una cadena de texto.")
    
    def get_nombre(self):
        return self.__nombre
    
    def set_edad(self, edad):
        if isinstance(edad, int) and edad > 0:
            self.__edad = edad
        else:
            print("Error: La edad debe ser un número entero positivo.")
    
    def get_edad(self):
        return self.__edad
    
    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 8 and dni.isdigit():
            self.__dni = dni
        else:
            print("Error: El DNI debe ser una cadena de 8 dígitos numéricos.")
    
    def get_dni(self):
        return self.__dni
    
    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"DNI: {self.__dni}")

# Ejemplo de uso
persona = Persona()
persona.set_nombre("Juan Pérez")
persona.set_edad(30)
persona.set_dni("12345678")

persona.mostrar()
