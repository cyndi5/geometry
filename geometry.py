import turtle
import math
import random
turtle.setup(512,512)
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

def spinCircle(t, size, repeat):
    for i in range(repeat):
        t.color('black')
        t.circle(size)
        t.right(360 / repeat)

def crescents(t, size, repeat):
    t.color('black')
    t.penup()
    t.goto(60,-150)
    move_amount = [-80, -50, 30, 0]

    fill_color = ['black','white smoke','black','white smoke']
    for i in range(repeat):
        t.color(fill_color[i])
        t.fillcolor(fill_color[i])
        t.begin_fill()
        t.pendown()
        t.circle(size, steps=50)
        t.penup()
        t.end_fill()
        if move_amount[i] > 0:
            t.forward(move_amount[i])
        else:
            t.back(abs(move_amount[i]))



crescents(Cyndi, 150, 4)

# hide the cursor/turtle
Cyndi.hideturtle()
# keep holding the screen until closed manually
wn.mainloop()