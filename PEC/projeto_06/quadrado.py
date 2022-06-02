from turtle import *

def quadrado():

    pendown()       # Começar a desenhar

    begin_fill()    # Colorir forma

    for side in range(5):
        left(90)   # Girar a esquerda
        forward(100) # ANdar

    end_fill()      # Parar de colorir

    penup()         # Parar de desenhar

quadrado()