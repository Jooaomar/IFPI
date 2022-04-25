"""
Escreva um programa que leia 2 datas (cada data é composta por 3 variáveis 
inteiras: dia, mês e ano) e escreva qual delas é a mais recente.
"""

def data_recente(d1,m1,a1,d2,m2,a2): 

    if a1 == a2 and m1 != m2:
        if m1 > m2:
            return d1,m1,a1
        else:
            return d2,m2,a2
    elif a1 == a2 and m1 == m2:
        if d1 > d2:
            return d1,m1,a1
        else:
            return d2,m2,a2
    else:
        if a1 > a2:
            return d1,m1,a1
        else:
            return d2,m2,a2  



def main():
    
    # Entrada de dados
    print("Escreva uma data")
    d1 = int(input("Dia: "))
    m1 = int(input("Mês: "))
    a1 = int(input("Ano: "))
    print("Escreva outra data")
    d2 = int(input("Dia: "))
    m2 = int(input("Mês: "))
    a2 = int(input("Ano: "))

    # Processamento de dados
    d,m,a = data_recente(d1, m1, a1, d2, m2, a2)

    # Saída de dados
    print(f"{d}/{m}/{a}")


if __name__ == '__main__':
    main()
