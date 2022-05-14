def dobra_em(deposito, taxa):
    
    anos  = 0
    valor = deposito
    
    while valor < deposito*2 :
        valor *= (1 + taxa/100)
        anos+=1

    return anos



def main():
    
    dp = int(input())
    tx = float(input())
    a  = dobra_em(dp,tx)

    print(a)



if __name__ == '__main__':
    main()
