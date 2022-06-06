"""
Escreva um programa que leia um número n. Considere uma lista com n posições, 
e então: 
    a) preencha com valores reais lidos pelo teclado e imprima na ordem inversa. 
    Considere até 4 (quatro) casas decimais. 
    b) preencha com n notas lidas pelo teclado e imprima as notas e a média 
    na tela. Considere 1 (uma) casa decimal. 
    c) preencha com n letras lidas pelo teclado e imprima quantas vogais foram 
    lidas. Imprima as consoantes.
"""


def n_lista_ordem_inversa_quatro_decimais(tamanho_lista):

    lista_01 = []
    for vezes in range(tamanho_lista):
        numero = float(input())
        # Jogando o último valor para o ínicio da lista
        lista_01.insert(0, numero)
    
    return lista_01


def n_lista_notas_com_uma_casa_decimal(tamanho_lista):
    # tamanho dessa lista baseado em [n_tamanho_listas]
    # Devolve notas com uma casa decimal
    # Se n = 0 Imprime "SEM NOTAS"
    lista_notas = []
    
    if tamanho_lista == 0:
        return lista_notas, "SEM NOTAS"
    else: 
        for vezes in range(tamanho_lista):
            nota = float(input())
            # Jogando o último valor para o ínicio da lista
            lista_notas.append(nota)

    return lista_notas

def media_notas(notas, tamanho_lista):
    # Devolve de notas media com uma casa decimal
    if "SEM NOTAS" not in notas:
        return sum(notas)/tamanho_lista

def qtd_vogais(tamanho_lista):
    lista_vogais     = []
    lista_consoantes = []

    for vezes in range(tamanho_lista):
        letra = input().strip()
        if letra in 'aeiouAEIOU':
            lista_vogais.append(letra)
        else:
            lista_consoantes.append(letra)
    # quantidade de vogais lidas
    total_vogais = len(lista_vogais)

    return total_vogais, lista_consoantes


def main():
    # Primriro definir Tamanho das listas:
    tamanho_lista = int(input())

    # VAMOS IMPRIMIR
    # 1 - Ordem inversa de lista com  base [tamanho_lista] lidas pelo teclado de numeros com 4 casas decimais
    lista_invertida = n_lista_ordem_inversa_quatro_decimais(tamanho_lista)
    print(lista_invertida)  # Imprime lista invertida

    # 2 - preencha com base [tamanho_lista] Notas lidas pelo teclado com 1 casa decimal
    lista_notas = n_lista_notas_com_uma_casa_decimal(tamanho_lista)

    if "SEM NOTAS" in lista_notas: # Verifica se temos valor "SEM NOTA"
        for valor in lista_notas:  # Imprime lista vazia [] e  "SEM NOTAS"
            print(valor)
    else:
        print(lista_notas) # Imprime lista de notas

    # 3 - Imprime a media das Notas [media_notas(notas)]:
    media = media_notas(lista_notas, tamanho_lista)
    if media != None: # Imprimimos a media somente se houver valor
        print(round(media, 1))

    # 4 - preencha com base  [tamanho_lista] letras lidas pelo teclado e imprima quantas vogais foram lidas. 
    # 5 - Imprimir consoantes.
    vogais, lista_consoantes = qtd_vogais(tamanho_lista)
    print(vogais) # Imprime quantidade de vogais
    print(lista_consoantes) # Imprime a lista de consoantes

if __name__ == '__main__':
    main()

