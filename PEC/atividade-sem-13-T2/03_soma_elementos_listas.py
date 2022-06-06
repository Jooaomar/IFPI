"""Leia duas listas A e B contendo 20 elementos inteiros cada, gerar e exibir uma lista C do mesmo
tamanho cujos elementos sejam a soma dos respectivos elementos de A e B."""

def lista_A():
    lista = []
    for vezes in range(20):
        numero = int(input()) # Ecreva 25 números inteiros
        lista.append(numero)
    return lista

def lista_B():
    lista = []
    for vezes in range(20):
        numero = int(input()) # Ecreva 25 números inteiros
        lista.append(numero)
    return lista

def lista_C(lista_a, lista_b):
    
    lista = []
    for x in range(20):
        y = lista_a[x] + lista_b[x]
        lista.append(y)

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
