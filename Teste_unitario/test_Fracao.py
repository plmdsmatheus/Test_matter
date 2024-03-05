import unittest
from fracao import Fracao 

class ExemploTest(unittest.TestCase):

    def test_1(self):
        x = 0
    
    def test_2(self):
        self.assertEqual(5, 5)

    def test_3(self):
        self.assertEqual(5, 5)
    
    def test_Fracao_Subtracao(self):
        f1 = Fracao(2,1)
        f2 = Fracao(5,1)
        result = f1.subtrair(f2)

        self.assertEqual(-3, result.numerador)
        self.assertEqual(1, result.denominador)

    def test_Fracao_Soma(self):
        f1 = Fracao(2,1)
        f2 = Fracao(5,1)
        result = f1.somar(f2)

        self.assertEqual(7, result.numerador)
        self.assertEqual(1, result.denominador)

    def test_Fracao_Divisao(self):
        f1 = Fracao(2,4)
        f2 = Fracao(5,3)
        result = f1.dividir(f2)

        self.assertEqual(20, result.denominador)
        self.assertEqual(6, result.numerador)

    def test_Fracao_Multiplicacao(self):
        f1 = Fracao(2,4)
        f2 = Fracao(5,3)
        result = f1.multiplicar(f2)

        self.assertEqual(12, result.denominador)
        self.assertEqual(10, result.numerador)

    def test_Fracao_redutiva(self):
        f = Fracao(16, 4)
        result = f.reduzir()

        self.assertEqual(4, result.numerador)
        self.assertEqual(1, result.denominador)
        
if __name__ == '__main__':
  unittest.main()
