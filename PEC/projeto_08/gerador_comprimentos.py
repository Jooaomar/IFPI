from random import *

print("Gerador de comprimentos")
print("----------------------")


adjetivos = ["maravilhoso", "acima da média", "excelente"]

hobies = ["andar de bicicleta", "programar", "fazer chá"]

nome = input("Qual o seu nome?: ")
print("Aqui está o seu comprimento", nome, ":")

print(nome, "Você é", choice(adjetivos), "em", choice(hobies))
print("De nada!")


