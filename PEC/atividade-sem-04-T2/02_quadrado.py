def area_quadrado(L):
    area = L**2
    perimetro = L*4
    return area, perimetro


def main():
    lado = float(input('Insira um valor L: ').strip())
    a, p = area_quadrado(lado)

    print('O valor da área do quadrado é: %10.4f' %(a))
    print('O valor do perimetro do quadrado é: %10.4f' %(p))


if __name__ == '__main__':
    main()
