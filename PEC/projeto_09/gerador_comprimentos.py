from cgitb import text


def display_menu():
    print("trdtr de exprss")
    print("=" * 13)
    print("Menu:")
    print(" c = converter uma frase")
    print(" p = imprimir discionário")
    print(" a = adicionar uma palavra")
    print(" d = remover uma palavra")
    print(" q = sair")


def converter_sentence(text_speak_dictionary):
    # Obtém a frase para tradução
    sentence = input("Insira uma frase para traduzir: ").lower()

    trasnslated_sentence = ""

    # remove a pontuação da frase
    for char in '?!.,':
        sentence = sentence.replace(char,'')
        
    # Divide a frase em uma lista de palavras
    words_to_translate = sentence.split()
    
    for word in words_to_translate:

        if word in text_speak_dictionary:
            trasnslated_sentence += text_speak_dictionary[word] + " "
        else:
            trasnslated_sentence += word + " "


    print("==>")
    print(trasnslated_sentence)


def add_dictionary_item(text_speak_dictionary):
    text_to_add = input("Insira a expressão a ser adicionada ao discionário: ")
    
    # Adicionar apenas chaves que não existe
    if text_to_add not in text_speak_dictionary:
        meaning = input("O que ela significa?: ")
        text_speak_dictionary[text_to_add] = meaning
    else:
        print(f"Este item '{text_to_add}' já existe!")


def delete_dictionary_item(text_speak_dictionary):
    txt_to_delete = input("Insira a expressão a ser removida ao discionário: ")
    
    if txt_to_delete in text_speak_dictionary:
        del text_speak_dictionary[txt_to_delete]
    else:
        print(f"Este item '{txt_to_delete}' não existe!")


def main():
    
    text_speak_dictionary = {
        "rs" : "risos",
        "tmb" : "também",
        "rs" : "risos",
        "tmb" : "também",
        "vc" : "você",
        "pq" : "porque"
    }
    
    running = True
    
    display_menu()
    
    while running == True:
        
        menu_choice = input(">_").lower()
        
        if menu_choice == 'c':
            converter_sentence(text_speak_dictionary)
            
        elif menu_choice == 'p':
            print(text_speak_dictionary)
        
        elif menu_choice == 'a':
            add_dictionary_item(text_speak_dictionary)
        
        elif menu_choice == 'd':
            delete_dictionary_item(text_speak_dictionary)
        
        elif menu_choice == 'q':
            running = False

        else:
            print("Escolha inválida!")
    



if __name__ == '__main__':
    main()