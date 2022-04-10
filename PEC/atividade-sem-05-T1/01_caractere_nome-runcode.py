def tamanho_nome(name):
    return len(name)


def main():
    nome = input().strip()
    tamanho = tamanho_nome(nome)
    print(tamanho)


if __name__ == '__main__':
    main()
