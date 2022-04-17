"""
Escreva um programa que leia o nome e o sexo de uma pessoa, e mostre o nome 
precedido da mensagem “Ilmo Sr.”, caso seja informado o sexo masculino, ou 
“Ilma Sra.” se for informado o sexo feminino. Use o número inteiro 1 para 
identificar masculino e 2 para identificar feminino.
"""


def identidade(nome, genero):
    
    if genero == 1:
        return f"Ilmo Sr. {nome}"
    if genero == 2:
        return f"Ilma Sra. {nome}"


def main():
    nome = input("Qual seu nome? ").strip()
    sexo = int(input("Qual seu gênero sexual? Escreva 1 masculino ou 2 feminino? "))
    
    print(identidade(nome, sexo))
    

if __name__ == '__main__':
    main()
