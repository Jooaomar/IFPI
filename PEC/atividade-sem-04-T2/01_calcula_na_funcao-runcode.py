def calcular(a, b, c):
    return 2 * a + 5 * b - c


def main():
    a = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())

    r = calcular(a, b, c)
    print(r)

if __name__ == '__main__':
    main()
