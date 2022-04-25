def ordem(n1,n2,n3):
    valores = [n1,n2,n3]
    return sorted(valores)



def main():
    number_01 = int(input())
    number_02 = int(input())
    number_03 = int(input())

    resultado = ordem(number_01, number_02, number_03)
    
    print(resultado[0])
    print(resultado[1])
    print(resultado[2])



if __name__ == '__main__':
    main()
