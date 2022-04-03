def area_quadrado(L):
    area = L**2
    perimetro = L*4
    return area, perimetro


def main():
    lado = float(input().strip())
    a, p = area_quadrado(lado)

    print('%10.4f' %(a))
    print('%10.4f' %(p))


if __name__ == '__main__':
    main()
