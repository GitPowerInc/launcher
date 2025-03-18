#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:46:00 2025

@author: Adrien
"""
from subprocess import run
from os import getcwd

def launch(pgrm) :
    emplacement = getcwd()+"/Programmes"

    if pgrm == "tueur_d_ovni" :
        emplacement += "/tueur_d_ovni_C"
        pgrm = "tueur_d_ovni_V4.3.py"

    elif pgrm == "chatbot --console" :
        emplacement += "/chatbot_C"
        pgrm = "chatbot_V_5.py"
    elif pgrm == "chatbot --interface" :
        emplacement += "/chatbot_C"
        pgrm = "chatbot_V_7.0.0.py"

    elif pgrm == "bases" :
        emplacement += "/bases_C"
        pgrm = "bases_V3.py"

    elif pgrm == "bonhome_de_neige" :
        emplacement += "/turtle_C"
        pgrm = "Adrien_Lachaize_bonhome_de_neige.py"

    elif pgrm == "etude_trinomes" :
        emplacement += "/fonctions_C"
        pgrm = "etude_trinome_2nd_degre.py"

    else :
        emplacement += "/defaut_C"
        pgrm = "Jeu_de_la_vie_V_1_0.py"
        print("exec")

    print(emplacement)
    run([ f"gnome-terminal -- {getcwd()}/LauncherBash.sh {emplacement} {pgrm} " ] , shell=True)

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
    dico_pgrm[galerie[0][1]] = "chatbot --console"
    dico_pgrm[galerie[0][2]] = "chatbot --interface"
    dico_pgrm[galerie[0][3]] = "bases"
    dico_pgrm[galerie[0][4]] = "bonhome_de_neige"
    dico_pgrm[galerie[1][0]] = "etude_trinomes"
    print(dico_pgrm)


    coord_perso = (0,0)
    choix = ""
    print("Vous êtes dans une galerie d'art dans laquelle vous pouvez vous déplacer chaque case correspond à un programme que vous pouvez exécuter (certaines cases sont vides)")
    print("choix par input : ")
    print(" - déplacement :\n\t - gauche(g)\n\t - droite(d)\n\t - haut(h)\n\t - bas(b)")
    print(" - lancer le programme correspondant à la case où on est (l)")
    print(" - quitter et fermer le laucher (e)")


    while choix != "e" :
        print("\n\n")
        print(coord_perso)
        print("programme correspondant à votre case : ")
        if coord_perso in dico_pgrm :
            if coord_perso in description_pgrm :
                print(description_pgrm[coord_perso])
            else :
                print(f"\taucune description pour {dico_pgrm[coord_perso]}")
        else :
            print("aucun programmme particulier, pgrm par défaut disponible")
        choix = input("votre choix : ")
        if choix == "l" :
            if coord_perso in dico_pgrm :
                pgrm = dico_pgrm[coord_perso]
            else :
                pgrm = "defaut"
            launch(pgrm)
            print(f"programme {pgrm} exécuté !")
        elif choix == "g" :
            coord_perso = ( coord_perso[0] , (coord_perso[1]-1)%larg )
            print("déplacement à gauche effectué")
        elif choix == "d" :
            coord_perso = ( coord_perso[0] , (coord_perso[1]+1)%larg )
            print("déplacement à droite effectué")
        elif choix == "h" :
            coord_perso = ( (coord_perso[0]-1)%long , coord_perso[1])
            print("déplacement en haut effectué")
        elif choix == "b" :
            coord_perso = ( (coord_perso[0]+1)%long , coord_perso[1])
            print("déplacement en bas effectué")


    return "Merci d'avoir utiliser ce launcher mais vous auriez pu l'utiliser plus longtemps '_° "
