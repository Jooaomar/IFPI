"""
O índice de massa corporal (IMC) é uma medida internacional usada para 
calcular se uma pessoa está no peso ideal. O IMC é determinado pela divisão da 
massa do indivíduo pelo quadrado de sua altura, em que a massa está em 
quilogramas e a altura em metros. Escreva um programa que leia a 
massa (o peso) e a altura...
"""


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
    
    massa = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))

    # Processamento
    calculo = imc(massa,altura)
    resultado = condicao(calculo)
    
    # Saída
    print(f"Seu IMC é: {calculo} e seu índice é: {resultado}")


if __name__ == '__main__':
    main()
