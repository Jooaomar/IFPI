def verifica(x):
    return 'a' <= x <= 'z'


def main():
    v = input().lower()
    r = verifica(v)
    print(r)

if __name__ == '__main__':
    main()
