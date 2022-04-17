"""
Escreva um programa que leia três números inteiros correspondentes a três 
notas de um aluno. Apresente a média das três notas, mas, se a terceira nota 
for superior a 8, o aluno deve ganhar mais um ponto na média. Além disso,
se a média final, em função do ponto extra, ficar acima de 10 ela deve ser 
ajustada para 10.
"""


def media(n1, n2, n3):
    r = (n1+n2+n3)/3
    if n3 > 8:
        r = r + 1
    if r > 10:
        r = 10
    return r


def main():
    nota_1 = int(input("Primeira nota: "))
    nota_2 = int(input("Segunda nota: "))
    nota_3 = int(input("Terceira nota: "))

    resultado = media(nota_1, nota_2, nota_3)

    print(f'Média do aluno é: {resultado:.2f}')

if __name__ == '__main__':
    main()
