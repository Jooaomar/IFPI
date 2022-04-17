def media(n1, n2, n3):
    r = (n1+n2+n3)/3
    if n3 > 8:
        r = r + 1
    if r > 10:
        r = 10
    return r


def main():
    nota_1 = int(input())
    nota_2 = int(input())
    nota_3 = int(input())

    resultado = media(nota_1, nota_2, nota_3)

    print(f'{resultado:.2f}')

if __name__ == '__main__':
    main()
