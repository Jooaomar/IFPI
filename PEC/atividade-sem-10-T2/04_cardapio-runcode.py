def main():
    
    total = 0
    while True:
            
        print('CÓDIGO  PRODUTO         PREÇO (R$)')
        print('H       Hamburger       5,50')
        print('C       Cheeseburger    6,80')
        print('M       Misto Quente    4,50')
        print('A       Americano       7,00')
        print('Q       Queijo Prato    4,00')
        print('X       PARA TOTAL DA CONTA')

        
        v = input().upper()[0]

        if v == 'H':
            total += 5.50 
        elif v == 'C':
            total += 6.80
        elif v == 'M':
            total += 4.50
        elif v == 'A':
            total += 7.00
        elif v == 'Q':
            total += 4.00
        elif v == 'X':
            print(f'{total:.2f}')
            break 
        else:
            print('Opção inválida.')


if __name__ == '__main__':
    main()
