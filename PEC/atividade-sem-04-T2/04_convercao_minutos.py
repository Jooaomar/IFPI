def conversao_minutos(m):
    horas = int(m / 60)
    minutos = int(m % 60)
    return horas, minutos


def main():
    v = int(input("Digite uma quantidade de minutos: ").strip())
    horas, minutos = conversao_minutos(v)

    print(f"{v} minutos é igual a: {horas}:{minutos}hrs")


if __name__ == '__main__':
    main()
