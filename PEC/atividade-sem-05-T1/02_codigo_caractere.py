def codigo(caractere):
    return ord(caractere)


def main():
    caractere = input('Digite um caractere qualquer: ').strip()
    print('O código unicode é:', codigo(caractere))


if __name__ == '__main__':
    main()
