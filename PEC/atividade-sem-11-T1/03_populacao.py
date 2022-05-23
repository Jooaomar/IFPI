"""
Dado um país A, com taxa de natalidade de 2% ao ano, e um país B com uma taxa de natalidade de 3%
ano. Sabe-se que, atualmente, o país A tem população maior que o país B. Faça um programa que leia a
população de cada país e imprima o tempo necessário para que a população do país B ultrapasse a
população do país A.
"""

def ultrapassa_natalidade(pais_a, pais_b):

    time_anos = 0
    
    pais_A = max(pais_a, pais_b)
    pais_B = min(pais_a, pais_b)
    
    while pais_B < pais_A:
        pais_A    *= 1.02
        pais_B    *= 1.03
        time_anos += 1
    return time_anos  


def main():
    
    pais_a = int(input())
    pais_b = int(input())

    ultrapassa_em = ultrapassa_natalidade(pais_a, pais_b)
    print(ultrapassa_em)


if __name__ == '__main__':
    main()
