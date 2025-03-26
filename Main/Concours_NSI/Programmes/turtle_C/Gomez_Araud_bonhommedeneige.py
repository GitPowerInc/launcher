# Créé par nsi, le 19/12/2024 en Python 3.7
import turtle as t
import random

def sol():
    t.penup()
    t.width(50)
    for i in range(60):
        t.penup()
        t.goto(-500,-100-i*5)
        t.color(0/255,(30+i*0.8)/255,0/255)
        t.pendown()
        t.forward(1000)

def boule(x, y, radius):
    t.setheading(0)
    t.width(1)
    t.color("white")
    for i in range(40):
        t.penup()
        t.setheading(90)
        t.goto(x-i*0.01*radius+radius, y)
        t.pendown()
        t.color((120+i*3)/255, (120+i*3)/255, (135+i*3)/255)
        t.fillcolor((120+i*3)/255, (120+i*3)/255, (135+i*3)/255)
        t.begin_fill()
        t.circle(radius-i*2)
        t.end_fill()

def moon():
    t.penup()
    for i in range(40):
        t.penup()
        t.setheading(90)
        t.goto(400-i*1.3,250)
        t.pendown()
        t.color((150+i*2)/255, (150+i*2)/255, (135+i*3)/255)
        t.fillcolor((150+i*2)/255, (150+i*2)/255, (135+i*3)/255)
        t.begin_fill()
        t.circle(70-i*1.3)
        t.end_fill()
    t.penup()
    t.color(0,0,0)


def boule_corp(x, y, radius):
    boule(x, y, radius)
    t.setheading(0)
    t.width(1)
    t.color(135/255, 80/255, 0)
    t.penup()
    t.goto(x + radius * 0.2, y - radius)
    t.setheading(60)
    for i in range(5):
        t.penup()
        t.circle(radius * 1.5, 10)
        t.pendown()
        t.width(radius * 0.1)
        t.circle(radius * 1.5, 2)

