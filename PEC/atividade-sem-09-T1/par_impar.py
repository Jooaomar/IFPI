def identifica(n):
    pares = 0    
    impares = 0
    for r in n: 
        if (r % 2) == 0:
            pares = pares + 1
        else:
            impares = impares + 1
    return pares, impares


def main():
    
    valores = []
    while (len(valores)<100):
        number = int(input())
        valores.append(number)
    p, i = identifica(valores)
    print(p)
    print(i)




if __name__ == '__main__':
    main()
