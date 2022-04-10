def tempo(segs):
    h = horas(segs)
    m = minutos(segs)
    s = segundos(segs)
    return h,m,s


def horas(minu):
    h = minu // 3600
    return h


def minutos(segs):
    m = (segs % 3600) // 60
    return m


def segundos(segs):
    s = (segs % 3600) % 60
    return s


def main():
    qtd_minutos = int(input())
    horas, minutos, segundos = tempo(qtd_minutos)

    print(f'{horas}:{minutos}:{segundos}')


if __name__ == '__main__':
    main()
