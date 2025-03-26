# Créé par nsi, le 27/01/2025 en Python 3.7
import random

def grille_border(Longueur,Largueur):
    return [[0 for i in range(2*Longueur-1)] for e in range(2*Largueur-1)]

def additionvec(T,t):
    return (T[0]+t[0],T[1]+t[1])

def liste_case_suivante(grille_jeu,directions,Longueur,Largueur):
    L=[]
    m=-1
    n=-1
    longueur= len(grille_jeu)
    largeur=len(grille_jeu[1])
    for e in grille_jeu:
        m+=1
        n=-1
        for i in e:
            n+=1
            if e[n]==0:
                coordonne=(m,n)
                for a in directions:
                    new=additionvec(a,coordonne)
                    if 0<=new[0]<longueur-1 and 0<=new[1]<largeur:
                        if grille_jeu[new[0]][new[1]]==1:
                            L+=[coordonne]
    return L



def poser_carte(grille_jeu,cpt,Longueur,Largueur):
    if cpt==0:
        grille_jeu[Largueur-1][Longueur-1]=1
    elif cpt==Longueur*Largueur-1:
        print("Vous avez complété le pateau")
        print("X --> case vide \n1 --> carte")
        verifier_grille(grille_jeu,Longueur,Largueur)
        emplacement_possible=liste_case_suivante(grille_jeu,directions,Longueur,Largueur)
        coordonne_choisi=emplacement_possible[random.randint(0,len(emplacement_possible)-1)]
        grille_jeu[coordonne_choisi[0]][coordonne_choisi[1]]=1
        verifier_grille(grille_jeu,Longueur,Largueur)
    else:
        verifier_grille(grille_jeu,Longueur,Largueur)
        emplacement_possible=liste_case_suivante(grille_jeu,directions,Longueur,Largueur)
        coordonne_choisi=emplacement_possible[random.randint(0,len(emplacement_possible)-1)]
        grille_jeu[coordonne_choisi[0]][coordonne_choisi[1]]=1
        verifier_grille(grille_jeu,Longueur,Largueur)
    afficher_grille()

def afficher_grille():
    i=0
    print("=========================================")
    for e in grille_jeu:
        print('  ',i,'   ',e)
        i+=1
    print("=========================================")

def test():
    poser_carte(grille_jeu,cpt,Longueur,Largueur)
    liste_case_suivante(grille_jeu,directions,Longueur,Largueur)
    grille_jeu[6][5]=1
    verifier_grille(grille_jeu,Longueur,Largueur)
    afficher_grille()


def verifier_grille(grille_jeu,Longueur,Largueur):
    for i in range(2*Largueur-1):
        for e in range(Longueur-1):
            if grille_jeu[i][e]==1:
                for a in range(2*Largueur-1):
                    for b in range(e+Longueur,2*Longueur-1) :
                        grille_jeu[a][b]="X"
    for i in range(2*Largueur-1):
        for e in range(Longueur,2*Longueur-1):
            if grille_jeu[i][e]==1:
                for a in range(2*Largueur-1) :
                    for b in range(e-Longueur+1):
                        grille_jeu[a][b]="X"
    for i in range(Largueur):
        for e in range(2*Longueur-1):
            if grille_jeu[i][e]==1:
                for b in range(2*Largueur-2,Largueur+i-1,-1):
                    grille_jeu[b]=["X" for _ in range(2*Longueur-1)]
    for i in range(Largueur,2*Largueur-1):
        for e in range(2*Longueur-1):
            if grille_jeu[i][e]==1:
                for b in range(0,i-Largueur+1):
                    grille_jeu[b]=["X" for _ in range(2*Longueur-1)]














#===========================================================
directions = [ (-1, 0), (0, -1), (0, 1), (1, 0)]

cpt=0
Longueur=5
Largueur=5
grille_jeu= grille_border(Longueur,Largueur)

for i in range(25):
    poser_carte(grille_jeu,cpt,Longueur,Largueur)
    cpt+=1
