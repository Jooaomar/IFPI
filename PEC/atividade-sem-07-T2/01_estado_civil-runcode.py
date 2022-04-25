def caractere(name):
    return len(name)


def estado_civil(nome, valor):
    if valor == 1:
        conjuge = input().strip()
        qtd_caracer = caractere(nome + conjuge)
        return qtd_caracer
    else:
        return caractere(nome)
 


def main():
    nome = input().strip()
    estado = int(input())

    resultado = estado_civil(nome, estado)
    
    print(resultado)

if __name__ == '__main__':
    main()
