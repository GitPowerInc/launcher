#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 13:14:01 2025

@author: Adrien
"""

from json import load

def affiche(dico,categorieG=" ",categorie1=" ",categorie2=" ") :
    if categorie1 != " " : categorie1 += ":"
    if categorieG != " " : categorieG += " :"
    cles = dico.keys()
    print(categorieG)
    for e in cles :
        print("\t- ",categorie1,e," : ",dico[e],categorie2)


with open("stats_du_tueur.json", "r") as stats :
    stats_tout = load(stats)
    
score = stats_tout[0]
temps = stats_tout[1]

affiche(score,"score MAX","Lv")
print("\n\n")
affiche(temps,"temps MAX","Lv","s")