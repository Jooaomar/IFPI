"""
Escreva um programa que leia o nome e o estado civil de uma pessoa, considere 
apenas “1” para casado e “2” para solteiro. Se a pessoa for casada, leia, 
também, o nome do cônjuge. Mostre quantos caracteres no total existem no(s) 
nome(s) lido(s).
"""

def caractere(name):
    return len(name)


def estado_civil(nome, valor):
    if valor == 1:
        conjuge = input("Escreva o nome de seu cônjuge: ").strip()
        qtd_caracer = caractere(nome + conjuge)
        return qtd_caracer
    else:
        return caractere(nome)
 


def main():
    nome = input('Escreva seu nome: ').strip()
    estado = int(input('Você possui um cônjuge? Escreva 1 para sim ou 0 para não: '))

    resultado = estado_civil(nome, estado)
    
    print(f"Total de caracteres por nome {resultado}")

if __name__ == '__main__':
    main()
