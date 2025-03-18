# auteurs : Adrien Lachaize et Anatole Couix
#version : 5   -optimisée-

import random
import json
import os

numdata = input("entrez le numéro de data de votre chat bot (si vous n'en avez pas entrez 0 et si vous voulez en créer un tapez 1) ")

if numdata=="chat_bot" or numdata=='chat bot':
    with open("data/chat_bot_data.json", "r") as data :
        dicorep = json.load(data)
    fichier_data = 3

else:
    if int(numdata)==1:
        numdata = input("entrez un numéro de data \n")
        if not os.path.isfile("data/chatbot_data_" + numdata + ".json") :
            data = open("data/chatbot_data_" + numdata + ".json", "w")
            data.write('{"bonjour": ["...", "bye"], "salut": ["tu a bien mang\u00e9", "euhh rebonjour ?", "comment ca va ?"], "\u00e7a va ?": ["super et toi ?", "tr\u00e8s bien merci et toi ?", "OOUII", "oui"]}')
            print("nouveau fichier data créé et enregistré comme 'chatbot_data_" + numdata + ".json'" )
        else :
            print("ce numéro de data est déjà occupé, veuillez recommencer la procédure de création de data")
            exit()

    #load le dictionnaire à partir du fichier data
    if int(numdata)==0:
        with open("data/chatbot_data_0.json", "r") as data :
            dicorep = json.load(data)
        fichier_data = 2

    else :
        if not os.path.isfile("data/chatbot_data_" + numdata + ".json"):
            print("ce numéro de data n'existe pas veuillez dréer ce data ou en choisir un autre")
            exit()
        with open("data/chatbot_data_" + numdata + ".json", "r") as data :
            dicorep = json.load(data)
            fichier_data = 1


#print(dicorep)

#définit les mots qui ne doivent pas être appris
blacklist = ['bye']

#premier tour de boucle

if fichier_data == 3:
    robot = "miaou"
else:
    robot = "bonjour"
inp = 0
total=0
#print(dicorep)

question_liste = []
rep_liste = []
liste = list(dicorep)
for i in range(len(liste)):
    if not '?' in liste[i]:
        rep_liste.append(liste[i])

#boucle principale
while inp != "bye":
    inp = input(robot + "\n")
    total+=1
    if not inp in blacklist:
        dicorep[robot].append(inp)

    if not inp in dicorep and not inp in blacklist :
        dicorep[inp]=[]
        if not inp in rep_liste and not '?' in inp :
            rep_liste.append(inp)

    if inp!="bye" and dicorep[inp] != [] and dicorep[inp] !='bye' :
        robot = random.choice(dicorep[inp])

    else :
        if inp in ("quoi","quoi?","quoi ?") :
            inutile=0

        elif "?" in inp:
            robot = random.choice(rep_liste)

        else :
            robot = random.choice(list(dicorep))



# sauvegarde des datas
if fichier_data == 1:
    with open("data/chatbot_data_" + numdata + ".json", "w") as data :
        json.dump(dicorep, data, indent = 4, separators = (",", ":"))
        print('sauvegarde du fichier chatbot_data_' + numdata + '.json terminée')

elif fichier_data == 3:
    with open("data/chat_bot_data.json", "w") as data :
        json.dump(dicorep, data, indent = 4, separators = (",", ":"))
        print('sauvegarde du fichier chat_bot_data.json terminée')

else :
    with open("data/chatbot_data_0.json", "w") as data :
        json.dump(dicorep, data, indent = 4, separators = (",", ":"))
        print('sauvegarde du fichier chatbot_data_0.json terminée')
print("avec ", len(list(dicorep)), " répliques différentes disponibles et ", total*2, " échangées")
