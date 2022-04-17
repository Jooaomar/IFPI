def identidade(nome, genero):
    
    if genero == 1:
        return f"Ilmo Sr. {nome}"
    if genero == 2:
        return f"Ilma Sra. {nome}"


def main():
    nome = input().strip()
    sexo = int(input())
    
    print(identidade(nome, sexo))
    

if __name__ == '__main__':
    main()
