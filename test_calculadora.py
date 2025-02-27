# Importancia del módulo unittest para poder realizar pruebas unitarias

import unittest  # Librería para pruebas unitarias

# Importación de la clase Calculadora desde el archivo calculadora.py
from calculadora import Calculadora

# Definición de la clase de pruebas que hereda de unittest.TestCase
class TestCalculadora(unittest.TestCase):
    # Método que se ejecuta antes de cada prueba
    def setUp(self):
        # Creamos una instancia de Calculadora para usar en las pruebas
        self.calc = Calculadora()

    # Prueba del método suma
    def test_suma(self):
        # Prueba la suma de dos números positivos
        self.assertEqual(self.calc.suma(5, 4), 9)
        
        # Prueba la suma de un número negativo y uno positivo
        self.assertEqual(self.calc.suma(-1, 1), 0)
        
        # Prueba de la suma de dos ceros
        self.assertEqual(self.calc.suma(0, 0), 0)
        
    # Prueba del método resta
    def test_resta(self):
        # Prueba la resta de dos números positivos
        self.assertEqual(self.calc.resta(9, 4), 5)
        
        # Prueba la resta de dos números iguales
        self.assertEqual(self.calc.resta(4, 4), 0)
        
        # Prueba la resta de dos números negativos
        self.assertEqual(self.calc.resta(-2, -2), 0)
    
    # Prueba del método multiplicacion
    def test_multiplicar(self):
        # Prueba la multiplicacion de dos numeros positivos
        self.assertEqual(self.calc.multiplica(5, 4),20)
        
        # Prueba la multiplicacion de dos numeros positivos
        self.assertEqual(self.calc.multiplica(1, 0), 0)
        
        # Prueba la multiplicacion de un numero negativo por uno positivo
        self.assertEqual(self.calc.multiplica(-3, 4), -12)
    
    # Prueba del metodo division
    def test_division(self):
        # Prueba la division exacta
        self.assertEqual(self.calc.division(10, 2), 5)
        
        # Prueba la division con resultado decimal
        self.assertEqual(self.calc.division(9, 2), 4.5)
        
        # Prueba con division periodica usando assertAlmostEqual para comparar con precision limitada
        self.assertAlmostEqual(self.calc.division(5, 11), 0.45454545454545454545454545454545)
    
    # Prueba especifica para verificar el manejo de la division por cero
    def test_division_por_cero(self):
        # Prueba para evaluar cuando dividida el primer numero entre el segundo e incluye validacion para evitar division por cero
        with self.assertRaises(ValueError):
            self.calc.division(20, 0)
        
        # Fuentes del metodo de prueba: https://docs.python.org/es/3.9/library/unittest.html#unittest.TestCase.assertRaises

# failUnlessEqual o assertEquals obsoleto.

# Bloque condicional que permite ejecutar las pruebas directamente
if __name__ == '__main__':
    # Inicializar la ejecución de todas las pruebas definidas en la clase
    unittest.main()

