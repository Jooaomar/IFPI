"""
Leia um dia e um mês como números inteiros distintos e informe as cidades que 
fazem aniversário nessa data. Veja o exemplo para o dia 9 e mês 2:
"""


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

def aniversario(dia, mes):
    cidades = carrega_cidades()
    lista = []
    for cidade in cidades:
        if cidade[3:5] == (dia,mes):
            lista.append(cidade)
    return lista


def mes_ano(n):
    n -= 1 
    lista = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO',
            'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
    
    return lista[n]

def main():
    dia = int(input())
    mes = int(input())
    result = aniversario(dia, mes)
    
    print(f"CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {mes_ano(mes)}:")
    for uf, ibge, nome, dia, mes, pop in result:
        print(f'{nome}({uf})')

if __name__ == '__main__':
    main()
