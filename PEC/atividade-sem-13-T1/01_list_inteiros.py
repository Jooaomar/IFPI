"""
Leia uma lista de 10 (dez) números inteiros, mostre os números, sua soma e a 
multiplicação.
"""
def mutiplica(lista):
    produto = 1
    for numero in lista:
        produto *= numero
    return produto



def main():

    my_list = []
    
    while len(my_list) < 10:
        v = int(input())
        my_list.append(v)

    print(my_list)
    print(sum(my_list))
    print(mutiplica(my_list))
        
        

if __name__ == '__main__':
    main()
