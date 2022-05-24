"""
A Sequência de Fibonacci é uma sequência de números inteiros, começando por 0 e 1, na qual, cada termo
subsequente corresponde à soma dos dois anteriores (0, 1, 1, 2, 3, 5, 8, 13, ...). Escreva um programa que
leia um número n, calcule e mostre os n primeiros termos da sequência de Fibonacci. O valor lido para n
sempre será maior ou igual a 2.
"""


def fibonacci(n):
    """Retorna a sequencia dos numeros calculados"""

    sequencia = '0, 1'

    v_anterior  = 0 
    v_depois    = 1 

    for x in range(n-2): # -2 tira a diferença dos 2 primeiros valores 0, 1 incluso
        """Cada valor [x] representa uma posição na sequência"""
        
        if x % 2 == 0: # Quando a posição da sequencia for par

            # Atualiza valor anterior
            v_anterior += v_depois
            # inserir valor na sequencia
            sequencia = sequencia + ", " + str(v_anterior)
        
        else: # Quando a posição da sequência for impar

            # Atualiza valor anterior
            v_depois += v_anterior 
            # inserir valor na sequência
            sequencia = sequencia + ", " + str(v_depois)

    return sequencia
    


def main():
    
    num = int(input())
    result = fibonacci(num)

    print(result)


if __name__ == '__main__':
    main()
