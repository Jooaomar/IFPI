"""
Escreva um programa que leia um caractere e mostra o valor booleano 
True (verdadeiro) se for uma LETRA (vogal ou consoante) ou um NÚMERO 
(entre ‘0’ e ‘9’) ou valor booleano False (falso) caso contrário.
"""


def verifica(valor):
    if 'a' <= valor <= 'z':
        return True
    elif '0' <= valor <= '9':
        return True
    else:
        return False
    


def main():
    caracter = input().lower()

    resultado = verifica(caracter)
        
    print(resultado)


if __name__ == '__main__':
    main()
