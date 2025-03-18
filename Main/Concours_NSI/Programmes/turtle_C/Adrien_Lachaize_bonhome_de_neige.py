#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 21:00:47 2024

@author: jasta
"""

import turtle as ttl
from random import randint
# ce programme a été réalisé en python 3.12,
# les formules par construction des listes utilisées ne fonctionnent pas 
# dans toutes les versions


def arriere_plan() :
    
    ttl.up()
    ttl.goto(-500,300)
    ensemble_nuage(1)
    
    ttl.up()
    ttl.goto(-500,60)
    chaine_montagnes(1)
    ttl.up()
    ttl.goto(-500,40)
    chaine_montagnes(0.6)
    
    sol()
    

def premier_plan() :
    ttl.up()
    ttl.goto(160,-320)
    ttl.right(0)
    bonhome_de_neige(1.5)
    
    ttl.up()
    ttl.goto(-280,-250)
    ttl.right(0)
    sapin(1)
    
    for _ in range(randint(30,50)) :
        flocon(int(randint(7,18)/10))
    
    

def chaine_montagnes (num) :
    if num == 1 :
        l = randint(7,10)
    else :
        l = randint(13,20)
    k = [e:=randint(10,20)*num for _ in range(int(2*l*(1/num)))]
    ttl.down()
    for i in range(l) :
        montagne(k[i])
        
def montagne(k) :
    c1 = 14
    c2 = 20
    n2 = 5
    
    # montagne :
    ttl.fillcolor('grey')
    ttl.begin_fill()
    ttl.down()
    ttl.forward(c1*k)
    ttl.left(110)
    ttl.forward(c2*k)
    ttl.left(140)
    ttl.forward(c2*k)
    ttl.end_fill()
    
    # neige sur montagne
    ttl.fillcolor('white')
    ttl.left(180)
    ttl.up()
    ttl.forward((c2-n2)*k)
    ttl.down()
    ttl.begin_fill()
    ttl.forward(n2*k)
    ttl.right(140)
    ttl.forward(n2*k)
    ttl.end_fill()
    
    ttl.up()
    ttl.forward((c2-n2)*k)
    ttl.left(70)
    ttl.forward(randint(-5,-2)*k)
    
    
    
    
def ensemble_nuage(num) :
    l = randint(4,6)
    k = [e:=randint(10,20)*num for _ in range(int(2*l*(1/num)))]
    for i in range(l) :
        nuage(k[i])
    ttl.color("black")
        
def nuage(k) :
    r1 = 4
    r2 = 5
    r3 = 2
    r4 = 3
    r5 = 7
    
    cercle_nuage(r1,k)
    cercle_nuage(r2,k)
    cercle_nuage(r3,k)
    cercle_nuage(r4,k)
    cercle_nuage(r5,k)
    
def cercle_nuage(r,k) :
    r = r*k
    ttl.down()
    ttl.fillcolor('white')
    ttl.color("white")
    ttl.begin_fill()
    ttl.circle(r)
    ttl.end_fill()
    ttl.up()
    ttl.forward(r+randint(-4,-1))
    
    
    
    
def sol() :
    color = "#F0F8FF"
    ttl.up()
    ttl.goto(-500,40)
    ttl.right(0)
    ttl.down()
    ttl.fillcolor(color)
    ttl.color(color)
    ttl.begin_fill()
    for _ in range(2) :
        ttl.forward(1000)
        ttl.right(90)
        ttl.forward(440)
        ttl.right(90)
    ttl.end_fill()
    ttl.color("black")
    
    
    
def bonhome_de_neige(k) :    
    tete , r1 , r2 = corps(k)
    chapeau(k)
    
    ttl.up()
    ttl.goto(160,-320)

    visage(k,tete,r2)
    
    ttl.up()
    ttl.goto(160,-320+r1)
    
    boutons(k,r1)
    
    
def corps(k) :
    r1 = 80*k
    r2 = 50*k
    ttl.down()
    ttl.fillcolor("white")
    ttl.begin_fill()
    ttl.circle(r1)
    ttl.end_fill()
    ttl.up()
    ttl.left(90)
    ttl.forward(2*r1-(r2/2-4))
    ttl.right(90)
    ttl.forward(2)
    ttl.right(0)
    ttl.down()
    ttl.begin_fill()
    ttl.circle(r2)
    ttl.end_fill()
    
    ttl.up()
    ttl.left(90)
    ttl.forward(r2*2-6)
    ttl.right(90)
    
    return (2*r1-(r2/2-4))+r2 ,r1 , r2
    
    
def chapeau(k) :
    c1 = 50*k
    c2 = 4*k
    
    c3 = 30*k
    c4 = 35*k
    
    ttl.fillcolor("black")
    ttl.color("black")
    ttl.right(0)
    ttl.begin_fill()
    ttl.forward(int(c1/2))
    ttl.left(90)
    ttl.forward(c2)
    ttl.left(90)
    ttl.forward(c1)
    ttl.left(90)
    ttl.forward(c2)
    ttl.left(90)
    ttl.forward(int(c1/2))
    ttl.end_fill()
    
    ttl.up()
    ttl.left(90)
    ttl.forward(c2)
    ttl.right(90)
    ttl.down()
    ttl.begin_fill()
    ttl.forward(int(c3/2))
    ttl.left(90)
    ttl.forward(c4)
    ttl.left(90)
    ttl.forward(c3)
    ttl.left(90)
    ttl.forward(c4)
    ttl.end_fill()
    
    
def visage(k,tete,r2) :
    oeuil = 4*k #taille oeuil
    n1 = 10*k   #taille nez
    n2 = 30*k  #
    ttl.up()
    ttl.left(180)
    ttl.forward(tete+13*k)
    r2 = r2 - 25*k
    ttl.right(90)
    ttl.fillcolor("black")
    ttl.forward(r2)
    #oeuil 1
    ttl.begin_fill()
    ttl.down()
    ttl.circle(oeuil)
    ttl.end_fill()
    #deplacement
    ttl.up()
    ttl.backward(2*r2)
    #oeuil 2
    ttl.begin_fill()
    ttl.down()
    ttl.circle(oeuil)
    ttl.end_fill()
    #deplacement
    ttl.up()
    ttl.forward(r2)
    ttl.right(90)
    ttl.forward(r2-15*k)
    ttl.left(90)
    #nez
    ttl.fillcolor("orange")
    ttl.begin_fill()
    ttl.forward(n1)
    ttl.right(140)
    ttl.forward(n2)
    ttl.end_fill()
    

def boutons(k,r1) :
    b = 7*k
    r1 = r1-40*k
    ttl.left(50)
    
    ttl.fillcolor("black")
    ttl.begin_fill()
    ttl.circle(b)
    ttl.end_fill()
    
    ttl.up()
    ttl.forward(r1)
    ttl.begin_fill()
    ttl.circle(b)
    ttl.end_fill()
    
    ttl.up()
    ttl.backward(2*r1)
    ttl.begin_fill()
    ttl.circle(b)
    ttl.end_fill()
    
    
def sapin(k) :
    tronc(k)
    feuillage(k)
    etoile(k)
    
def tronc(k) :
    c1 = 35*k
    c2 = 50*k
    ttl.right(90)
    ttl.fillcolor("brown")
    ttl.begin_fill()
    ttl.forward(int(c1/2))
    ttl.left(90)
    ttl.forward(c2)
    ttl.left(90)
    ttl.forward(c1)
    ttl.left(90)
    ttl.forward(c2)
    ttl.left(int(c1/2))
    ttl.end_fill()
    ttl.left(73)
    ttl.forward(int(c1/2))
    ttl.left(180)
    
def feuillage(k) :
    c1 = 200*k
    c2 = 365*k
    ttl.fillcolor("green")
    ttl.color("green")
    ttl.backward(int(c1/2))
    ttl.begin_fill()
    ttl.forward(c1)
    ttl.left(108)
    ttl.forward(c2)
    ttl.end_fill()

def etoile(k) :
    e = 20*k
    ttl.color("yellow")
    ttl.fillcolor("yellow")
    ttl.up()
    x,y = ttl.pos()
    ttl.goto(x-20,y+20)
    ttl.begin_fill()
    for _ in range(10) :
        ttl.right(146)
        ttl.forward(e)
        ttl.left(110)
        ttl.forward(e)
    ttl.end_fill()


def flocon(k):
    f = 15*k
    ttl.up()
    ttl.goto(randint(-450, 450), randint(-400, 400))
    ttl.down()
    ttl.color("#00BFFF")
    for _ in range(6):
        ttl.forward(f)
        ttl.backward(f)
        ttl.right(60)


def joyeux_noel():
    ttl.up()
    ttl.goto(-170,-390)
    ttl.down()
    ttl.write("Joyeux Noël !",font=("Arial",36,"bold"))


ttl.screensize(950,800)
ttl.speed(0)

screen = ttl.Screen()
screen.bgcolor("sky blue")

arriere_plan()
premier_plan()
joyeux_noel()

ttl.hideturtle()
ttl.exitonclick()