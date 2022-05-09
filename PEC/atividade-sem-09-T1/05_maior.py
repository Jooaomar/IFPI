def maior(n):
    return max(n)


def main():
    valores = []
    while (len(valores)<=99):
        number = int(input())
        valores.append(number)
    resultado = maior(valores)
    print(resultado)


if __name__ == '__main__':
    main()
