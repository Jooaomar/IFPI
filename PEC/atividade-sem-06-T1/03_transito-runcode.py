def sinal(cor):
    
    cor = cor.upper()
    if (cor == 'V') or (cor == 'VERDE'):
        return 'Siga'
    if (cor == 'A') or (cor == 'AMARELO'):
        return 'Atenção'
    if (cor == 'E') or (cor == 'VERMELHO'):
        return 'Pare'



def main():
    cor = input().strip()
    print(sinal(cor)) 
     


if __name__ == '__main__':
    main()
    
