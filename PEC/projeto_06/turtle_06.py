from curses import start_color
from tracemalloc import start
from turtle import *
from random import *


def moveToRandomLocation():
    """Função que move a tartaruga para uma posição aleatória"""
    penup()
    setpos( randint(-400,400), randint(-400,400) )
    pendown()



def drawStart(startSize, startColor):
    """Uma função para desenhar uma estrela de um tamanho específico"""
    color(startColor)
    pendown()           # Começar a desenhar
    begin_fill()        # Colorir forma

    for side in range(5):
        left(144)       # Girar a esquerda
        forward(startSize) # ANdar

    end_fill()          # Parar de colorir
    penup()             # Parar de desenhar


def drawGalaxy(numberOfStars):
    """Uma função para desenhar uma pequena galáxia de estrelas"""
    startColours = ["#058396", "#0275A6", "#827E01"]
    moveToRandomLocation()
    # Desenha várias pequenas estrelas coloridas    
    for star in range(numberOfStars):
        penup()
        left( randint(-180, 180) )
        forward( randint(5,20) )
        pendown()

        # Desenha uma pequena estrela de cor aleatória
        drawStart( 2, choice(startColours) )

speed(11)

# Desenha o fundo Azul escuro
bgcolor("MidnightBlue")

# Desenha 30 estrelas brancas
for star in range(30):
    moveToRandomLocation()
    drawStart( randint(5,25), "White" )

# Desenha 3 pequenas galáxias de 40 estrelas
for galaxy in range(3):
    drawGalaxy(40)


hideturtle()
done()