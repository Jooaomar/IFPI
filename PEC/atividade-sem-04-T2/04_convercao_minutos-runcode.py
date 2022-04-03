def conversao_minutos(m):
    horas = int(m / 60)
    minutos = int(m % 60)
    return horas, minutos


def main():
    v = int(input().strip())
    horas, minutos = conversao_minutos(v)

    print(f"{horas}:{minutos}")


if __name__ == '__main__':
    main()
