from turtle import *

speed(1000)

def drawPlanet(startSize, startColor):

    color(startColor)
    pendown()           # Começar a desenhar

    begin_fill()        # Colorir forma

    for count in range(360):
        forward(1)
        right(startSize)

    end_fill()          # Parar de colorir

    penup()             # Parar de desenhar

# Desenha o fundo azul escuro
bgcolor("MidnightBlue")

drawPlanet(1, "red")
forward(100)

done()