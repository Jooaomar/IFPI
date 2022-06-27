def main():
    
    cadastros = {
        "João Marcelo" : "123456",
        "Maria" : "654321"
    }
    
    for x in range(4):
        
        print("Programa super sercreto")
        print("="*25)
        nome = input("Nome: ")
        senha = input("Senha: ")
        # tentativas
        tentativas = 4 - (x + 1)
        
        
        if nome in cadastros:
            if cadastros[nome] == senha:
                print("BEM-VINDO PROGRAMADOR")
                break
            else:
                print("Senha inválida!")
                print(f"Você tem {tentativas} tentativas ")
        else:
            print("Usuário inválido")
            print(f"Você tem {tentativas} tentativas ")
            

if __name__ == '__main__':
    main()