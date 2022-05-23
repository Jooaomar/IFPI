"""
A tartaruga e a lebre vão apostar uma corrida. A lebre concede à tartaruga o 
direito de sair n sua frente. A tartaruga corre a 1 metro por minuto e a lebre 
corre a 10 metros por minuto. Faça um programa que leia quantos metros a 
tartaruga sai à frente da lebre e calcule quantos minutos levará até que a 
lebre alcance a tartaruga. Por exemplo, se a tartaruga sair 500 metros à frente 
a lebre alcança em 56 minutos.
"""

def alcance_lebre(d_tartaruga):

    distancia_tartaruga = d_tartaruga
    distancia_lebre     = 1
    
    alcanca_em          = 0

    while distancia_lebre < distancia_tartaruga:
        alcanca_em          += 1
        distancia_tartaruga += 1
        distancia_lebre     += 10
    
    return alcanca_em


def main():

    tartaruga_adiantada = int(input())
    
    lebre_alcanca = alcance_lebre(tartaruga_adiantada)

    print(lebre_alcanca)

if __name__ == '__main__':
    main()
