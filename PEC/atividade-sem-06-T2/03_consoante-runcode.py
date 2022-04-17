def verifica_consoante(x):
    return x in 'b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,x,w,y,z'


def main():
    v = input().lower()

    r = verifica_consoante(v)
    print(r)


if __name__ == '__main__':
    main()
