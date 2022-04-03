def calcular(a, b, c):
    return 2 * a + 5 * b - c


def main():
    a = int(input('Insira um valor A: ').strip())
    b = int(input('Insira um valor B: ').strip())
    c = int(input('Insira um valor C: ').strip())

    r = calcular(a, b, c)
    print(f"O resultado da equação 2*A+5*B-C é igual a: {r}")

if __name__ == '__main__':
    main()
