"""
Você tem uma poupança de 10 mil reais, que rende 0,7% ao mês. Você deseja comprar um carro, mas o
preço do carro sobe a taxa de 0,4% ao mês. Escreva um programa que leia o preço de um carro hoje e
calcule em quantos meses, com o dinheiro dessa aplicação, você terá dinheiro suficiente para comprar o
carro à vista.
"""

def redimento(polpanca):
    """Calcula rendimento da polpanca"""
    return polpanca * 1.007


def inflacao_carro(valor_carro):
    """Calcula inflção do carro"""
    return valor_carro * 1.004


def compra_em(valor_carro):
    """Calcula quantos meses leva para que o rendimento da polpanca seja maior 
    que a inflação do carro"""
    
    # Total de meses 
    mes = 0
    # valor do carro
    v_carro    = valor_carro
    # valor da polpanca
    v_polpanca = 10000

    while v_polpanca < v_carro: # Se valor polpança for menor que do carro
        v_carro     = inflacao_carro(v_carro) # Calcula inflação do carro
        v_polpanca  = redimento(v_polpanca) # Calcula rendimento da polpança
        mes        += 1 # Soma 1 mês
    
    return mes


def main():
    
    preco_carro = int(input())

    pode_comprar = compra_em(preco_carro)

    print(pode_comprar)


if __name__ == '__main__':
    main()
