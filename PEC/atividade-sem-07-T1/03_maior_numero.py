def maior(n1,n2,n3,n4,n5):
    number_max = n1
 
    if n2 > number_max:
        number_max = n2
    if n3 > number_max:
        number_max = n3
    if n4 > number_max:
        number_max = n4
    if n5 > number_max:
        number_max = n5 
    
    return number_max 


def menor(n1,n2,n3,n4,n5):
    number_min = n1
 
    if n2 < number_min:
        number_min = n2
    if n3 < number_min:
        number_min = n3
    if n4 < number_min:
        number_min = n4
    if n5 < number_min:
        number_min = n5 
    
    return number_min 


def main():

    # Entrada de dados
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())
    
    # Processamento
    maior_numero = maior(n1,n2,n3,n4,n5)
    menor_numero = menor(n1,n2,n3,n4,n5)

    print(maior_numero)
    print(menor_numero)


if __name__ == '__main__':
    main()