def boule_tete(x, y, radius):
    boule(x, y, radius)
    t.color(0,0,0)
    t.fillcolor("black")
    t.setheading(0)
    t.width(1)
    t.penup()
    t.goto(x + radius * 0.7, y + radius * 0.1)
    t.setheading(0)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(radius * 0.05)
    t.end_fill()
    t.penup()
    t.goto(x + radius * 0.1, y + radius * 0.1)
    t.setheading(0)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(radius * 0.05)
    t.end_fill()
    t.penup()
    t.goto(x + radius * 0.5, y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.right(10)
    t.forward(radius * 0.7)
    t.right(160)
    t.forward(radius * 0.7)
    t.end_fill()
    t.penup()
    t.goto(x + radius * 0.5, y)
    t.pendown()
    t.begin_fill()
    t.setheading(180)
    t.circle(radius * 0.12, 180)
    t.end_fill()
    t.penup()
    t.goto(x - radius * 0.9, y + radius * 0.8)
    elipse(radius, (45/255, 45/255, 55/255))
    t.goto(x - radius * 0.6, y + radius * 0.8)
    elipse(radius / 1.5, (235/255, 45/255, 55/255))
    t.goto(x - radius * 0.59, y + radius * 0.8)
    hatpart(radius)
    t.penup()
    t.goto(x - radius * 0.59, y + radius * 0.8)
    t.setheading(105)
    t.forward(radius)
    t.setheading(0)
    elipse(radius * 0.94, (45/255, 45/255, 55/255))

def hatpart(radius):
    t.setheading(105)
    t.width(radius * 0.05)
    t.color(45/255, 45/255, 55/255)
    t.pendown()
    t.fillcolor(25/255, 25/255, 35/255)
    t.begin_fill()
    t.forward(radius)
    t.penup()
    t.setheading(0)
    t.forward(radius * 1.68)
    t.setheading(-105)
    t.pendown()
    t.forward(radius)
    t.end_fill()

def draw_snowman(x, y, rayon):
    t.setheading(0)
    t.width(1)
    t.color("white")
    boule_corp(x, y, rayon * 0.75)
    boule_corp(x, y + rayon * 0.8, rayon * 0.6)
    boule_tete(x, y + rayon * 1.6, rayon * 0.45)
    t.penup()
    t.goto(x - rayon * 0.4, y + rayon)
    t.pendown()
    t.color(125/255, 90/255, 0/255)
    t.setheading(-105)
    t.forward(rayon * 0.5)
    t.setheading(-70)
    t.forward(rayon * 0.5)
    t.setheading(-60)
    t.forward(rayon * 0.2)
    t.right(180)
    t.setheading(-20)
    t.forward(rayon * 0.2)
    t.right(180)
    t.forward(rayon * 0.2)
    t.setheading(-45)
    t.forward(rayon * 0.2)
    t.right(180)
    t.forward(rayon * 0.2)
    t.setheading(-65)
    t.forward(rayon * 0.2)
    t.right(180)
    t.forward(rayon * 0.2)
    t.setheading(-85)
    t.forward(rayon * 0.2)
    t.right(180)
    t.forward(rayon * 0.2)
    t.setheading(10)
    t.forward(rayon * 0.15)
    t.penup()
    t.goto(x + rayon * 0.45, y + rayon * 1.2)
    t.pendown()
    t.color(125/255, 90/255, 0/255)
    t.setheading(60)
    t.forward(rayon * 0.5)
    t.setheading(85)
    t.forward(rayon * 0.5)
    t.setheading(95)
    t.forward(rayon * 0.2)
    t.right(180)
    t.setheading(105)
    t.forward(rayon * 0.2)
    t.right(180)
    t.forward(rayon * 0.2)
    t.setheading(90)
    t.forward(rayon * 0.2)
    t.right(180)
    t.forward(rayon * 0.2)
    t.setheading(75)
    t.forward(rayon * 0.2)
    t.right(180)
    t.forward(rayon * 0.2)
    t.setheading(60)
    t.forward(rayon * 0.2)
    t.right(180)
    t.forward(rayon * 0.2)
    t.setheading(130)
    t.forward(rayon * 0.15)

    t.penup()
    t.goto(1000, 1000)

def draw_triangle(t, size):
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

def draw_star_rays(size):
    t.penup()
    t.goto(-400,350)
    joyeux(size)
    noel(size)

def draw_star_rays2( x, y, size):
    t.penup()
    t.goto(x,y)
    t.penup()
    t.pendown()
    t.color("yellow")
    t.width(0)
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def joyeux(size):
    y=300
    x=-380
    j(x,y,size)
    x=-380+60
    o(x,y,size)
    x=-380+120
    Y(x,y,size)
    x=-380+180
    e(x,y,size)
    x=-380+240
    u(x,y,size)
    x=-380+300
    X(x,y,size)


def noel(size):
    y=200
    x=-300
    n(x,y,size)
    x=-300+60
    o(x,y,size)
    x=-300+110
    e(x,y,size)
    t.penup()
    t.goto(x+5,y+12)
    draw_star(size)
    t.penup()
    t.goto(x+15,y+12)
    draw_star(size)
    x=-300+150
    l(x,y,size)


def l(x,y,size):
    for i in range(5):
        t.penup()
        t.goto(x,y-i*10)
        draw_star( size)
        t.penup()
        t.goto(x,y-i*10)
    for i in range(3):
        t.penup()
        t.goto(x+i*10,y-5*10)
        draw_star( size)
        t.penup()
        t.goto(x+i*10,y-5*10)

def j(x,y,size):
    for i in range(4):
        t.penup()
        t.goto(x+17,y-10-i*10)
        draw_star( size)
        t.penup()
        t.goto(x,y-i*10)
    for i in range(2):
        t.penup()
        t.goto(x+i*10,y-5*10)
        draw_star( size)
        t.penup()
        t.goto(x+i*10,y-5*10)
    for i in range(4):
        t.penup()
        t.goto(x+i*10,y)
        draw_star( size)
        t.penup()
        t.goto(x+i*10,y-5*10)

def u(x,y,size):
    for i in range(5):
        t.penup()
        t.goto(x,y-i*10)
        draw_star( size)
        t.penup()
        t.goto(x+26,y-i*10)
        draw_star(size)
    for i in range(2):
        t.penup()
        t.goto(x+8+i*10,y-5*10)
        draw_star( size)
        t.penup()
        t.goto(x+i*10,y-5*10)

def e(x,y,size):
    for i in range(3):
        t.penup()
        t.goto(x+i*10,y)
        draw_star( size)
        t.penup()
        t.goto(x+i*10,y-3*10)
    for e in range(5):
        t.penup()
        t.goto(x,y-e*10)
        draw_star( size)
        t.penup()
        t.goto(x,y-i*10)
    for i in range(3):
        t.penup()
        t.goto(x+i*10,y-2*10)
        draw_star( size)
        t.penup()
        t.goto(x+i*10,y-3*10)
    for i in range(3):
        t.penup()
        t.goto(x+i*10,y-5*10)
        draw_star( size)
        t.penup()
        t.goto(x+i*10,y-5*10)

def n(x,y,size):
    for i in range(6):
        t.penup()
        t.goto(x,y-i*10)
        draw_star( size)
        t.penup()
        t.goto(x,y-i*10)
    for i in range(5):
        t.penup()
        t.goto(x+i*7,y-10*(i))
        draw_star( size)
        t.penup()
        t.goto(x+i*10,y-5*10)
    for i in range(6):
        t.penup()
        t.goto(x+35,y-i*10)
        draw_star( size)
        t.penup()
        t.goto(x,y-i*10)

def X(x,y,size):
    for i in range(5):
        t.penup()
        t.goto(x+i*7,y-i*12.5)
        draw_star( size)
        t.penup()
        t.goto(x+i*7,y-50+i*12.5)
        draw_star( size)

def Y(x,y,size):
    for i in range(3):
        t.penup()
        t.goto(x+i*7,y-i*12.5)
        draw_star( size)
        t.penup()
        t.goto(x+i*7,y-50+i*12.5)
        draw_star( size)
    for i in range(2):
        t.penup()
        t.goto(x+21+i*7,y-12+i*12.5)
        draw_star(size)


def o(x,y,size):
    for i in range(2):
        t.penup()
        t.goto(x+10+i*10,y)
        draw_star( size)
        t.penup()
        t.goto(x+10+i*10,y-50)
        draw_star( size)
    for i in range(4):
        t.penup()
        t.goto(x,y-8-i*12)
        draw_star( size)
        t.penup()
        t.goto(x+30,y-8-i*12)
        draw_star( size)



def draw_star( size):
    t.penup()
    t.pendown()
    t.color("yellow")
    t.width(0)
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def triangle(size):
    for i in range(20):
        t.pendown()
        t.setheading(0)
        t.color((0/255, (100-i*4)/255, (60-i*3)/255))
        t.fillcolor((0/255, (100-i*4)/255, (60-i*3)/255))
        t.setheading(0)
        t.begin_fill()
        t.forward(size*(1-0.05*i))
        t.setheading(120)
        t.forward(size*(1-0.05*i))
        t.setheading(-120)
        t.forward(size*(1-0.05*i))
        t.end_fill()
        t.penup()
        t.setheading(0)
        t.forward(size*0.025)


def rectangle(size):
    for i in range(20):
        t.pendown()
        t.setheading(0)
        t.color(((80-i*2)/255, (40-i*2)/255, (20-i*1)/255))
        t.fillcolor(((80-i*2)/255, (40-i*2)/255, (20-i*1)/255))
        t.setheading(0)
        t.begin_fill()
        t.forward(size*(1-0.05*i))
        t.setheading(90)
        t.forward(size*2*(1-0.05*i))
        t.setheading(180)
        t.forward(size*(1-0.05*i))
        t.setheading(270)
        t.forward(size*2*(1-0.05*i))
        t.end_fill()
        t.penup()
        t.setheading(0)
        t.forward(size*0.025)



def draw_tree(x,y,size):
    t.penup()
    t.goto(x+size*0.3,y-size*0.3)
    rectangle(size*0.4)
    for i in range(3):
        t.penup()
        t.goto(x+i*7.5,y+i*40)
        triangle(100-i*15)
    t.goto(x+size*0.5,y-size*0.3)



def bouledenoel(x,y,radius,a,b,c):
    t.setheading(0)
    t.width(1)
    for i in range(20):
        t.penup()
        t.setheading(90)
        t.goto(x-i*0.02*radius+radius, y)
        t.pendown()
        t.color((a+i*3)/255,(b+i*3)/255,(c+i*3)/255)
        t.fillcolor((a+i*3)/255,(b+i*3)/255,(c+i*3)/255)
        t.begin_fill()
        t.circle(radius-i*0.2)
        t.end_fill()

def draw_christmas_tree(x,y,size):
    t.penup()
    t.goto(x+size*0.3,y-size*0.3)
    rectangle(size*0.4)
    for i in range(3):
        t.penup()
        t.goto(x+i*15,y+i*size*0.4)
        triangle(size-i*30)
    t.goto(x+size*0.425,y+size*1.45)
    draw_star( 30)
    bouledenoel(-320,-120,10,150,0,0)
    bouledenoel(-360,70,10,150,0,0)
    bouledenoel(-320,-30,10,150,0,0)#===========
    bouledenoel(-320,60,10,0,150,0)
    bouledenoel(-390,-40,10,0,150,0)
    bouledenoel(-310,-90,10,0,150,0)#===========
    bouledenoel(-380,-140,10,0,0,150)
    bouledenoel(-360,-60,10,0,0,150)
    bouledenoel(-400,20,10,0,0,150)



def ciel():
    t.width(100)
    for i in range(40):
        t.penup()
        t.goto(-500,-300+i*20)
        t.color(0/255,0/255,(200-i*5)/255)
        t.pendown()
        t.forward(1000)


def elipse(radius, border):
    t.setheading(0)
    t.width(radius * 0.05)
    t.color(border)
    t.pendown()
    t.fillcolor(25/255, 25/255, 35/255)
    t.begin_fill()
    for i in range(2):
        t.setheading(330 + i * 180)
        t.circle(radius * 1.8, 60)
    t.end_fill()
    t.penup()

t.update()
screen = t.Screen()
screen.bgcolor("midnightblue")

tree = t.Turtle()
t.tracer(0)
ciel()

t.penup()
t.goto(-200,200)
draw_star_rays(8)
for _ in range(110):
    x = random.randint(-450, 450)
    y = random.randint(-100, 500)
    draw_star_rays2( x, y, 8)
sol()

t.penup()
moon()
draw_snowman(50, -200, 200)
t.update()
t.penup()
t.goto(-200,-100)

t.goto(-150,-125)
draw_tree(-280,-100,100)
draw_tree(-200,-165,100)
draw_tree(200,-125,100)
draw_tree(375,-100,100)
draw_tree(300,-220,100)
draw_tree(220,-255,100)
draw_christmas_tree(-450,-150,200)
draw_tree(-450,-250,100)
draw_tree(-270,-292,100)
draw_tree(-360,-325,100)
t.goto(1000,1000)
tree.hideturtle()
t.done()
