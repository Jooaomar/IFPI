def main():
    while True:
        
        print('OPÇÕES:')
        print('1 - SAUDAÇÃO')
        print('2 - BRONCA')
        print('3 - FELICITAÇÃO')
        print('0 - FIM')

        v = int(input())

        if v == 1:
            print('1 - Olá. Como vai?')
        if v == 2:
            print('2 - Vamos estudar mais.')
        if v == 3:
            print('3 - Meus parabéns!')
        if v == 0:
            print('0 - Fim de serviço.')
            break




if __name__ == '__main__':
    main()
