# Desafio adicionando traduções

text_speak_dictionary = {
    "rs" : "risos",
    "tmb" : "também",
    "vc" : "você",
    "pq" : "porque"
}

# Obtém a frase para tradução
sentence = input("Insirauma frase para traduzir: ").lower()

# Divide a frase em uma lista de palavras
words_to_translate = sentence.split()

trasnslated_sentence = ""

for word in words_to_translate:

    if word in text_speak_dictionary:
        trasnslated_sentence += text_speak_dictionary[word] + " "
    else:
        trasnslated_sentence += word + " "

print("==>")
print(trasnslated_sentence)