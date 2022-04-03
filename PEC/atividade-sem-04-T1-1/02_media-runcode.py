def media(a,b,c):
    m =( a + b + c)/3
    return m


def main():
    x = int(input())
    y = int(input())
    z = int(input())

    resultado = media(x,y,z)

    print(f'{resultado:.2f}')


if __name__ == '__main__':
    main()
