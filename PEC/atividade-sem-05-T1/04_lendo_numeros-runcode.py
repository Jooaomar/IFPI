import statistics

def read_number(n1,n2,n3,n4,n5):
    n = n1,n2,n3,n4,n5
    maior = max(n)
    menor = min(n)
    media = statistics.mean(n)
    return maior, menor, media


def main():
    x1 = int(input())
    x2 = int(input())
    x3 = int(input())
    x4 = int(input())
    x5 = int(input())

    maior, menor, media = read_number(x1,x2,x3,x4,x5)

    print(maior)
    print(menor) 
    print(media)


if __name__ == '__main__':
    main()
