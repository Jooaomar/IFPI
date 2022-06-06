"""
Escreva um programa que leia um número n. Considere uma lista com n posições, e então:
"""

def lista_zero(tamanho=None):
    L = []
    # 1 - Listando Valores zero
    if tamanho != None: 
        for x in range(tamanho): 
            L.append(0)
        return L
    else:
        return L

def largura_lista(tamanho=None):
    L = []
    # 2 - Listando de 1 até tamanho da lista
    if tamanho != None: 
        for x in range(tamanho):
            x += 1
            L.append(x)
        return L
    else:
        return L

def lista_ate(lista=None, tamanho=None):
    L = []
    # 3 - Valores a partir do índice 1 ate índice n tamanho da lista 
    if tamanho != None: 
        tamanho += 1 
        L = [x for x in lista[1:tamanho]]
        return L
    else:
        return L

def lista_invertida(lista=None, tamanho=None):
    L = []
    # 4 - Invertendo valores restante
    if tamanho != None:
        tamanho += 1
        for x in lista[tamanho:]:
            L.insert(0, x)
        return L
    else:
        return L



def main():
    lista_base     = []
    
    contador = 0
    # Inserindo números na lista base
    while True:
        # OBS: O Primeiro valor n é o tamanho das listas
        n = int(input())
        
        if n != 0:  # Arescemos a lista base
            lista_base.append(n)
        if n == 0:  # Quando o primeiro valor for zero, retorna listas []
            lista_01 = lista_zero()
            lista_02 = largura_lista()
            lista_03 = lista_ate()
            lista_04 = lista_invertida()
            
            print(lista_01)
            print(lista_02)
            print(lista_03)
            print(lista_04)
            break
        if (2*lista_base[0]) == contador:
            """Criamos 4 listas"""
            tamanho_lista = lista_base[0] 
            lista_01 = lista_zero(tamanho_lista)
            lista_02 = largura_lista(tamanho_lista)
            lista_03 = lista_ate(lista_base, tamanho_lista)
            lista_04 = lista_invertida(lista_base, tamanho_lista)
            
            print(lista_01)
            print(lista_02)
            print(lista_03)
            print(lista_04)
            break
        
        contador +=1


if __name__ == '__main__':
    main()

