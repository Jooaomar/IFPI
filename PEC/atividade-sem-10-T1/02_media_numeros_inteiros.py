"""
Escreva um programa que leia uma quantidade indefinida de números inteiros 
positivos terminada pelo número 0 (zero). Ao final, o programa deve mostrar 
a média aritmética de todos os números lidos (excluindo o zero).
"""

def media_inteiros(vlr, qtd):
    media = vlr / qtd 
    return round(media,2)


def main():
    
    v   = 0 
    qtd = 0
    while True:

        n = float(input())            
        
        if n != 0:
            qtd += 1
            v   += n
        if n == 0 and v == 0:
            break
        elif n == 0 and v > 0: 
            print(media_inteiros(v, qtd))
            break 


if __name__ == '__main__':
    main()
