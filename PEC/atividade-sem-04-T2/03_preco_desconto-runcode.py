def preco_calculado(preco, percentual):
    acrescendo = 1 + (percentual/100)
    descontando = 1 - (percentual/100)

    preco_acrescido = preco * acrescendo
    preco_descontado = preco * descontando
    
    return preco_acrescido, preco_descontado


def main():
    preco = float(input().strip())
    porcentagem = float(input().strip())
    
    preco_acrescido, preco_descontado = preco_calculado(preco, porcentagem)

    print(f"{preco_acrescido:.2f}")
    print(f"{preco_descontado:.2f}")

if __name__ == '__main__':
    main()
