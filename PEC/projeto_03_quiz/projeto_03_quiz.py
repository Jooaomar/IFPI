score = 0


print("""
Q1 - No python, como se chama uma 'caixa' usada para armazenar dados?

a - texto
b - variavel
c - uma caixa de sapatos
""")
resposta = input().lower()

if resposta == "a":
    print(" Não - texto é um tipo de dado :(")
elif resposta == "b":
    print(" Correto!! :) ")
    score = score + 2
elif reposta == "c":
    print(" Não seja bobinho! :( ")
else:
    print(" Você não escolheu a, b ou c :( ")


print("""
Q2 - No python, como se chama o espaçamento que define em qual bloco a instrução 
está contida?

a - espaço
b - não existe isso
c - identação
""")
resposta = input().lower()

if resposta == "a":
    print(" Não - é um espaço mas existe um nome específico :(")
elif resposta == "b":
    print(" Claro que existe! :( ")
elif resposta == "c":
    print(" Exato! :) ")
    score = score + 2
else:
    print(" Você não escolheu a, b ou c :( ")

print("""
Q3 - No python, ela recebe uma sequência de comandos que executa alguma tarefa
e que tem um nome. Sua principal finalidade é ajudar a organizar programas em
pedaços. O qué?

a - variaveis
b - funções
c - endentação
""")
resposta = input().lower()

if resposta == "a":
    print(" Não - é uma variável pois faz mais que armazenar dados :(")
elif resposta == "b":
    print(" Acertou! :) ")
    score = score + 2
elif resposta == "c":
    print(" Nada haver! :( ")
else:
    print(" Você não escolheu a, b ou c :( ")


print("""
Q4 - O python se caracterisa por sua tipagem ser:

a - dinamica
b - estática
c - nenhuma
""")
resposta = input().lower()

if resposta == "a":
    print(" Muito bem! :) ")
    score = score + 2
elif resposta == "b":
    print(" Não :( ")
elif resposta == "c":
    print(" Resposta errada :( ")
else:
    print(" Você não escolheu a, b ou c :( ")


print("""
Q5 - O python é uma liguagem de programação:

a - Interpretada de baixo nível
b - Não interpretada de alto nível
c - Interpretada de Nível muito alto
""")
resposta = input().lower()

if resposta == "a":
    print(" Errado! Python é interpretada mas não de baixo nível :( ")
elif resposta == "b":
    print(" Errado! Python é interpretada :( ")
elif resposta == "c":
    print(" Correto! :) ")
    score = score + 2
else:
    print(" Você não escolheu a, b ou c :( ")


if score == 8:
    print(f"Show você mandou bem!!! Acertou {score} pontos ")
elif 2 < score <= 6:
    print(f"Vocẽ pode se sair melhor!!! Acertou {score} pontos")
elif score == 10:
    print(f"Top demais, melhor pontuação! Acertou {score}")
else:
    print(f"Você foi muito mau :( e acertou {score}")


