"""
Escreva um programa que leia um caractere e mostra o valor booleano 
True (verdadeiro) se for um dígito entre ‘0’ e ‘9’ ou o valor booleano 
False (falso) caso contrário.
"""

def sinal(cor):
    
    cor = cor.upper()
    if (cor == 'V') or (cor == 'VERDE'):
        return 'Siga'
    if (cor == 'A') or (cor == 'AMARELO'):
        return 'Atenção'
    if (cor == 'E') or (cor == 'VERMELHO'):
        return 'Pare'



def main():
    cor = input('Digite uma cor semafórica: ').strip()
    print(sinal(cor)) 
     


if __name__ == '__main__':
    main()
    
