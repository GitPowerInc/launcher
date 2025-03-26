import random
import json
import os

#Base de donnée------------------------------------------------------------------------
addition_motcle = ["addition", "adition", "addittion", "adittion", "additions", "aditions", "addittions", "adittions", "1"]
soustraction_motcle = ["soustraction", "soustracion", "soustractions", "soustracions", "2"]
multiplication_motcle = ["multiplication", "multiplications", "3"]
oui_motcle = ["oui","yes","oi","ouais"]
non_motcle = ["non","no","nn"]
difficulte_motcle = {
    "facile": ["easy", "simple", "basic", "simpliste","1"],
    "mediant": ["medium", "intermedière", "intermediere", "normal", "midd", "moyen","2"],
    "difficile": ["hard", "difficult", "complex", "dur", "difficile", "complexe","3"],
    "tres_difficile": ["demon", "extreme","extrème", "démon","4"],
    "impossible": ["secrete","secrète", "impossible","enfer", "diable","42"]
}


# Fonction analyse------------------------------------------------------------------------
def normalize_input(reponse):
    return reponse.lower().strip()

def analyser_difficulte(mot, difficulte_motcle):
    mot = mot.lower().strip()
    for niveau, mots in difficulte_motcle.items():
        if mot in mots:
            return niveau
    return None

def analyse_question(choix):
    reponse = normalize_input(choix)
    if any(ad in reponse for ad in addition_motcle):
        return 1
    elif any(sou in reponse for sou in soustraction_motcle):
        return 2
    elif any(mul in reponse for mul in multiplication_motcle):
        return 3
    elif reponse == "quit":
        return "quit"
    else:
        return -1

def analyse_ouinon(Final_reponse):
    reponse = normalize_input(Final_reponse)
    if any(no in reponse for no in non_motcle):
        return "quit"
    elif any(ou in reponse for ou in oui_motcle):
        return "oui"
    else:
        return -1


def creer_fichier_json(nom_fichier, structure_initiale=None):
    if not os.path.exists(nom_fichier):
        print(f"Chatbot : Création du fichier {nom_fichier}...")
        if structure_initiale is None:
            structure_initiale = {}
        with open(nom_fichier, "w") as fichier:
            json.dump(structure_initiale, fichier, indent=4)
        print(f"Chatbot : Fichier {nom_fichier} créé avec succès.")
    else:
        print(f"Chatbot : Le fichier {nom_fichier} existe déjà.")

def sauvegarder_score(utilisateur, score):
    with open("scores.json", "r+") as fichier:
        data = json.load(fichier)
        data[utilisateur] = data.get(utilisateur, 0) + score
        fichier.seek(0)
        json.dump(data, fichier)

#Fonction générer réponse------------------------------------------------------------------------
def message_bravo(score,choix2,niveau):
    print(f"Chatbot : Vous avez un score de : {score} / {choix2} !")
    if niveau == "impossible":
        if score/10 ==0:
            print("Chatbot : Choqué? Dites vous que vous ne pouvez que progresser")
        elif score/10 <0.5:
            print("Chatbot : Presque la moyenne, ne célèbré pas cela pour autant")
        elif score/10 <0.6:
            print("Chatbot : La moyenne de justesse, pathétique")
        elif score/10 <0.8:
            print("Chatbot : Vous en êtes encore loin...")
        elif score/10 <0.9:
            print("Chatbot : La réussite est à votre portée! mais... Vous avez quand même echoué!")
        elif score/10 ==1:
            print("Chatbot : Les portes vous sont ouvertes, mais rassurez vous, nous nous reverrons très bientôt...")
    if score/choix2 ==0:
        print("Chatbot : On peut difficilement faire pire")
    elif score/choix2 <0.5:
        print("Chatbot : Allez courage on persevère")
    elif score/choix2 <0.6:
        print("Chatbot : La moyenne de justesse")
    elif score/choix2 <0.7:
        print("Chatbot : Mention assez bien, chapeau!")
    elif score/choix2 <0.8:
        print("Chatbot : Mension bien , bravo!")
    elif score/choix2 <0.9:
        print("Chatbot : Mension très bien, exellent! Vous êtes un très bonne element")
    elif score/choix2 <1:
        print("Chatbot : Félicitation du Jury!!! Vous êtes l'avenir de ce pays")
    elif score/choix2 ==1:
        print("Chatbot : La perfection!!! Vous êtes l'avenir de notre espèce")

