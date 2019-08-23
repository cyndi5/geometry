import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor('white')
Cyndi = turtle.Turtle()
Cyndi.speed(0)
Cyndi.color('black')
rotate = int(360)


def drawCircles(t, size):
    colors = ['white smoke', 'light gray', 'dark gray', 'dim gray']
    for i in range(4):
        t.color(colors[i])
        t.circle(size)
        size = size - 4


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)


drawSpecial(Cyndi, 70, 7)
# hide the cursor/turtle
Cyndi.hideturtle()
# keep holding the screen until closed manually
wn.mainloop()