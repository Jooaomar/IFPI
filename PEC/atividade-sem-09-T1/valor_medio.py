def media(n):
    return sum(n) / 100


def main():
    valores = []
    while (len(valores)<100):
        number = int(input())
        valores.append(number)
    m = media(valores)
    print(m)


if __name__ == '__main__':
    main()
