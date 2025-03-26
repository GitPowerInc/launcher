import random

#mots clés--------------------------------------------------------------

pierre_motcle = [
    "caillou", "galet"," pierraille"," roc", "rocher","pierre","piere",
]

ciseaux_motcle = [
    "ciseaux","ciseau","siseaux"
]
feuille_motcle = [
    "feuille","feuilles","feuile","papier","papiers"
]
commencer_motcle = [
    "commencer","commence","comencer","comence","start","début","debut"
]

regle_motcle = [
    "rule","rules","règle","regle","règles","regles"
]

#fonction--------------------------------------------------------------

def simplifier(reponse):
    return reponse.lower().strip()
#apparament ça supprime les majuscules et les espaces

def debut_partie(reponse):
    reponse_simplifie = simplifier(reponse)
    if any(reg in reponse_simplifie for reg in regle_motcle):
        return "regle"
    elif any(deb in reponse_simplifie for deb in commencer_motcle):
        return "start"
    return "inconnu"

def ordi():
    a=random.randint(1,3)
    if a==1:
        return "pierre"
    if a==2:
        return "feuille"
    if a==3:
        return "ciseau"

def jeux(reponse):
    reponse_simplifie = simplifier(reponse)
    if any(pie in reponse_simplifie for pie in pierre_motcle):
        return "pierre"
    elif any(eau in reponse_simplifie for eau in ciseaux_motcle):
        return "ciseau"
    elif any(feu in reponse_simplifie for feu in feuille_motcle):
        return "feuille"
    return "inconnu"

def regles(coup_ordi,coup_joueur):
    if coup_joueur=="pierre" :
        if coup_ordi=="ciseau":
            return("vous avez gagné")
        if coup_ordi=="pierre":
            return("il y a égalité")
        if coup_ordi=="feuille" :
            return("vous avez perdu")
    if coup_joueur=="ciseau" :
        if coup_ordi=="feuille":
            return("vous avez gagné")
        if coup_ordi=="ciseau":
            return("il y a égalité")
        if coup_ordi=="pierre":
            return("vous avez perdu")
    if coup_joueur=="feuille":
        if coup_ordi=="pierre":
            return("vous avez gagné")
        if coup_ordi=="feuille":
            return("il y a égalité")
        if coup_ordi=="ciseau":
            return("vous avez perdu")



#programme principale

print("Bienvenue dans le jeux pierre feuille ciseaux ! Taper 'regle' pour avoir les règle et 'début' pour commencer et 'quit' pour arreter.")

while True:
    utilisateur = input("Vous: ")
    if utilisateur.lower() == "quit":
        print("bot : Au revoir !")
        break
    reponse = debut_partie(utilisateur)
    if reponse=="inconnu":
        print("bot : Je ne comprends pas.")
    if reponse=="regle":
        print("bot : Rappel des règles : La pierre bat les ciseaux,les ciseaux battent la feuille et la feuille bat la pierre. Si les deux joueurs jouent le même symbole, il y a égalité. Il n'y a pas de puit!!!")
    if reponse=="start":
        print("bot : Commençons!")
        while True:
            utilisateur = input("Vous: ")
            if utilisateur.lower() == "quit":
                break
            coup_ordi = ordi()
            print("bot : ", coup_ordi)
            coup_joueur = jeux(utilisateur)
            conclution=regles(coup_ordi, coup_joueur)
            print("bot : ",conclution)
    if utilisateur.lower() == "quit":
        print("bot : Au revoir !")
        break