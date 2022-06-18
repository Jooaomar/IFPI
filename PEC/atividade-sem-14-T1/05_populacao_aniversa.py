"""Leia um mês e uma população. Mostre as cidades com população maior que o 
valor lido fazem aniversário no mês informado."""


def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado

def analise_populacional(populacao, mes_aniversario):
    lista = []
    for cidade in mes_aniversario:
        if cidade[5] > populacao:
            lista.append(cidade)
    return lista


def aniversario(mes):
    cidades = carrega_cidades()
    lista = []
    for cidade in cidades:
        if cidade[4] == mes:
            lista.append(cidade)
    return lista

def mes_ano(n):
    n -= 1 
    lista = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO',
            'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
   
    return lista[n]


def main():
    mes  = int(input())
    populacao = int(input())
    cond_anivers  = aniversario(mes)
    result  = analise_populacional(populacao, cond_anivers)

    print(f"CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM {mes_ano(mes)}:")
    for uf, ibge, nome, dia, mes, pop in result:
        print(f'{nome}({uf}) tem {pop} habitantes e faz aniversário em {dia} de {mes_ano(mes).lower()}.')

if __name__ == '__main__':
    main()