def generer_calcul(n, nb,niveau,utilisateur):
    cpt = 0
    #niveau impossible --------------------------------------------------
    if niveau == "impossible":
        print("Chatbot : Bienvenue en enfer, desormais vous ne pouvez plus reculer...")
        print("Chatbot : Si vous parvenez à répondre à dix questions sans fautes vous sortez, sinon... Nous avons l'éternité de toute façon, n'est ce pas?")
        for _ in range(10):
            a = random.randint(bornemin, bornemax)
            b = random.randint(bornemin, bornemax)
            op = random.choice(["^", "/", "*"])
            if op == "^":
                c = a ** b
                print(f"Chatbot : Aimez vous les puissances ? Combien font : {b} ^ {a} ? ")
            elif op == "/":
                c = round(a / b, 2)
                print(f"Chatbot : Une simple division ... Combien font : {a} / {b} ? Arrondir au centième.")
            else:
                c = a * b
                print(f"Chatbot : Une multiplication... comme en CP Combien font : {a} * {b} ?")
            try:
                d = float(input(f"{utilisateur} : "))
                if d == c:
                    print("Chatbot : Bon résultat !")
                    cpt += 1
                else:
                    print(f"Chatbot : Faux ! La bonne réponse est : {c}")
            except ValueError:
                print(f"Chatbot : Entrée invalide. La bonne réponse était : {c}")
        return cpt
    #niveau normaux --------------------------------------------------
    if n!=3:
        if niveau == "facile":
            bornemin=0
            bornemax=10
        elif niveau == "mediant":
            bornemin=-10
            bornemax=20
        elif niveau == "difficile":
            bornemin=-100
            bornemax=100
        elif niveau == "tres_difficile":
            bornemin=-1000
            bornemax=1000
    if n==3:
        if niveau == "facile":
            bornemin=0
            bornemax=5
        elif niveau == "mediant":
            bornemin=-10
            bornemax=10
        elif niveau == "difficile":
            bornemin=-20
            bornemax=20
        elif niveau == "tres_difficile":
            bornemin=-100
            bornemax=100
    for _ in range(nb):
        a = random.randint(bornemin, bornemax)
        b = random.randint(bornemin, bornemax)
        if n == 1:
            c = a + b
            print(f"Chatbot : Combien font : {a} + {b} ? ")
        elif n == 2:
            c = a - b
            print(f"Chatbot : Combien font : {a} - {b} ? ")
        elif n == 3:
            c = a * b
            print(f"Chatbot : Combien font : {a} * {b} ? ")
        try:
            d = int(input(f"{utilisateur} : "))
            if d == c:
                print("Chatbot : Bon résultat!")
                cpt += 1
            else:
                print(f"Chatbot : Faux!!! Le bon résultat est : {c}")
        except ValueError:
            print(f"Chatbot : Entrée invalide. Le bon résultat était : {c}")
    return cpt
#Fonction principale-----------------------------------------------------------------------



def quiz(utilisateur):
    reponses = -1
    while reponses == -1:
        print("\n=========================================")
        print("Quelle opération voulez-vous réviser ?")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("Tapez 'quit' pour quitter.")
        print("=========================================")

        choix = input(f"{utilisateur} : ")
        reponses = analyse_question(choix)
        if reponses == "quit":
            return "quit"
        elif reponses == -1:
            print("Chatbot : Entrée invalide. Veuillez réessayer.")
    #--------------------------------------------------
    choix2 = 0
    while choix2 <= 0:
        print("\n=========================================")
        print("Combien de questions voulez-vous ?")
        print("=========================================")
        choix2 = input(f"{utilisateur} : ")
        if choix2.isdigit():
            choix2 = int(choix2)
            if choix2 <= 0:
                print("Chatbot : Veuillez entrer un nombre positif.")
        else:
            print("Chatbot : Entrée invalide. Veuillez entrer un nombre entier positif.")

    #--------------------------------------------------

    print("\n=========================================")
    print("quel niveau de difficulté voulez vous ?")
    print("1. facile")
    print("2. moyen")
    print("3. difficile")
    print("4. demon")
    print("=========================================")
    difficulte = input(f"{utilisateur} : ")
    niveau = analyser_difficulte(difficulte, difficulte_motcle)
    if niveau:
        print(f"Chatbot : Niveau détecté : {niveau}")
    else:
        print("Chatbot : Niveau non reconnu. Veuillez réessayer.")
        verifieur=1
        while verifieur!=0:
            difficulte = input(f"{utilisateur} : ")
            niveau = analyser_difficulte(difficulte, difficulte_motcle)
            if niveau:
                print(f"Niveau détecté : {niveau}")
                verifieur=0
            else:
                print("Chatbot : Niveau non reconnu. Veuillez réessayer.")


    #--------------------------------------------------

    score = generer_calcul(reponses, choix2,niveau,utilisateur)
    message_bravo(score,choix2,niveau)
    print("Chatbot : Souhaitez vous sauvegarder? oui/non")
    sauvgarde= input(f"{utilisateur} : ")
    repsauv = analyse_ouinon(sauvgarde)
    if repsauv == "oui":
        creer_fichier_json("scores.json")
        sauvegarder_score(utilisateur, score)
    elif repsauv == -1:
        verifieur=1
        print("Chatbot : Entrée invalide. Veuillez réessayer.")
        while verifieur == 1:
            print("Chatbot : Souhaitez vous sauvegarder? oui/non")
            sauvgarde= input(f"{utilisateur} : ")
            repsauv = analyse_ouinon(sauvgarde)
            if repsauv == "oui":
                sauvegarder_score(utilisateur, score)
                verifieur=-1
            elif repsauv == "non":
                verifieur=-1
            elif repsauv == -1:
                print("Chatbot : Entrée invalide. Veuillez réessayer.")


    #--------------------------------------------------
    print("Souhaitez vous continuez? oui/non")
    Final_reponse= input(f"{utilisateur} : ")
    rep = analyse_ouinon(Final_reponse)
    if rep == "quit":
            return "quit"
    elif rep == -1:
        print("Chatbot : Entrée invalide. Veuillez réessayer.")
        while rep ==-1:
            print("Chatbot : Souhaitez vous continuez? oui/non")
            Final_reponse= input(f"{utilisateur} : ")
            rep = analyse_ouinon(Final_reponse)
            if rep == "quit":
                    return "quit"
            elif rep == -1:
                print("Chatbot : Entrée invalide. Veuillez réessayer.")
    return None

#Programme principale--------------------------------------------------------------------------



print("\nBienvenue dans le chatbot maths!")
print("\nChatbot : entrez votre nom d'utilisateur")
utilisateur= input("Vous : ")
while True:
    resultat = quiz(utilisateur)
    if resultat == "quit":
        print("Chatbot : Au revoir !")
        break
