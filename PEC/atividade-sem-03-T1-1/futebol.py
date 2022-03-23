"""No próximo final de semana seu time de futebol entrará em campo. 
Escreva um programa que leia o seu nível de empolgação para a partida, 
um número inteiro entre 1 e 10, e mostre a empolgação do lado de fora 
do estádio representando por letras “O” ao gritar GOL."""

def empolgacao(nivel):
    """Gerando nível de empolgação no futebol ao sair
    um gol"""
    
    x = nivel
    
    resultado = print('G%sl' %(x))
    
    return resultado

empolgacao(3)
