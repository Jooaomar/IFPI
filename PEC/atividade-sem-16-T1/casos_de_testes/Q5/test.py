from unittest import mock
from unittest import TestCase
import unittest
from aluno_matricula import consulta_matricula, matricula




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
    @mock.patch('aluno_matricula.input', create=True)
    def testDiscionarioSimple(self, mocked_input):
        mocked_input.side_effect = arquivo
        result = matricula()
        print("==================================")
        result = consulta_matricula(result)
        self.assertEqual(result, saida_esperada)

if __name__ == '__main__':
    unittest.main()