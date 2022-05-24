"""
Escreva um programa que calcule o fatorial de um número inteiro lido...
"""


def calcula(n):
    """Calcula o valor fatorado do numero n!"""
    
    # [Valor] vai acumular o resultado e [aux] irá contar
    valor = aux = n

    while n > 0:
        
        aux -= 1

        if aux == 0: # quando o contador chegar em 0 finaliza 
            break
        
        # Calcula novo valo
        valor *= aux
    
    # caso o [n] seja igual a 0 [valor] será 1
    if n == 0:
        valor = 1

    return valor

def main():
    number = int(input())
    resultado = calcula(number)
    print(resultado)


if __name__ == '__main__':
    main()
