import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.width(3)

def flecha(x, y, angulo, color, largo):
    t.penup()
    t.goto(x, y)
    t.setheading(angulo)
    t.pendown()
    t.color(color)
    t.forward(largo)
    t.right(150)
    t.forward(12)
    t.backward(12)
    t.left(300)
    t.forward(12)
    t.backward(12)
    t.right(150)

flecha(60, 70, 180, "green", 120)
flecha(-70, 70, 270, "blue", 120)
flecha(-60, -70, 0, "red", 120)
flecha(70, -70, 90, "orange", 120)

screen.mainloop()
