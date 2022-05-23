"""
O dodô é uma ave não voadora, extinta atualmente, e que era endêmica da Ilha
Maurítius, na costa leste da África. A partir do ano 1600, durante cada ano, 6%
dos animais dos animais vivos no começo do ano morreram e o número de
animais nascidos ao longo do ano que sobreviveram foi de 1% da população
inicial.
Escreva um programa que leia a população de aves no início do ano 1600 e
imprime, anualmente, a partir do fim de 1600, o número de nascimentos, mortes e o total da população
por ano (apenas a parte inteira do números, separados por vírgula). O programa encerra sua execução
quanto a população total cai para menos de 10% da população original.
"""


def situacao(qtd_inicial):
    

    populacao   = qtd_inicial
    ano         = 1599
    mortes      = 0
    nascimentos = 0 

    while True:

        mortes     =  populacao * 0.06
        nascimentos = populacao * 0.01
        populacao  =  populacao + nascimentos - mortes
        ano       += 1
        print(f'{ano:.0f},{nascimentos:.0f},{mortes:.0f},{populacao:.0f}')
        if populacao < qtd_inicial * 0.10:
            break


def main():
    qtd_populacao = int(input())
    situacao(qtd_populacao)


if __name__ == '__main__':
    main()
