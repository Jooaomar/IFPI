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
        elif v == 2:
            print('2 - Vamos estudar mais.')
        elif v == 3:
            print('3 - Meus Parabéns!')
        elif v == 0:
            print('0 - Fim de serviço.')
            break
        else:
            print('Opção inválida.')




if __name__ == '__main__':
    main()
