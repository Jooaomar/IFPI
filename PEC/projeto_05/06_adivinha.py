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
        # Gerando número aleatório de 1 a 10
        n = randint(1,10)
        # Acrescendo número aleatório ao score
        score += n
        # Pontuação
        print('\nSua pontuação é ', score)
    
    # Caso não queira continuar encerrar jogo e pontuação final
    if v == 'n':
        print('Sua pontuação final é', score)
        jogando = False
    
    # Se acertar os 21 pontos usuário ganha jogo
    if score == 21:
        print("\n** Parabéns! Você fez 21 pontos **")
        jogando = False 
    
    # Se passar de 21 pontos, usuário perde jogo
    if score > 21:
        print("Que pena!!")
        jogando = False

