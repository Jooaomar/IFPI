def main():
    
    v = 0
    while True:

        n = int(input('Escreva um número inteiro: '))            
        
        if n != 0:
            v += n
        elif n == 0: 
            print(f'A soma dos valores é: {v}')
            break


if __name__ == '__main__':
    main()
