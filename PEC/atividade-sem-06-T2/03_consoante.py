"""
Escreva um programa que leia um caractere e mostra o valor booleano 
True (verdadeiro) se for uma consoante ou o valor booleano False (falso) 
caso contrário.
"""

def verifica_consoante(x):
    return x in 'b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,x,w,y,z'


def main():
    v = input("Digite uma letra: ").lower()

    r = verifica_consoante(v)
    print(f"É uma consoante? {r}")


if __name__ == '__main__':
    main()
