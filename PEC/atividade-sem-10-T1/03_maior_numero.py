"""
Escreva um programa que leia uma quantidade indefinida de números inteiros 
positivos terminada pelo número 0 (zero). Ao final, o programa deve mostrar o 
maior e o menor de todos os números lidos (excluindo o zero).
"""

def maior(valores):
    return max(valores)


def menor(valores):
    return min(valores)
    


def main():
    
    v = []
    while True:
        n = int(input("Digite um número inteiro: "))
        
        if n != 0 :
            v.append(n)     
            v_maior = maior(v)
            v_menor = menor(v)
        elif n == 0 and len(v) > 0:
            print(f'O maior valor é: {v_maior}')
            print(f'O menor valor é: {v_menor}')
            break
        elif n == 0:
            break
        

if __name__ == '__main__':
    main()
