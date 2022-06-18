"""
Leia uma população e informe as cidades com população maior que o valor lido. 
Veja o exemplo: Veja o exemplo para a leitura de 50000 para a população:
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

def analise_populacional(populacao):
    cidades = carrega_cidades()
    lista = []
    for cidade in cidades:
        if cidade[5] > populacao:
            lista.append(cidade)
    return lista



def main():
    populacao = int(input())
    result    = analise_populacional(populacao)

    print(f"CIDADES COM MAIS DE {populacao} HABITANTES:")
    for uf, ibge, nome, dia, mes, pop in result:
        print(f'IBGE: {ibge} - {nome}({uf}) - POPULAÇÃO: {pop}')

if __name__ == '__main__':
    main()
