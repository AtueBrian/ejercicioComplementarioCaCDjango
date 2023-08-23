from e7 import Cuenta, Persona

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    def set_bonificacion(self, bonificacion):
        if bonificacion >= 0:
            self.__bonificacion = bonificacion
        else:
            print("Error: La bonificación no puede ser negativa.")
    
    def get_bonificacion(self):
        return self.__bonificacion
    
    def es_titular_valido(self):
        edad_titular = self._Cuenta__titular.get_edad()
        return 18 <= edad_titular < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("Error: No se puede retirar dinero si el titular no es válido.")
    
    def mostrar(self):
        super().mostrar()
        print(f"Cuenta Joven con bonificación del {self.__bonificacion}%")
    

# Ejemplo de uso
titular_joven = Persona("Ana López", 22, "87654321")
cuenta_joven = CuentaJoven(titular_joven, 1500, 5)

cuenta_joven.mostrar()

if cuenta_joven.es_titular_valido():
    print("El titular es válido para esta cuenta joven.")
else:
    print("El titular no es válido para esta cuenta joven.")

cuenta_joven.retirar(300)
cuenta_joven.mostrar()
