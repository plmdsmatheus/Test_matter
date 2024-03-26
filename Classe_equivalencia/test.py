# tests.py

import unittest
import modelo

class TestTriangulo(unittest.TestCase):
    def test_validar_forma(self):
        # Válidos
        self.assertTrue(modelo.Triangulo(2, 4, 5).validarForma())  # É triângulo
        self.assertTrue(modelo.Triangulo(5, 5, 5).validarForma())  # É triângulo
        self.assertTrue(modelo.Triangulo(5, 5, 7).validarForma())  # É triângulo
        # Inválidos
        self.assertFalse(modelo.Triangulo(1, 2, 3).validarForma())  # Não é triângulo
        self.assertFalse(modelo.Triangulo(2, 3, 6).validarForma())  # Não é triângulo
        self.assertFalse(modelo.Triangulo(0, 2, 3).validarForma())  # Não é triângulo
        self.assertFalse(modelo.Triangulo(-5, -8, 1).validarForma())  # Não é triângulo

    def test_eh_equilatero(self):
        # Válidas
        self.assertTrue(modelo.Triangulo(5, 5, 5).ehEquilatero())  # Triângulo Equilátero
        # Inválidas
        self.assertFalse(modelo.Triangulo(3, 4, 5).ehEquilatero())  # Triângulo não é Equilátero

    def test_eh_isosceles(self):
        # Válidas
        self.assertTrue(modelo.Triangulo(5, 5, 7).ehIsosceles())  # Triângulo Isósceles
        # Inválidas
        self.assertFalse(modelo.Triangulo(3, 4, 5).ehIsosceles())  # Triângulo não é Isósceles

    def test_eh_escaleno(self):
        # Válidas
        self.assertTrue(modelo.Triangulo(3, 4, 5).ehEscaleno())  # Triângulo Escaleno
        # Inválidas
        self.assertFalse(modelo.Triangulo(5, 5, 5).ehEscaleno())  # Triângulo não é Escaleno


if __name__ == '__main__':
    unittest.main()