# EdCoWNY STEAM (08/2019) - turtle demo (by Eric Bray, ebray@gow.org)
# square.py

import turtle

leo = turtle.Turtle()
canvas = turtle.Screen()

leo.speed(5)
leo.shape("turtle")
leo.color("blue")

leo.forward(100)
leo.left(90)

leo.forward(100)
leo.left(90)

leo.forward(100)
leo.left(90)


canvas.exitonclick()
