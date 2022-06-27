"""Escreva um programa que lê matrícula, nome e duas notas de vários alunos e armazena tais 
notas em um dicionário, onde a chave é a matrícula do aluno. A entrada de dados deve 
terminar quando for lida uma string vazia como matrícula. Escreva uma função que retorna a 
média do aluno, dado sua matrícula, o programa finaliza com a leitura de uma matrícula 
vazia,"""


###### NOTA o professor quer que o programa pare de receber matriculas quando o valor for
# em branco. E o valor a ser impimido é dado de acordo com a matrícula digitada não 

def matricula():
    discio = {}
    
    while True:
        # Verificar condição
        matricula = input().strip()
        if (matricula == ''):
            break
            
        # Entradas
        nome = input().strip()
        nota_1 = float(input().strip())
        nota_2 = float(input().strip())
        # Media
        media = calcula_media(nota_1, nota_2)
        
        # ìndice Matricula
        discio[matricula] = {}
        # Nome aulo
        discio[matricula]['Nome'] = nome
        # Média
        discio[matricula]['Média'] = round(media,1)
    
    return discio


def calcula_media(n1,n2):
    return (n1+n2)/2


def consulta_matricula(dic):
    lista = []
    
    while True:
        # Verificar condição
        matricula = input().strip()
        if (matricula == ''):
            break
        lista.append(matricula)
    
    for matricula in lista:
        print(f"{dic[matricula]['Nome']}: {dic[matricula]['Média']}")


def main():
    dic = matricula()
    consulta_matricula(dic)
    # imprimir(dic)
    # print(dic)


if __name__ == '__main__':
    main()