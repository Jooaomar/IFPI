"""
Leia duas listas A e B contendo 25 elementos inteiros cada, gerar e imprimir 
uma lista C de 50 elementos, cujos elementos sejam a intercalação dos 
elementos de A e B.
"""

"""Leia duas listas A e B contendo 25 elementos inteiros cada, gerar e imprimir uma lista C de 50 elementos,
cujos elementos sejam a intercalação dos elementos de A e B."""

def lista_A():
    lista = []
    for vezes in range(25):
        numero = int(input()) # Ecreva 25 números inteiros
        lista.append(numero)
    return lista

def lista_B():
    lista = []
    for vezes in range(25):
        numero = int(input()) # Ecreva 25 números inteiros
        lista.append(numero)
    return lista

def lista_C(lista_a, lista_b):
    lista = lista_a + lista_b
    lista[::2]  = lista_a 
    lista[1::2] = lista_b      
    return lista


def main():

    primeira_lista = lista_A()
    segunda_lista  = lista_B()
    terceira_lista = lista_C(primeira_lista, segunda_lista)

    print(primeira_lista)
    print(segunda_lista)
    print(terceira_lista)   


if __name__ == '__main__':
    main()
