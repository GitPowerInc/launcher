# Créé par user, le 30/11/2024 en Python 3.7

import turtle
turtle.speed(0)


def carre_noir():
    turtle.pendown()
    turtle.color("black")
    turtle.fillcolor("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(26)
        turtle.right(90)
        turtle.forward(26)
        turtle.right(90)
    turtle.forward(26)
    turtle.end_fill()

def carre_blanc():
    turtle.pendown()
    turtle.color("white")
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.setheading(0)
    for _ in range(2):
        turtle.forward(26)
        turtle.right(90)
        turtle.forward(26)
        turtle.right(90)
    turtle.forward(26)
    turtle.end_fill()

def carre_blanc_verticaux():
    carre_blanc()
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(6)
    turtle.setheading(270)
    turtle.forward(2)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("black")
    turtle.fillcolor("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(18)
    turtle.setheading(0)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()


def carre_noir_verticaux():
    carre_noir()
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(6)
    turtle.setheading(270)
    turtle.forward(2)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("white")
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(18)
    turtle.setheading(0)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()

def carre_blanc_verticaux2():
    carre_blanc()
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(24)
    turtle.setheading(270)
    turtle.forward(2)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("black")
    turtle.fillcolor("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(18)
    turtle.setheading(0)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()


def carre_noir_verticaux2():
    carre_noir()
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(24)
    turtle.setheading(270)
    turtle.forward(2)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("white")
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(18)
    turtle.setheading(0)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()

def carre_noir_horizontaux():
    carre_noir()
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(24)
    turtle.setheading(270)
    turtle.forward(2)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("white")
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(18)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()

def carre_blanc_horizontaux():
    carre_blanc()
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(24)
    turtle.setheading(270)
    turtle.forward(2)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("black")
    turtle.fillcolor("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(18)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()

def carre_noir_horizontaux2():
    carre_noir()
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(24)
    turtle.setheading(270)
    turtle.forward(18)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("white")
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(18)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()

def carre_blanc_horizontaux2():
    carre_blanc()
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(24)
    turtle.setheading(270)
    turtle.forward(18)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("black")
    turtle.fillcolor("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(18)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()



def carre_noir_diagaunaux():
    carre_noir()
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(24)
    turtle.setheading(270)
    turtle.forward(2)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("white")
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(18)
    turtle.setheading(270)
    turtle.forward(18)
    turtle.setheading(0)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()

def carre_blanc_diagaunaux():
    carre_blanc()
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(24)
    turtle.setheading(270)
    turtle.forward(2)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("black")
    turtle.fillcolor("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(18)
    turtle.setheading(270)
    turtle.forward(18)
    turtle.setheading(0)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()

def carre_noir_diagaunaux2():
    carre_noir()
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(7)
    turtle.setheading(270)
    turtle.forward(2)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("white")
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(17)
    turtle.setheading(270)
    turtle.forward(18)
    turtle.setheading(0)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()

def carre_blanc_diagaunaux2():
    carre_blanc()
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(6)
    turtle.setheading(270)
    turtle.forward(2)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("black")
    turtle.fillcolor("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(18)
    turtle.setheading(270)
    turtle.forward(18)
    turtle.setheading(0)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(4)
        turtle.right(90)
        turtle.forward(4)
        turtle.right(90)
    turtle.end_fill()

def noir_blanc(c,l):
    if c%2==0:
        if l%2==0:
            return 0
        return 1
    if c%2!=0:
        if l%2==0:
            return 1
        return 0

def tableau_couleur(n):
    L=[]
    T=[]
    for c in range(n):
        for l in range(n):
            couleur= noir_blanc(c,l)
            T = T+ [couleur]
        L =L + [copie(T)]
        T=[]
    return L


def copie(T):
    U=[]
    for element in T:
        U= U+ [element]
    return U

def addition_tableau(L,V):
    T=[]
    J=[]
    W=[]
    N=[]
    longueur = len(L)
    for i in range(longueur):
        J= L[i]
        W= V[i]
        for e in range(longueur):
            couleur_motif = W[e]+ J[e]
            T= T+ [couleur_motif]
        N= N + [copie(T)]
        T=[]
    return N

def afficher_tableau(L):
    longueur = len(L)
    for i in range(longueur):
        print(L[i])

def tableau_motif(n):
    L=[]
    T=[]
    if n%2==0:
        for c in range(n):
            for l in range(n):
                if c==((n/2)-1) or c==(n/2):#------------------------------------------------
                    if l==((n/2)-1) or l==(n/2):#000000000000000000000
                        T=T+[0]
                    elif l<(n/2):#000000000000000000000
                        T=T+[6]
                    elif l>(n/2):#000000000000000000000
                        T=T+[8]
                elif c<(n/2):#----------------------------------------------------------------
                    if l==((n/2)-1) or l==(n/2):#000000000000000000000
                        T=T+[2]
                    elif l<(n/2):#000000000000000000000
                        if l+3>(n/2)-c:
                            T=T+[10]
                        else:
                            T=T+[0]
                    elif l>(n/2):#000000000000000000000
                        if l<=n/2+c+1:
                            T=T+[12]
                        else:
                            T=T+[0]
                elif c>(n/2):#---------------------------------------------------------------
                    if l==((n/2)-1) or l==(n/2):#000000000000000000000
                        T=T+[4]
                    elif l<(n/2):#000000000000000000000
                        if l+1 +(n/2)>=c:
                            T=T+[12]
                        else:
                            T=T+[0]
                    elif l>(n/2):#000000000000000000000
                        if 1.5*n-l+1>c:
                            T=T+[10]
                        else:
                            T=T+[0]
            L =L + [copie(T)]
            T=[]
        return L
    if n%2!=0:
        for c in range(n):
            for l in range(n):
                if c==((n-1)/2):#------------------------------------------------
                    if l==((n-1)/2):#000000000000000000000
                        T=T+[0]
                    elif l<(n/2):#000000000000000000000
                        T=T+[6]
                    elif l>((n-1)/2):#000000000000000000000
                        T=T+[8]
                elif c<((n-1)/2):#----------------------------------------------------------------
                    if l==((n-1)/2):#000000000000000000000
                        T=T+[2]
                    elif l<((n-1)/2):#000000000000000000000
                        if l+1>=((n-1)/2)-c:
                            T=T+[10]
                        else:
                            T=T+[0]
                    elif l>((n-1)/2):#000000000000000000000
                        if l<=((n-1)/2)+c+1:
                            T=T+[12]
                        else:
                            T=T+[0]
                elif c>((n-1)/2):#---------------------------------------------------------------
                    if l==((n-1)/2):#000000000000000000000
                        T=T+[4]
                    elif l<((n-1)/2):#000000000000000000000
                        if l +((n-1)/2)+1>=c:
                            T=T+[12]
                        else:
                            T=T+[0]
                    elif l>((n-1)/2):#000000000000000000000
                        if 1.5*n-l>c:
                            T=T+[10]
                        else:
                            T=T+[0]
            L =L + [copie(T)]
            T=[]
        return L

def quelle_motif_couleur(a):
    if a%2==0:
        if a==0:
            carre_noir()
        elif a==2:
            carre_noir_horizontaux2()
        elif a==4:
            carre_noir_horizontaux()
        elif a==6:
            carre_noir_verticaux()
        elif a==8:
            carre_noir_verticaux2()
        elif a==10:
            carre_noir_diagaunaux2()
        elif a==12:
            carre_noir_diagaunaux()
    elif a%2!=0:
        if a==1:
            carre_blanc()
        elif a==3:
            carre_blanc_horizontaux2()
        elif a==5:
            carre_blanc_horizontaux()
        elif a==7:
            carre_blanc_verticaux()
        elif a==9:
            carre_blanc_verticaux2()
        elif a==11:
            carre_blanc_diagaunaux2()
        elif a==13:
            carre_blanc_diagaunaux()


def dessiner_illusion(n,L):
    J=[]
    if n%2==0:
        x=-(n/2)*27
        y=(n/2)*27
        turtle.penup()
        turtle.goto(x,y)
        for c in range(n):
            J= L[c]
            y=((n/2)-c)*27
            turtle.penup()
            turtle.goto(x,y)
            for l in range(n):
                x=-(n/2)*27+(l*27)
                turtle.penup()
                turtle.goto(x,y)
                a= J[l]
                quelle_motif_couleur(a)
    if n%2!=0:
        x=-(n/2)*27+13.5
        y=(n/2)*27+13.5
        turtle.penup()
        turtle.goto(x,y)
        for c in range(n):
            J= L[c]
            y=((n/2)-c)*27+13.5
            turtle.penup()
            turtle.goto(x,y)
            for l in range(n):
                x=-(n/2)*27+(l*27)+13.5
                turtle.penup()
                turtle.goto(x,y)
                a= J[l]
                quelle_motif_couleur(a)


def illusion(n):
    if type(n)!=int or n<0:
        exit(" le nombre de lignes doit être un entier positif ")
    if n==0:
        turtle.goto(0,0)
        return None
    if n==1:
        carre_noir()
        return None
    L=tableau_couleur(n)
    V=tableau_motif(n)
    N =addition_tableau(L,V)
    dessiner_illusion(n,N)





























#n= int(input(" combien de lignes voulez vous : "))
n=int(input("combien de ligne voulez vous : "))
turtle.tracer(0)
illusion(n)





turtle.penup()
turtle.goto(1000,1000)
turtle.update()


turtle.hideturtle()
turtle.exitonclick()