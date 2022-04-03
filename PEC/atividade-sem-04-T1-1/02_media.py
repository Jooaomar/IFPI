def media(a,b,c):
    m = (a + b + c)/3
    return m


def main():
    x = int(input("Digite um número x: ").strip())
    y = int(input("Digite um número y: ").strip())
    z = int(input("Digite um número z: ").strip())

    resultado = media(x,y,z)

    print(f'A média de {x}, {y}, {z} é: %1.2f'%(resultado))


if __name__ == '__main__':
    main()
