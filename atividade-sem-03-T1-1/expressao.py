"""Escreva um programa que ler o valor da variável x. Calcule e mostre o 
resultado da expressão: 9x-4x+10 """


def calculando(x):
    Y = 9*x - 4*x + 10
    return Y


print("Calculando 'Y' da função ")
print("Insira um valor para x")
x = input()
x = int(x)
Y = calculando(x)
print("O resultado de 9x-4x+10 é:", Y)

