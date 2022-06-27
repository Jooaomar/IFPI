# Desafio: Planetas distantes

def escolha_planeta(planetas):
    planeta = input("Digite um planeta: ")
    
    # Adicionar apenas chaves que não existe
    if planeta in planetas:
        print(f'{planeta} está a {planetas[planeta]} km da Terra')
    elif planeta == 'q':
        return 'q'
    else:
        print(f"Este item '{planeta}' não existe!")


def main():
    
    planetas = {
        "Mercúrio": "91.700.000",
        "Venus" : "41.400.000",
        "Marte" : "225.000.000",
        "Jupiter" : "778.000.000",
        "Saturno" : "1.4000.000.000",
        "Urano" : "4.308.000.000",
        "Netuno" : "4.000.000.000"
    }
    
    running = True
    
    print("Descubra a distáncia de um planeta da terra")
    print("Digite 'q' para sair")
    while running == True:
        
        a = escolha_planeta(planetas)
        if a == 'q':
            running = False
        
    



if __name__ == '__main__':
    main()