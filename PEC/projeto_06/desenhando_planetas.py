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
bgcolor("Black")


# Definindo tamanho do planeta e cor
drawPlanet(5, "red")
forward(50)

done()