"""DEsafio: Melhorando sua cifra"""

# Embaralhar lista
alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto = alfabeto[::] + 

# a chave secreta é 3
chave = int(input("Escreva o valor da chave secreta: "))

mensagem = input("Por favor entre com uma mensagem a ser criptografada: ").lower()

mensagem_criptografada = ""

for char in mensagem:
    if char in alfabeto:
        posicao = alfabeto.find(char)

        nova_posicao = (posicao + chave) % 26
        
        # Vai somando a letra por vez
        mensagem_criptografada = mensagem_criptografada +  alfabeto[nova_posicao]
    else:
        mensagem_criptografada = mensagem_criptografada + char

print("Sua mensagem criptografada é", mensagem_criptografada)
