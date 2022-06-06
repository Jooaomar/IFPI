from random import *

executa = True


print("Gerador de comprimentos")
print("----------------------")


adjetivos = ["maravilhoso", "acima da média", "excelente", "TOP DEMAIS", "genial", "espetacular", "showww"]

hobies = ["andar de bicicleta", "programar", "fazer chá"]

nome = input("Qual o seu nome?: ")

print("""
Menu
    c = obter cumprimento
    a = adicionar hobby
    d = remover hobby
    p = imprimir hobies
    q = sair
      """)

print(nome, "Você é", choice(adjetivos), "em", choice(hobies))
print("De nada!")



while executa == True:
    menu_choice = input("\n>_").lower()

    if menu_choice == 'c':

        print("Aqui está o seu cumprimento", nome, ":")

        print(nome, "você é", choice(adjetivos), "em", choice(hobies))
        print("De nada!")
    
    elif menu_choice == 'a':
        item_to_add = input("Adicione o hobby: ")
        hobies.append(item_to_add)

    elif menu_choice == 'd':
        
        item_to_delete = input("Insira o hobby a ser deletado: ")
        if item_to_delete in hobies:
            hobies.remove(item_to_delete)
        else:
            print("O hobie não está na lista!")
    elif menu_choice == 'p':
        print(hobies)

    elif menu_choice == 'q':
        executa = False 

    else:
        print("Escolha uma opção válida!")


