"""
Escreva um programa que leia um caractere e mostra o valor booleano 
True (verdadeiro) se for um dígito entre ‘0’ e ‘9’ ou o valor booleano 
False (falso) caso contrário
"""

def confere_caracter(x):
    return '0'<= x <= '9' 


def main():
    
    v = input('Inserir Caractere de 0 a 9: ')
    
    print(confere_caracter(v))
       

if __name__ == '__main__':
    main()
