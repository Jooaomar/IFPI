"""
Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio. Escreva um programa
que leia um número e determine se ele é ou não primo.
"""

def primo(n):
    """Verifica se o [n] é número primo, retornando True ou False"""
    
    # quantidade de divisores
    divisores = 0

    for x in range(n):

        # tira o valor da divisão inicial por 0
        x +=1

        if n % x == 0 :  # Verifica se o resto é igual a 0
            divisores += 1 # Incrementa divisores se resto igual a 0

    if divisores == 2 or divisores == 1: # verifica quantos divisores teve
        return True  # Se 2 ou 1 divisores é número primo
    else:
        return False # Se mais de 2 divisores não é número primo



def main():
    
    numero = int(input())

    eh_primo = primo(numero)
    print(eh_primo)

if __name__ == '__main__':
    main()
