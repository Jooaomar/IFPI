def inverter(n):
    return n[::-1]


def main():
    v = input().strip()
    r = inverter(v)

    print(f"{r}")


if __name__ == '__main__':
    main()
