"""
... escreva um programa para calcular o valor de H. O número n é lido.
"""


def calcula(n):
    
    # [v] base inicial da divisão
    v = 2 
    # [H] valor inicial de H
    H = 1
    
    for x in range(n-1): # [n-1] pois consideramos que o primeiro valor H = 1

        # Calcula H 
        H += (1/v)
        
        # incrementa a base da divisão [v]
        v += 1

    return f'{H:.4f}'


def main():
    
    num = int(input())

    result = calcula(num)

    print(result)


if __name__ == '__main__':
    main()
