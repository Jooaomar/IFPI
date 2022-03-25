"""
Objetivo: Escrevendo um programa que dirá quantos anos você vai ter
em 2025
"""

print("Em que ano você nasceu?")
nascimento = input()
nascimento = int(nascimento)
idade_em_2025 = 2025 - nascimento
print("Em 2025 você terá", idade_em_2025, "anos")
