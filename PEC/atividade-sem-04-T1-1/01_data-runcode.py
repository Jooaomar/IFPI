def format_data(d, m, a):
    data = f'{d}/{m}/{a}'
    return data

def main():
    dia = int(input())
    mes = int(input())
    ano = int(input())

    data = format_data(dia, mes, ano)
    print(data)

if __name__ == '__main__':
    main()

