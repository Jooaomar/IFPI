from random import *

# Desafio: vinte-e-um 

print('''
      Vinte e um!
      ========= 
      Tente fazer exatamete 21 pontos!
    
      ''')
score      = 0
jogando    = True 

while jogando == True:
    
    print('\nSua pontuação é ', score)

    v = input('Gostaria de somar mais um número? (s/n) ').lower() 
        
    if v == 's':
        n = randint(1,10)
        score += n
        print('\nSua pontuação é ', score)

    if v == 'n':
        print('Sua pontuação final é', score)
        jogando = False

    if score == 21:
        print("\n** Parabéns! Você fez 21 pontos **")
        jogando = False 

    if score > 21:
        print("Que pena!!")
        jogando = False

