def idade(dia_a, mes_a, ano_a, dia_n, mes_n, ano_n):
    
    idade = ano_a - ano_n
    if mes_n > mes_a:
        idade -= 1 
    elif mes_n == mes_a:
        if dia_n > dia_a:
            idade -= 1

    return idade 


def main():

    # Entrada de dados
    dia_atual = input()
    mes_atual = input()
    ano_atual = int(input())
    dia_nascimento = input()
    mes_nascimento = input()
    ano_nascimento = int(input())
    
    # Processamento chamando a função
    resultado = idade(dia_atual,mes_atual,ano_atual,dia_nascimento, mes_nascimento,ano_nascimento)

    # Saída de dados
    print(resultado)

if __name__ == '__main__':
    main()
