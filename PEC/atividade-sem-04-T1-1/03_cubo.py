def cubo(x):
    return x**3


def main():
    n = int(input('Escreva um número: ').strip())
    c = cubo(n)
    print(f'{n} elevado ao cubo é: {c}')


if __name__ == '__main__':
    main()
