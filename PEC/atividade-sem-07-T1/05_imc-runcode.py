def imc(m, a):
    return int(m/(a**2))


def condicao(valor):
    if valor < 18.5:
        return 'Abaixo do peso'
    elif valor < 25:
        return 'Peso normal'
    elif valor < 30:
        return 'Sobrepeso'
    elif valor < 35:
        return 'Obeso leve'
    elif valor < 40:
        return 'Obeso moderado'
    else:
        return 'Obeso mórbido'


def main():
    
    massa = float(input())
    altura = float(input())

    # Processamento
    calculo = imc(massa,altura)
    resultado = condicao(calculo)
    
    # Saída
    print(f"{calculo}\n{resultado}")


if __name__ == '__main__':
    main()
