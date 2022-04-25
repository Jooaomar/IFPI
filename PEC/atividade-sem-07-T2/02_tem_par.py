def verifica(n):
    qtd = 0

    if len(n) == 3:
        if int(n[0]) % 2 == 0:
            qtd += 1
        if int(n[1]) % 2 == 0:
            qtd += 1
        if int(n[2]) % 2 == 0:
            qtd += 1
        return qtd 
    else:
        return qtd


def main():
    number = input('Digite um número entre 100 e 999: ')
    qtd = verifica(number)
    

    print(f"Esse número possui {qtd} números pares ")

if __name__ == '__main__':
    main()
