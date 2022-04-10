def compra(produto):
    d_avista = produto * 0.91
    d_sem = produto / 5
    juros = (produto * 1.17) / 10
    return d_avista, d_sem, juros

def main():
    preco = float(input('Diga o preco do produto: '))
    desconto, sem_desconto, com_juros = compra(preco)

    print(f'Valor para pagamento a vista: {desconto:.2f}')
    print(f'Prestação para pagamento em 5: {sem_desconto:.2f}')
    print(f'Prestação para pagamento em 10 vezes: {com_juros:.2f}')


if __name__ == '__main__':
    main()
