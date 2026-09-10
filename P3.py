import turtle
import math

x, y = map(float, input("Ingrese las coordenadas del centro del circulo: ").split())
r = float(input("Ingrese el radio del circulo: "))

area = math.pi * r * r
texto = "%.2f" % area

t = turtle.Turtle()
t.color("red")
t.penup()
t.goto(x, y - r)
t.pendown()
t.circle(r)

t.penup()
t.goto(x, y)
t.color("blue")
t.write(texto, align="center", font=("Arial", 10, "normal"))

turtle.mainloop()
