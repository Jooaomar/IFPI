# lista de letras para criptografar
alfabeto = "abcdefghijklmnopqrstuvwxyz"

# a chave secreta é 3
chave = int(input("Escreva o valor da chave secreta: "))

letra = input("Por favor entre com uma letra para criptografar: ")


# Encontre uma posição da letra em alfabeto
# Exemplo: "a" está na posição 0, "e" está na posição 4, etc.
posicao = alfabeto.find(letra)

# Some a chave secreta para encontrar a posição da letra criptografada
#% 26 significa 'volte para 0 quando você chegar no 26'
nova_posicao = (posicao + chave) % 26

letra_criptografada = alfabeto[nova_posicao]

print("Sua letra criptografada é", letra_criptografada)
