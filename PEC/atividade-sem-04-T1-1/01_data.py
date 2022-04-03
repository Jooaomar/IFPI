def format_data(d, m, a):
    data = f'{d}/{m}/{a}'
    return data

def main():
    dia = int(input('Escreva o dia: '))
    mes = int(input('Escreva o mês: '))
    ano = int(input('Escreva o ano: '))

    data = format_data(dia, mes, ano)
    print(data)

if __name__ == '__main__':
    main()

