# JEU DE LA VIE
from tkinter import *
import random
TAILLE = 600

def init():
    global JEU
    JEU = [ ]
    for i in range(60):
        JEU.append([0]*60) # [0]*60 produit une ligne de 60 zeros

    for i in range(600): # 500
        x = random.randint(0,59)
        y = random.randint(0,59)
        JEU[x][y] = 1
init()
def Affiche():
    canvas.delete("all")
    for x in range(60) :
       for y in range(60) :
           if JEU[x][y] == 1:
             xx = x * 10 # Facteur 10 entre la grille du JEUX de 60 par 60 et la taille de la fennêtre de 600 par 600
             yy = y * 10
             c="red"
             canvas.create_rectangle(xx,yy,xx+10,yy+10,fill=c) # 10 representes le nombre de pixel par case

def CompteVoisins(x,y) :
    count = 0
    V = [(-1,-1), (0,-1),(1,-1),(-1,0),(1,0),(-1,1), (0,1),(1,1)] # V represente les mouvement autour de chaque case -1 deplacement a gauche ou en bas
    for dx,dy in V:
        count += JEU[(x+dx)%60][(y+dy)%60] # %60 car il y a 60 cases de JEU et JEU et de 60 par 60
    return count

def Evolution():
    global JEU
    JEU2 = [ ] # init nouvelle grille vide
    for i in range(60):
        JEU2.append([0]*60)

    for x in range(60) :
       for y in range(60) :
            nbVoisins = CompteVoisins(x,y)

            if JEU[x][y] == 0 and nbVoisins == 3 :
                    JEU2[x][y] = 1

            if JEU[x][y] == 1 and nbVoisins in [2,3] :
                    JEU2[x][y] = 1
    JEU = JEU2

def PROG() :
    Affiche()
    Evolution()
    Mafenetre.after(100,PROG) # apres 100ms la fonction PROG est appelée


# Création de la fenêtre de dessin
Mafenetre = Tk()
Mafenetre.geometry(str(TAILLE) +"x"+str(TAILLE+40))
canvas = Canvas(Mafenetre,width=TAILLE, height=TAILLE, borderwidth=0, highlightthickness=0,bg="lightgray")
canvas.pack()
bouton= Button(Mafenetre,text="init",command=init)
bouton.pack()
Mafenetre.after(100,PROG) # premier appel
Mafenetre.mainloop()
