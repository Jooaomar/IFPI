from unittest import mock
from unittest import TestCase
import unittest
from discionario_books import discionario, imprimir




# Entrada de dados
f = open("./6.in", "r")
arquivo = f.read()
arquivo = arquivo.split("\n")
arquivo = list(arquivo)

# Saída de dados reproduzida
f = open("./6.out", "r")
saida_esperada = f.read()
saida_esperada = print(saida_esperada)


class DictCreateTests(TestCase):
    @mock.patch('discionario_books.input', create=True)
    def testDiscionarioSimple(self, mocked_input):
        mocked_input.side_effect = arquivo
        result = discionario()
        result = imprimir(result)
        # print(result)
        self.assertEqual(result, saida_esperada)

if __name__ == '__main__':
    unittest.main()