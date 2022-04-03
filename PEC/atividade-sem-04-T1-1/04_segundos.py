def soma_segundos(h, m, s):
    h_s = h * 3600
    m_s = m * 60
    total_s = h_s + m_s + s
    return total_s


def main():
    horas = int(input('Escreva o valor horas: '))
    minutos = int(input('Escreva o valor minutos: '))
    segundos = int(input('Escreva o valor segundos: '))
    total_segundos = soma_segundos(horas, minutos, segundos)

    print(f'De meia noita à {horas}:{minutos}:{segundos} hrs, se passaram {total_segundos} segundos')


if __name__ == '__main__':
    main()
