# Passo 1: Quanto dinheiro?
print(8*2)

"""
Desafio: Dinheiro no bolso
"""
print(12*12.50)

# Passo 2: Quantos anos?
print(2025 - 2004)

"""
Desafio Mudando datas
"""
print(2025 - 1998)
print(2050 - 2022)

# Passo 3: Variáveis
print("Em que ano você nasceu?")
nascimento = input()
nascimento = int(nascimento)
idade_em_2025 = 2025 - nascimento
print("Em 2025 você terá", idade_em_2025, "anos")

"""
Desafio: O ano 3000
"""
print("Em que ano você nasceu?")
nascimento = input()
nascimento = int(nascimento)
print("Para qual ano você quer saber sua idade?")
idade_em = input()
idade_em = int(idade_em)
idade = idade_em - nascimento
print(f"Em {idade_em} você terá {idade} anos")
