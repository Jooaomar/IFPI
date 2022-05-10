from turtle import *

# Desenhando uma casa

shape("turtle")
speed(5)

forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(45)
forward(70)
right(90)
forward(70)

# tira a caneta
penup()
# Girar
right(45)
# andar
forward(100)
# Girar
right(90)
# andar
forward(20)
# Girar
right(90)

# Colocar caneta
pendown()
# andar
forward(40)
# Girar
left(90)
# andar
forward(50)
# Girar
left(90)
# andar
forward(40)

done()
