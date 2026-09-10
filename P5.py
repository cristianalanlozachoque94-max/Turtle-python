import math
from turtle import *


setup(900, 500)
title("Tortuga: Figuras coloridas")
speed(0)  
hideturtle()


def dibujar_figura(x, y, color_borde, color_relleno, puntos):
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    pencolor(color_borde)
    fillcolor(color_relleno)
    begin_fill()
    for px, py in puntos:
        goto(x + px, y + py)
    end_fill()



def dibujar_ovalo(x, y, color_borde, color_relleno, rx, ry):
    penup()
    goto(x, y - ry)
    setheading(0)
    pendown()
    pencolor(color_borde)
    fillcolor(color_relleno)
    begin_fill()
   
    for i in range(361):
        rad = math.radians(i)
        px = x + rx * math.sin(rad)
        py = (y - ry) + ry + ry * math.cos(rad)  
    end_fill()





dibujar_figura(-320, 100, "black", "deeppink", [])  


def poligono_relativo(x, y, color_relleno, instrucciones):
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    pencolor("black")
    fillcolor(color_relleno)
    begin_fill()
    for func, val in instrucciones:
        if func == "f":
            forward(val)
        elif func == "l":
            left(val)
        elif func == "r":
            right(val)
    end_fill()



penup()
goto(-330, 80)
setheading(0)
pendown()
fillcolor("deep sky blue")
begin_fill()
forward(70)
left(120)
forward(70)
left(120)
forward(70)
left(120)
end_fill()

penup()
goto(-170, 80)
setheading(0)
pendown()
fillcolor("red")
begin_fill()
for _ in range(4):
    forward(65)
    left(90)
end_fill()


penup()
goto(-20, 80)
setheading(0)
pendown()
fillcolor("yellow")
begin_fill()
for _ in range(2):
    forward(90)
    left(90)
    forward(60)
    left(90)
end_fill()


penup()
goto(160, 110)
setheading(0)
pendown()
fillcolor("limegreen")
begin_fill()
circle(35)
end_fill()



penup()
goto(-290, -30)
setheading(0)
pendown()
fillcolor("yellow")
begin_fill()
left(45)
for _ in range(2):
    forward(55)
    left(90)
    forward(55)
    left(90)
end_fill()

penup()
goto(-130, -30)
setheading(0)
pendown()
fillcolor("deep sky blue")
begin_fill()
forward(70)
left(60)
forward(55)
left(120)
forward(70)
left(60)
forward(55)
left(120)
end_fill()


penup()
goto(20, -30)
setheading(0)
pendown()
fillcolor("limegreen")
begin_fill()
forward(70)
left(115)
forward(60)
left(65)
forward(30)
left(65)
forward(60)
left(115)
end_fill()


penup()
goto(185, -5)
setheading(0)
pendown()
fillcolor("red")
begin_fill()

setheading(0)
for _ in range(2):
    forward(80)
    circle(30, 180)
end_fill()

done()
