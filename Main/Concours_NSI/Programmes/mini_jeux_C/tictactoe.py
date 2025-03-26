import random

# Mots-clés --------------------------------------------------------------
morpion_motcle = ["morpion", "tic tac toe", "tictactoe", "jeu", "jouer"]
commencer_motcle = ["commencer", "start", "début", "debut"]
regle_motcle = ["règle", "regle", "règles", "regles", "rule", "rules"]
cases_motcle = {str(i): i for i in range(9)}  # Permet d'associer les nombres 0-8 à eux-mêmes

# texte -----------------------------------------
def simplifier(reponse):
    return reponse.lower().strip()

def debut_partie(reponse):
    reponse_simplifie = simplifier(reponse)
    if any(reg in reponse_simplifie for reg in regle_motcle):
        return "regle"
    elif any(deb in reponse_simplifie for deb in commencer_motcle):
        return "start"
    return "inconnu"

# Fonctions du jeu -------------------------------------------------------
def afficher_grille(grille):
    print("\n")
    for i in range(3):
        print(" | ".join(grille[i*3:(i+1)*3]))
        if i < 2:
            print("-" * 9)
    print("\n")

def verifier_victoire(grille, joueur):
    combinaisons_gagnantes = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)              
    ]
    return any(all(grille[i] == joueur for i in combinaison) for combinaison in combinaisons_gagnantes)

def grille_pleine(grille):
    return all(cell != " " for cell in grille)

def ordi_joue(grille):
    coups_possibles = [i for i in range(9) if grille[i] == " "]
    return random.choice(coups_possibles) if coups_possibles else None

# Programme principal ----------------------------------------------------
print("Bienvenue dans le Morpion ! Tapez 'règle' pour voir les règles, 'début' pour commencer, et 'quit' pour quitter.")

while True:
    utilisateur = input("Vous: ")
    if utilisateur.lower() == "quit":
        print("Bot : Au revoir !")
        break

    reponse = debut_partie(utilisateur)
    if reponse == "inconnu":
        print("Bot : Je ne comprends pas.")
    elif reponse == "regle":
        print("Bot : Le Morpion se joue sur une grille 3x3. Chaque joueur place à tour de rôle son symbole (X ou O). Le premier qui aligne 3 symboles gagne !")
    elif reponse == "start":
        print("Bot : Commençons !")
        grille = [" "] * 9
        joueur_actuel = "X"

        while True:
            afficher_grille(grille)
            if joueur_actuel == "X":
                utilisateur = input("Entrez un chiffre (0-8) pour jouer: ")
                coup_joueur = simplifier(utilisateur)
                if coup_joueur in cases_motcle and grille[cases_motcle[coup_joueur]] == " ":
                    grille[cases_motcle[coup_joueur]] = "X"
                else:
                    print("Bot : Coup invalide ! Réessayez.")
                    continue
            else:
                coup_ordi = ordi_joue(grille)
                grille[coup_ordi] = "O"
                print(f"Bot joue en case {coup_ordi}")
            if verifier_victoire(grille, joueur_actuel):
                afficher_grille(grille)
                print(f"Bot : Le joueur {joueur_actuel} a gagné !")
                break
            if grille_pleine(grille):
                afficher_grille(grille)
                print("Bot : Match nul !")
                break
            joueur_actuel = "O" if joueur_actuel == "X" else "X"
