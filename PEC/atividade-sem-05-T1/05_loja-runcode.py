def compra(produto):
    d_avista = produto * 0.91
    d_sem = produto / 5
    juros = (produto * 1.17) / 10
    return d_avista, d_sem, juros

def main():
    preco = float(input())
    desconto, sem_desconto, com_juros = compra(preco)

    print(f'{desconto:.2f}')
    print(f'{sem_desconto:.2f}')
    print(f'{com_juros:.2f}')


if __name__ == '__main__':
    main()
