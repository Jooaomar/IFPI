def media(a,b,c):
    m = (a + b + c)/3
    return m


def main():
    x = int(input("Digite um número x: "))
    y = int(input("Digite um número y: "))
    z = int(input("Digite um número z: "))

    resultado = media(x,y,z)

    print(f'A média de {x}, {y}, {z} é: %1.2f'%(resultado))


if __name__ == '__main__':
    main()
