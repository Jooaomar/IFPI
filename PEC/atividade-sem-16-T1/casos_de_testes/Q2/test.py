from unittest import mock
from unittest import TestCase
import unittest
from contatos_agenda import dic_agenda, imprimir




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
    @mock.patch('contatos_agenda.input', create=True)
    def testDiscionarioSimple(self, mocked_input):
        mocked_input.side_effect = arquivo
        result = dic_agenda()
        result = imprimir(result)
        print(result)
        self.assertEqual(result, saida_esperada)

if __name__ == '__main__':
    unittest.main()