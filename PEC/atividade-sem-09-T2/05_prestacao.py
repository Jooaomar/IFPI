def calcula(v,n):
    return '%1.2f'%(v/(n+1))


def main():
    valor = int(input('Escreva um valor: '))
    for x in range(24):
        c = calcula(valor, x)
        print(f'{x+1}x de R$ {c}')
    



if __name__ == '__main__':
    main()
