#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:46:00 2025

@author: Adrien, V
"""
import os
from subprocess import run
from os import getcwd
import sys

depends = {
    "tueur_d_ovni": ["pygame", "os", "json", "random", "math", "sys"],
    "chatbot --console": ["os", "json", "random"],
    "chatbot --interface": ["customtkinter", "tkinterdnd2", "os", "json", "random"],
    "bonhome_de_neige": ["turtle"]
}

def deps(pgrm):
    manquant = []
    for module in depends.get(pgrm, []):
        try:
            __import__(module)
        except ImportError:
            manquant.append(module)

    if manquant:
            import tkinter as tk
            from tkinter import messagebox

            root = tk.Tk()
            root.withdraw()
            msg = f"Modules manquants pour {pgrm}:\n\n" + "\n".join(manquant)
            messagebox.showerror("Erreur de dépendances", msg)
            root.destroy()
    return True

def launch(pgrm):
    if not deps(pgrm): return

    emplacement = os.path.join(getcwd(), "Programmes")

    if pgrm == "tueur_d_ovni":
        emplacement = os.path.join(emplacement, "tueur_d_ovni_C")
        pgrm = "tueur_d_ovni_V4.3.py"

    elif pgrm == "chatbot --console":
        emplacement = os.path.join(emplacement, "chatbot_C")
        pgrm = "chatbot_V_5.py"
    elif pgrm == "chatbot --interface":
        emplacement = os.path.join(emplacement, "chatbot_C")
        pgrm = "chatbot_V_7.0.0.py"

    elif pgrm == "bases" :
        emplacement = os.path.join(emplacement, "bases_C")
        pgrm = "bases_V3.py"

    elif pgrm == "bonhome_de_neige" :
        emplacement = os.path.join(emplacement, "turtle_C")
        pgrm = "Adrien_Lachaize_bonhome_de_neige.py"

    elif pgrm == "etude_trinomes" :
        emplacement = os.path.join(emplacement, "fonctions_C")
        pgrm = "etude_trinome_2nd_degre.py"

    else :
        emplacement += "/defaut_C"
        pgrm = "Jeu_de_la_vie_V_1_0.py"

    print("Emplacement :", emplacement)
    cwd = getcwd()

    if os.name == "posix":
        pgpath = os.path.join(cwd, "LauncherBash.sh")
        if sys.platform == "darwin":
            run(['osascript', '-e',f'tell application "Terminal" to do script "{pgpath} \\"{emplacement}\\" \\"{pgrm}\\""'])
        else:
            run([f"gnome-terminal -- {pgpath} {emplacement} {pgrm}"], shell=True)
            ##run(f'gnome-terminal -- bash -c \'{pgpath} "{emplacement}" "{pgrm}"; exec bash\'',shell=True)
    else:
        run(f'cmd /k "cd /d {emplacement} && python {pgrm}"', shell=True)



def h(y):
        return f"   O\n  /|\\\n  / \\\n   |\n   v\n—{'—' * 11}—\n| Etage: {y} |\n—{'—' * 11}—\n"

def jouer() :
    galerie = [[(i,j) for j in range(5)] for i in range(5)]
    print(galerie)
    long = len(galerie)
    larg = len(galerie[0])
    dico_pgrm = {}
    description_pgrm = {}

    dico_pgrm[galerie[0][0]] = "tueur_d_ovni"
    description_pgrm[galerie[0][0]] = """
    Le jeu Tueur D'Ovnis consiste en la destruction d'ovnis qui veulent anéantir
    la race humaine pour prendre le contrôle de cette suberbe planète qu'est la
    Terre afin d'étendre leur domination de l'univers à l'héliosphère.
    Vous devez défendre notre planète et empêcher les Perséens de nous envahir.
    Bon courage et Bonne chasse !!"""


    dico_pgrm[galerie[1][0]] = "chatbot --console"

    dico_pgrm[galerie[2][0]] = "chatbot --interface"


    dico_pgrm[galerie[3][0]] = "bases"


    dico_pgrm[galerie[4][0]] = "bonhome_de_neige"


    dico_pgrm[galerie[0][1]] = "etude_trinomes"


    print(dico_pgrm)


    coord_perso = (0,0)
    choix = ""
    print("Vous êtes dans une galerie d'art dans laquelle vous pouvez vous déplacer chaque case correspond à un programme que vous pouvez exécuter (certaines cases sont vides)")
    print("/!\ les programmes sont exécuter dans le terminal et certaines fonctionnaliyés peuvent ne pas être disponibles, merci de votre compréhension")

    x,y=0,0
    etage=["Jeux","Outils","Illusions"]
    hom=f"   O\n  /|\\\n  / \\\n   |\n   v\n—{'—' * 11}—\n| Etage: {y} |\n—{'—' * 11}—\n"

    coord_perso = (0,0)
    inp = ""
    choix = ""

    print("Bienvenue a la gallerie, vous etes actuellement au Rez de Chaussee")
    print(hom)
    print("choix par input : ")
    print(" - déplacement :\n\t monter un etage (m)\n\t descendre un etage(d)\n\t entrer dans l'etage (e)")
    print(" quitter et fermer le laucher (q)")

    while inp != "q":
        inp = input("votre choix : ")
        if inp == "d" and y > 0:
            y -= 1
        elif inp == "m" and y < 2:
            y += 1
        x=0
        coord_perso = (x, y)

        if inp == "e":
            print("\n\n - déplacement :\n\t gauche(g)\n\t droite(d)\n\t sortir de l'etage(h)")

            if galerie[x][y] in dico_pgrm :
                print(f"programme actuel:{dico_pgrm[galerie[x][y]]}")
                if galerie[x][y] in description_pgrm :
                    print(f"descripton:\n{description_pgrm[galerie[x][y]]}")
                else : print("aucune description disponible pour l'instant")
            else : print("aucun programme sur cette case ==> programme par défaut")

            print(" - lancer le programme correspondant à la case où on est (l)")


            while choix != "h":
                choix = input("votre choix : ")
                if choix == "l":
                    try :
                        launch(dico_pgrm[coord_perso])
                    except Exception() :
                        launch("defaut")
                        print("programme par défaut exécuter")
                    finally :
                        print("pgrm exécuté avec succès !")

                else:
                    if choix == "g" and x > 0:
                        x -= 1
                    elif choix == "d" and x < 4:
                        x += 1
                    coord_perso = (x, y)
                    print(x,y)

                    if galerie[x][y] in dico_pgrm :
                        print(f"programme actuel:{dico_pgrm[galerie[x][y]]}")
                        if galerie[x][y] in description_pgrm :
                            print(f"descripton:\n{description_pgrm[galerie[x][y]]}")
                        else : print("aucune description disponible pour l'instant")
                    else : print("aucun programme sue cette case ==> programme par défaut")

        else:
            print(h(y))

    return


if __name__ == "__main__":
    jouer()
    print("merci d'avoir utilisé notre launcher ;)")
