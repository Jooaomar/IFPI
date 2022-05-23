"""
O número da sorte de uma pessoa é calculado somando os dígitos da sua data de 
nascimento. Escreva um programa que leia a data de nascimento, digitada no 
formado ddmmaaaa (um número inteiro com 8 dígitos), e mostre o seu número da 
sorte. Por exemplo, quem nasceu em 29/04/1989 deve digitar 29041989 e o 
programa vai calcular que o número da sorte é 42 (2 + 9 + 0 + 4 + 1 + 9 + 8 + 9 = 42).
"""

def somar_digitos(n):
    s = 0
    while n:
        s += n % 10 # Soma `s` ao ultimo numeral de `n`
        n //= 10 # Remove o ultimo numero de `n`
    return s



def main():
    
    data         = int(input())
    numero_sorte = somar_digitos(data) 
    print(numero_sorte)

if __name__ == '__main__':
    main()
