def idade(ano_a,ano_n):
    return ano_a - ano_n


def main():

    # Entrada de dados
    dia_atual = input()
    mes_atual = input()
    ano_atual = int(input())
    dia_nascimento = input()
    mes_nascimento = input()
    ano_nascimento = int(input())
    
    # Processamento chamando a função
    resultado = idade(ano_atual, ano_nascimento)

    # Saída de dados
    print(resultado)

if __name__ == '__main__':
    main()
