"""03.Fazer um programa para ler uma matriz n x m de números inteiros. Os 
valores de n e m são inteiros, positivos e devem ser informados pelo usuário, 
calcular e armazenar em uma tupla para mostrar, respectivamente:"""


def preencher_matriz():
    linhas = int(input().strip())
    colunas = int(input().strip())

    matriz = [] # Lista vazia
    for lin in range(linhas):
        linha = [] # Cada linha é uma lista (vetor)
        for col in range(colunas):
            # Gera número aleatório entre 1 e 50
            linha.append(int(input().strip()))
        # Insere a linha na matriz
        matriz.append(linha)

    return matriz


def main():
    matriz = preencher_matriz()

    resposta = ()

    # Soma de elementos da primeira linha
    resposta += sum(matriz[0]),
    
    # A soma dos elementos da última coluna
    som_ult_colun = 0
    for linha in matriz:
        som_ult_colun += linha[-1]
    resposta += som_ult_colun,

    # A média de todos os elementos
    element_matr = []
    for linha in matriz:
        for v in linha:
            element_matr.append(v)
    media_todos = sum(element_matr)/len(element_matr)
    resposta += round(media_todos, 4),

    # O menor elemento
    menor = min(element_matr)
    resposta += menor,

    # O maior elemento
    maior = max(element_matr)
    resposta += maior,

    # Imprime resposta
    print(resposta)


if __name__ == '__main__':
    main()
