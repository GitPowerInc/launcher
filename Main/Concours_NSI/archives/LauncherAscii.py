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
    "tueur_d_ovni": ["pygame", "tkinter"],
    "chatbot --console": ["os", "json"],
    "chatbot --interface": ["customtkinter", "tkinter", "tkinterdnd2"],
    "bonhome_de_neige": []
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
        emplacement = os.path.join(emplacement, "tueur_d_ovni")
        pgrm = "tueur_d_ovni_V4.3.py"
    elif pgrm == "chatbot --console":
        emplacement = os.path.join(emplacement, "chatbot")
        pgrm = "chatbot_V_5.py"
    elif pgrm == "chatbot --interface":
        emplacement = os.path.join(emplacement, "chatbot")
        pgrm = "chatbot_V_7.0.0.py"
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
    print("ça continuuuuuuuuuuuu!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


def h(y):
        return f"   O\n  /|\\\n  / \\\n   |\n   v\n—{'—' * 11}—\n| Etage: {y} |\n—{'—' * 11}—\n"

def jouer() :
    galerie = [[(i,j) for j in range(5)] for i in range(5)]
    print(galerie)
    long = len(galerie)-1
    larg = len(galerie[0])-1
    dico_pgrm = {}
    x,y=0,0
    etage=["Jeux","Outils","Illusions"]
    hom=f"   O\n  /|\\\n  / \\\n   |\n   v\n—{'—' * 11}—\n| Etage: {y} |\n—{'—' * 11}—\n"

    dico_pgrm[galerie[0][0]] = "tueur_d_ovni"

    dico_pgrm[galerie[1][0]] = "chatbot --console"
    dico_pgrm[galerie[2][0]] = "chatbot --interface"

    dico_pgrm[galerie[3][0]] = "bases"

    dico_pgrm[galerie[4][0]] = "bonhome_de_neige"


    coord_perso = (0,0)

    inp = ""

    print("Bienvenue a la gallerie, vous etes actuellement au Rez de Chaussee")
    print(hom)
    print("choix par input : ")
    print(" - déplacement :\n\t monter un etage (m)\n\t descendre un etage(d)\n\t entrer dans l'etage (e)")
    print(" quitter et fermer le laucher (q)")
    
    
   ## print(" - déplacement :\n\t gauche(g)\n\t droite(d)\n\t haut(h)\n\t bas(b)\n\t")
   ## print(" - lancer le programme correspondant à la case où on est (l)")
    
    c=""
    
    while inp != "q":
        choix = input("votre choix : ")
        if choix == "d" and y > 0:
            y -= 1
        elif choix == "m" and y < 2:
            y += 1
        coord_perso = (x, y)
        if choix == "e":
            print("\n\n - déplacement :\n\t gauche(g)\n\t droite(d)\n\t sortir de l'etage(h)")
            print(f"programme actuel:{dico_pgrm[galerie[x][y]]}")
            print(" - lancer le programme correspondant à la case où on est (l)")
            while c != "h":
                c = input("votre choix : ")
                if c == "l":
                    launch(dico_pgrm[coord_perso])
                    print("pgrm exécuté avec succès !")
                else:
                    if c == "g" and x > 0:
                        x -= 1
                    elif c == "d" and x < 4:
                        x += 1
                    coord_perso = (x, y)
                    print(f"programme actuel:{dico_pgrm[galerie[x][y]]}")
                
        else: 
            print(h(y))
    
    return


if __name__ == "__main__":
    jouer()
