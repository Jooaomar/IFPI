"""
Escreva um programa que pergunte o depósito inicial e a taxa de juros ao ano de 
uma poupança. Mostre em quantos anos o valor acumulado será o dobro do valor 
inicial...
"""

def dobra_em(deposito, taxa):
    
    anos  = 0
    valor = deposito
    
    while valor < deposito*2 :
        valor *= (1 + taxa/100)
        anos+=1

    return anos



def main():
    
    dp = int(input('Escreva um valor para depósito: '))
    tx = float(input('Escreva um valor de taxa: '))
    a  = dobra_em(dp,tx)

    print('Em {anos} anos você terá {dobro} '.format(anos = a, dobro = dp * 2))



if __name__ == '__main__':
    main()
