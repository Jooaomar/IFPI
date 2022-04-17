"""
Escreva um programa que leia um caractere e mostra uma das mensagens: “vogal”, 
“consoante”, “número” ou “símbolo”. Observação: O cedilha “ç”, caracteres 
acentuados, espaço em branco e outros como “símbolo”;
"""


def verifica(x):
    if x in 'a,e,i,o,u':
        return 'vogal'
    elif x in 'b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,x,y,w,z':
        return 'consoante'
    elif x in '0,1,2,3,4,5,6,7,8,9':
        return 'número'
    else:
        return 'símbolo'


def main():
    v = input("Escreva um caractere: ").lower()
    r = verifica(v)

    print(f'O caractere é um(a): {r}')


if __name__ == '__main__':
    main()
