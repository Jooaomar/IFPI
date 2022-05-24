"""
Escreva um programa que leia dois valores inteiros (x e y) e mostre todos os 
números primos entre x e y.
"""

def primos(n_1, n_2):
    
    """Verifica quais valores enre [n_1] e [n_2] são primos"""

    for x in range(n_1, n_2 + 1): # Valores [x] entre [n_1] e [n_2]
                                  # [n_2 + 1] torna incluso o ultimo valor [x]
        
        # Verifica se numero [x] é numero primo usando a função divide_numero()
        numero_primo =  divide_numero(x)

        if numero_primo != None: # Discartando resultados None
            # imprime numero primo
            print(numero_primo)

       
def divide_numero(numero):
   
    # Conta quantos divisores tem o número
    divisores = 0
    
    for x in range(numero): 
        
        # valor inical do divisor [x] deve ser maior que 0
        x += 1

        if numero % x == 0 :  # Verifica se o resto da divisão é igual a 0
            divisores += 1 # Incrementa divisores se resto igual a 0

    if divisores == 2 or divisores == 1: # verifica quantos divisores teve
        return numero # retorna número primo


def main():
    numero_inicial = int(input())
    numero_final = int(input())
    

    primos(numero_inicial, numero_final)



if __name__ == '__main__':
    main()
