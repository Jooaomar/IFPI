"""Escreva um programa que leia dois números e mostre na tela a soma e a 
multiplicação deles."""

def soma(x, y):
    return x + y

def mutiplicacao(x, y):
    return x * y


print("Insira dois números")
print("Valor 1:")
v1 = input()
v1 = int(v1)
print("Valor 2:")
v2 = input()
v2 = int(v2)

print("Soma dos valores:", soma(v1, v2))
print("Multiplicação dos valores:", mutiplicacao(v1, v2))
