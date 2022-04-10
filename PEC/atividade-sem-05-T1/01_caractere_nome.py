def tamanho_nome(name):
    return len(name)


def main():
    nome = input('Escreva um nome: ').strip()
    tamanho = tamanho_nome(nome)
    print(f'Este nome, {nome}, possui {tamanho} caracteres.')


if __name__ == '__main__':
    main()
