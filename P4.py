import turtle
import math

screen = turtle.Screen()
screen.bgcolor("yellow")

t = turtle.Turtle()
t.hideturtle()

t.penup()
t.goto(-230, -180)
t.pendown()
t.color("black")
t.width(4)
for i in range(2):
    t.forward(460)
    t.left(90)
    t.forward(360)
    t.left(90)

def dibuja_letra(trazos):
    for x1, y1, x2, y2 in trazos:
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)

t.color("red")
t.width(10)

trazos_L = [
    (-190, 100, -190, -100),
    (-190, -100, -120, -100),
]

trazos_H = [
    (90, 100, 90, -100),
    (160, 100, 160, -100),
    (90, 0, 160, 0),
]

dibuja_letra(trazos_L)
dibuja_letra(trazos_H)

cx, cy, r = 10, 0, 100
angulo = 60
start_x = cx + r * math.cos(math.radians(angulo))
start_y = cy + r * math.sin(math.radians(angulo))

t.penup()
t.goto(start_x, start_y)
t.setheading(150)
t.pendown()
t.circle(r, 240)

turtle.mainloop()
