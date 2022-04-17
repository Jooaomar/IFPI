def verifica(x):
    return x in 'a,e,i,o,u'
    


def main():
    v = input().lower()
    print(verifica(v)) 


if __name__ == '__main__':
    main()
