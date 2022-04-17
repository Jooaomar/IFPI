"""
Escreva um programa que leia um caractere e mostra o valor booleano 
True (verdadeiro) se for uma VOGAL ou o valor booleano False (falso) caso 
contrário.
"""


def verifica(x):
    return x in 'a,e,i,o,u'
    


def main():
    v = input("Digite uma letra: ").lower()
    r = verifica(v) 
    print(f'Temos uma vogal? {r}')

if __name__ == '__main__':
    main()
