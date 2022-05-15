def analise_salario(s):
    return s * 1.05



def analise_divida(d):
    return d * 1.15


def analise_situacao(s, d):
    mes = 10
    ano = 2016
    
    divida  = d
    salario = s
    
    while True:
        
        divida  = analise_divida(divida)
        if mes == 3:
            salario = analise_salario(salario) 

        mes +=1

        if mes == 13:
            mes = 1
            ano +=1 

        if divida > salario: 
            break
    return mes, ano


def main():
    salario = int(input('Salario: '))
    divida  = int(input('Dívida: '))
    m, a  = analise_situacao(salario, divida) 
    print(f'{m}/{a}')
    


if __name__ == '__main__':
    main()
