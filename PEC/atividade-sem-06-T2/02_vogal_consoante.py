"""
Escreva um programa que leia um caractere e mostra o valor booleano 
True (verdadeiro) se for uma LETRA (vogal ou consoante) ou o valor booleano 
False (falso) caso contrário.
"""


def verifica(x):
    return 'a' <= x <= 'z'


def main():
    v = input().lower()
    r = verifica(v)
    print(r)

if __name__ == '__main__':
    main()
