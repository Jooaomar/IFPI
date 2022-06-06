"""As estruturas básicas de programação são sequência, condição e repetição. Usando apenas as
estruturas básicas de programação, reescreva as funções abaixo (sem utilizá-las):"""

def comprimento(lista):
    qtd = 0
    for x in lista:
        qtd +=1
    return qtd


def inverter(lista):
    lista_invertida = []

    for x in lista:
        lista_invertida.insert(0,x)
    return lista_invertida


def minimo(lista):

    # Primeiro definido
    menor = lista[0]
    for x in lista:
        if x < menor:
            menor = x
    return menor


def maximo(lista):
    # Primeiro definido
    maior = lista[0]
    for x in lista:
        if x > maior:
            maior = x
    return maior


def soma(lista):
    valor = 0
    for x in lista:
        valor += x
    return valor


def main():

    lista = []
    
    while True:
    # leitura dos valores necessários pelo teclado, a leitura de um número 0 (zero) encerra a
    # leitura dos elementos da lista.
        valor = int(input())
        if valor == 0:
            break
        lista.append(valor)
        

    # Imprimir lista
    print(lista)
    # Uso tipo len
    print(comprimento(lista))
    # Inverter lista
    print(inverter(lista))
    # Valor minimo
    print(minimo(lista))
    # Valor máximo
    print(maximo(lista))
    # Soma dos valores
    print(soma(lista))


if __name__ == '__main__':
    main()
