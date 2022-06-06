"""
Leia 20 números inteiros e armazene-os numa lista. Separe os números pares na 
lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.
"""


"""
Leia 20 números inteiros e armazene-os numa lista. Separe os números pares na 
lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.
"""

def lista_principal():
    """Lista com 20 númros inteiros"""
    lista = []
    for vezes in range(20):
        numero = int(input()) # Ecreva 20 números inteiros
        lista.append(numero)
    return lista

def lista_pares(lista):
    """Devolve números pares da lista recebida"""
    pares = []
    for valor in lista:
        if valor % 2 == 0:
            pares.append(valor)
    return pares


def lista_impares(lista):
    """Devolve números ímpares da lista recebida"""
    impares = []
    for valor in lista:
        if valor % 2 != 0:
            impares.append(valor)
    return impares


def main():
    
    # 20 Números inteiros
    lista = lista_principal()
    print(lista)
    # Números pares da lista
    pares = lista_pares(lista)
    print(pares)
    # Números ímpares
    impares = lista_impares(lista)
    print(impares)





if __name__ == '__main__':
    main()
