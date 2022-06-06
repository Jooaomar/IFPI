"""
Usando apenas as estruturas básicas de programação, reescreva as funções count(), 
que recebe uma lista e um valor e retorna o número de ocorrências do valor na 
lista. Por exemplo count([1, 2, 3, 2, 4, 2, 5], 2) retorna 3, a quantidade de 
vezes que o valor 2 aparece na lista.

Faça a leitura pelo teclado, a leitura de um 0 (zero) encerra a leitura. 
Primeiro leia a lista e depois o valor para pesquisar. Imprima a lista que foi 
lida, o valor pesquisado e o resultado encontrado.
"""

def pesquisa(lista, numero):
    
    qtd = 0
    for x in lista:
        if x == numero:
            qtd +=1
    return qtd


def main():
    lista = []
    
    while True:
    # leitura dos valores necessários pelo teclado, a leitura de um número 0 (zero) encerra a
    # leitura dos elementos da lista.
        valor = int(input())
        if valor == 0:
            break
        lista.append(valor)
    
    # Número a ser pesquisado na lista
    numero = int(input()) 

    # Imprimir lista
    print(lista)
    # Valor pesquisado
    print(numero)
    # Resultado 
    print(pesquisa(lista,numero))

if __name__ == '__main__':
    main()
