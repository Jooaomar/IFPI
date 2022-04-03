def inverter(n):
    return n[::-1]


def main():
    v = input('Escreva um número inteiro entre 1000 e 9999: ').strip()
    r = inverter(v)

    print(f"Número invertido: {r}")


if __name__ == '__main__':
    main()
