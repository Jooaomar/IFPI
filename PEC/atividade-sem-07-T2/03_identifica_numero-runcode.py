def identifica(n):
    qtd = 0
    if int(n[0]) % 2 != 0:
        qtd += 1
    if int(n[1]) % 2 != 0:
        qtd += 1
    
    res = mensagem(qtd)

    return(res)


def mensagem(m):
    if m == 1:
        return 'Apenas um dígito é ímpar.'
    elif m == 2:
        return 'Os dois dígitos são ímpares.'
    else:
        return 'Nenhum dígito é ímpar.'

def main():
    numero = input()
    verifica = identifica(numero)
    print(verifica)

if __name__ == '__main__':
    main()
