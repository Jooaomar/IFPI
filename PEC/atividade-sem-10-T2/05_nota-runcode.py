def nota(v):
    if v >= 8.5:
        return 'A'
    if v >= 7.0:
        return 'B'
    if v >= 5.0:
        return 'C'
    if v >= 4.0:
        return 'D'
    if v >= 0.0:
        return 'E'


def main():
    
    while True:
        
        v = float(input())
        
        if v >= 0.0 and v <= 10.0:
            print(nota(v))
            break
        else:
            print('Nota inválida.')


if __name__ == '__main__':
    main()
