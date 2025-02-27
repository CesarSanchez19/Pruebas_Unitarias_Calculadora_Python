# Definición de la clase Calculadora que proporciona operaciones matemáticas básicas

class Calculadora:
    
    # Método para sumar dos números
    def suma(self, a, b):
        return a + b

    # Método para restar dos números
    def resta(self, a, b):
        return a - b
    
    # Método para restar dos números
    def multiplica(self, a, b):
        return a * b
    
    # Metodo para dividir el primer numero entre el segundo e incluye validacion para evitar division por cero
    def division (self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b