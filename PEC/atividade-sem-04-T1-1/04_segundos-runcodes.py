def soma_segundos(h, m, s):
    h_s = h * 3600
    m_s = m * 60
    total_s = h_s + m_s + s
    return total_s


def main():
    horas = int(input())
    minutos = int(input())
    segundos = int(input())
    total_segundos = soma_segundos(horas, minutos, segundos)

    print(total_segundos)


if __name__ == '__main__':
    main()
