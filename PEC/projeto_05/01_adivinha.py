from random import *

print('''
      Porta da Fortna!

      =========

      Existe um super prêmio atrás de uma destas 3 portas!
      Adivinhe qual é a porta certa para ganhar o prêmio!
        
       _____   _____   _____
      |     | |     | |     |
      | [1] | | [2] | | [3] |
      |   ° | |   ° | |   ° |
      |_____| |_____| |_____|      
               
      Escolha uma porta (1, 2 ou 3):  
    
      ''')


porta_escolhida = input()
porta_escolhida = int(porta_escolhida)

porta_certa = randint(1,3)

print('A porta escolhida foia a', porta_escolhida)
print('A porta certa é a', porta_certa)


if porta_escolhida == porta_certa:
    print('Parabéns!')
else:
    print('Que peninha!')
