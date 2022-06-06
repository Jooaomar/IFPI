"""Um time de basquete possui 12 jogadores. Deseja-se um programa que, dado o nome e a altura
dos jogadores, determine:"""

def mais_alto(nome, altura):
    valor = max(altura)
    nome  = nome[altura.index(valor)]
    return valor, nome


def altura_media_time(altura):
    media = sum(altura) / len(altura)
    return round(media, 2)


def altura_acima_da_media(nomes, alturas, media):
    
    resultado = []
    jogadores = []
    
    for x in range(12):
        if alturas[x] > media:
            resultado.append(alturas[x])
            jogadores.append(nomes[x])
   
    # Quantidade de jogadores
    qtd = len(jogadores)
    return jogadores, resultado, qtd


def main():
    nome   = []
    altura = []
    for vezes in range(12):
        nome.append(input())
        altura.append(float(input()))
    
    # Nome e altura do jogador mais alto
    maior_altura, jogador_maior = mais_alto(nome, altura)   
    print("JOGADOR MAIS ALTO DO TIME")
    print(jogador_maior)
    print(f'{maior_altura:.2f}')

    # A média de altura do time
    print("ALTURA MÉDIA DO TIME")
    media = altura_media_time(altura)
    print(media)
    
    # Jogaores com altura maior que a média
    print("JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME")
    jogadores_ma, alturas_jogad, qtd = altura_acima_da_media(nome,altura, media)
    for x in range(qtd):
        print(jogadores_ma[x])
        # Formatando altura para string com 2 casas decimais
        altura_format = f'{alturas_jogad[x]:.2f}'
        print(altura_format)



if __name__ == '__main__':
    main()
