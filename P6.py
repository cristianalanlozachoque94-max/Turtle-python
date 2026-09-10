from turtle import *


setup(900, 500)
title("Tortuga: Escenario de cementerio")
speed(0)
hideturtle()


penup()
goto(-450, -250)
setheading(0)
pendown()
fillcolor("#0a0a1a")  
begin_fill()
for _ in range(2):
    forward(900)
    left(90)
    forward(350)
    left(90)
end_fill()


penup()
goto(-450, -250)
setheading(0)
pendown()
fillcolor("#1c2826")  
begin_fill()
for _ in range(2):
    forward(900)
    left(90)
    forward(150)
    left(90)
end_fill()


penup()
goto(250, 100)
setheading(0)
pendown()
fillcolor("#f4f6f0")  
begin_fill()
circle(40)
end_fill()



def dibujar_lapida(x, y, ancho, alto):
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    fillcolor("#7f8c8d")  
    pencolor("#34495e")
    begin_fill()
    forward(ancho)
    left(90)
    forward(alto - ancho / 2)
    circle(ancho / 2, 180)
    forward(alto - ancho / 2)
    left(90)
    end_fill()


dibujar_lapida(-250, -180, 50, 80)
dibujar_lapida(-170, -160, 40, 60)
dibujar_lapida(80, -170, 60, 95)
dibujar_lapida(170, -150, 45, 70)



def dibujar_arbol_seco(x, y):
    penup()
    goto(x, y)
    setheading(90)
    pendown()
    pencolor("#2c3e50")
    pensize(8)
    forward(90)  
    left(35)
    forward(40)
    backward(40)
    right(70)
    forward(45)
    backward(45)
    left(35)
    pensize(1)  


dibujar_arbol_seco(-60, -180)
dibujar_arbol_seco(-350, -180)



penup()
goto(-50, -160)
setheading(0)
pendown()
fillcolor("#4a5568")
pencolor("#1a202c")
begin_fill()
for _ in range(2):
    forward(100)
    left(90)
    forward(70)
    left(90)
end_fill()


penup()
goto(-60, -90)
pendown()
begin_fill()
goto(0, -40)
goto(60, -90)
goto(-60, -90)
end_fill()


penup()
goto(-15, -160)
pendown()
fillcolor("#1a202c")
begin_fill()
forward(30)
left(90)
forward(45)
circle(15, 180)
forward(45)
left(90)
end_fill()

done()
