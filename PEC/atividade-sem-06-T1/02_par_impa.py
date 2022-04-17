"""
Escreva um programa que leia um número e mostra o valor booleano 
True (verdadeiro) se o número for ímpar ou o valor booleano False 
(falso) caso contrário.
"""


def par_impar(n):
    return n % 2 != 0


def main():
    number = int(input('Digite um número inteiro: '))
    print(par_impar(number))

if __name__ == '__main__':
    main()
