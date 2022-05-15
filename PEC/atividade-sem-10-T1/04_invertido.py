def invertendo(numero):
    
    test_num = 0
    while (numero>0):
        resto = numero % 10
        test_num = (test_num * 10) + resto
        numero = numero // 10
    return test_num



def main():
    num = int(input('Insira um número: '))
    print(invertendo(num))

   

if __name__ == '__main__':
    main()
