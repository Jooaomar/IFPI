"""
Foram anotados nomes, idades e alturas de 30 alunos. Faça um programa que 
determine quais alunos com mais de 13 anos possuem altura inferior à média de 
altura dos alunos. Considerar a altura arredondando para duas casas decimais.
"""

def maior_que_13(idades, lista_alturas, lista_nomes):
    alturas = []
    alunos  = []
    
    for x in range(30):
        if idades[x] > 13:
            alturas.append(lista_alturas[x])
            alunos.append(lista_nomes[x])

    return alturas, alunos


def altura_inferior_media(lista_alturas, lista_nomes, media):
    alturas = []
    nomes   = []
    # Alunos maior que 13 menor que a media
    qtd = len(lista_nomes)
    for x in range(qtd):
        if lista_alturas[x] < media:
            alturas.append(lista_alturas[x])
            nomes.append(lista_nomes[x])

    return nomes, alturas 
        


def media_altura(lista):
    media = sum(lista)/len(lista)
    return round(media,2)


def main():
    
    nomes   = []
    idades  = []
    alturas = []

    for vzes in range(30):
         nomes.append(input())
         idades.append(int(input()))
         alturas.append(float(input()))


    # Media
    result_media = media_altura(alturas)
    
    # Maior que 13 e alturar inferior que a media
    result_alturas, result_alunos = maior_que_13(idades, alturas, nomes)
    alunos_altura_inferior, valor = altura_inferior_media(result_alturas, result_alunos, result_media)
    
    # Quantidade de alunos
    qtd = len(alunos_altura_inferior)
    # Imprimir resultado
    print("MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA")
    for x in range(qtd):
        print(alunos_altura_inferior[x])


if __name__ == '__main__':
    main()
