import statistics

def read_number(n1,n2,n3,n4,n5):
    n = n1,n2,n3,n4,n5
    maior = max(n)
    menor = min(n)
    media = statistics.mean(n)
    return maior, menor, media


def main():
    x1 = int(input('Digite n1: '))
    x2 = int(input('Digite n2: '))
    x3 = int(input('Digite n3: '))
    x4 = int(input('Digite n4: '))
    x5 = int(input('Digite n5: '))

    maior, menor, media = read_number(x1,x2,x3,x4,x5)

    print(f'O maior: {maior}')
    print(f'O menor: {menor}') 
    print(f'A media: {media}')


if __name__ == '__main__':
    main()
