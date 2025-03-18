"""
 auteurs : Adrien Lachaize et Anatole Couix
version : 7.0.0  - optimisée, avec interface CustomTkinter, avec une validation des deux répliques (robot + joueur)  -
"""
#ce programme utilise de nombreux modules qui ne sont pas présents par défaut,
# il est donc nécessaire de tous les installer si ce n'est pas fait ,
# vous pouvez trouver leurs noms ci-dessous

######################################################################################

# importation des modules demandés
try :
    import random
    import json
    import os
    import customtkinter
    import tkinterdnd2
    from sys import exit

    ######################################################################################

    #fonction principale du chatbot
    def fonction_princip(robot):
        global dicorep
        print(robot)
        inp=reponse.get()
        print(inp)
        global inp_bis

        if inp != "bye":
            if not inp in blacklist and not inp in dicorep[robot]:
                dicorep[robot].append(inp)

            if not inp in dicorep and not inp in blacklist :
                dicorep[inp]=[]
                if not inp in rep_liste and not '?' in inp :
                    rep_liste.append(inp)

            if inp!="bye" and dicorep[inp] != [] and dicorep[inp] !='bye' :
                robot = random.choice(dicorep[inp])

            else :
                if not inp in ("quoi","quoi?","quoi ?"):
                    if "?" in inp:
                        robot = random.choice(rep_liste)
                    else :
                        robot = random.choice(list(dicorep))

            demande.delete(0 , len(demande.get()))
            demande.insert(0, robot)
            inp_bis = reponse.get()
            reponse.delete(0 , len(inp_bis))

            return robot
        else:
            app.quit()

    ######################################################################################

    # fonction "tampon" pour les paramètres de la principale
    def fonction_tk():
        global texte
        robot=texte
        texte=fonction_princip(robot)

    ######################################################################################

    # fonction pour que la réplique donnée par le chatbot vis-à-vis de la précedente réponse de l'utilisateur
    def validation_replique():
        inp=inp_bis
        robot=demande.get()
        if inp in dicorep :
            if not robot in dicorep[inp] :
                dicorep[inp].append(robot)

        else :
            dicorep[inp] = []
            dicorep[inp].append(robot)

    ######################################################################################

    #fonction permettant de valider la réplique de l'utilisateur à l'aide la touche entrée
    def touche(event):
        t = event.keysym
        if t == "KP_Enter":
            fonction_tk()

    ######################################################################################

    #fonction permettant de passer du theme clair au theme sombre et inversement
    def chgt_theme():
        global theme_moi
        if theme_moi == "b" :
            customtkinter.set_appearance_mode("dark")
            theme_moi = "n"
        elif theme_moi == "n" :
            customtkinter.set_appearance_mode("light")
            theme_moi = "b"


    ######################################################################################
    ######################################################################################


    # préremplissage de la variable de base de donnée en cas de non assignation par bug
    fichier_data=0
    numdata = input("entrez le numéro de data de votre chat bot (si vous n'en avez pas entrez 0 et si vous voulez en créer un tapez 1) ")

    # load le dictionnaire à  partir du fichier data
    if numdata=="chat_bot" or numdata=='chat bot':
        with open("data/chat_bot_data.json", "r") as data :
            dicorep = json.load(data)
        fichier_data = 3

    else:
        if numdata=="1":
            numdata = input("entrez un numéro de data \n")
            if not os.path.isfile("data/chatbot_data_" + numdata + ".json") :
                data = open("data/chatbot_data_" + numdata + ".json", "w")
                data.write('{"bonjour": ["...", "bye","salut"] , "bye":["bye"] , "euhh rebonjour ?":["salut"] , "...":["euhh rebonjour ?"] , "salut": ["euhh rebonjour ?", "ça va ?"] , "\u00e7a va ?": ["super et toi ?"] , "super et toi ?":["super"] , "super":["cool"] , "cool":["super"] }')
                print("nouveau fichier data créé et enregistré comme 'chatbot_data_" + numdata + ".json'" )

            else :
                print("ce numéro de data est déjà  occupé, veuillez recommencer la procédure de création de data")
                exit()


        if numdata=="0":
            with open("data/chatbot_data_0.json", "r") as data :
                dicorep = json.load(data)
            fichier_data = 2

        else :
            if not os.path.isfile("data/chatbot_data_" + numdata + ".json"):
                print("ce numéro de data n'existe pas veuillez créer ce data ou en choisir un autre")
                exit()
            with open("data/chatbot_data_" + numdata + ".json", "r") as data :
                dicorep = json.load(data)
                fichier_data = 1


    ######################################################################################

    #définit les mots qui ne doivent pas être appris
    blacklist = ['bye']

    #premier tour de boucle -initialisation des varibles -
    if fichier_data == 3:
        texte = "miaou"
        robot = texte
    else:
        texte = "bonjour"
        robot = texte

    inp = 0

    question_liste = []
    rep_liste = []
    liste = list(dicorep)
    for i in range(len(liste)):
        if not '?' in liste[i]:
            rep_liste.append(liste[i])

    ######################################################################################

    # création de la fenetre principale
    largeur=500
    global theme_moi
    theme_moi = "n"

    customtkinter.set_ctk_parent_class(tkinterdnd2.Tk)

    # mise en place du thème sombre (chgt possible)
    customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

    # création de la fenètre en elle-même
    app = customtkinter.CTk()
    app.geometry(str(largeur)+"x255")
    app.title("chatbot_V_7.0.0")

    # configuration de la zone où seront affichées les répliques du chatbot
    demande = customtkinter.CTkEntry( master = app , width=largeur*4 , height=18 , placeholder_text = "réplique du chatbot" , font=("Arial" , 16))
    demande.pack(pady=13, padx=0)
    demande.delete(0)
    demande.insert(0, texte)

    # configuration de la zone où l'utilisateur rentre ses répliques
    reponse = customtkinter.CTkEntry( master = app , width=largeur*4 , height=18 , placeholder_text = "insérez votre réplique" , font=("Arial" , 16))
    reponse.pack(pady=20, padx=0)
    reponse.delete(0 , len(reponse.get()))

    # bouton pour valider la réplique de l'utilisateur
    valider = customtkinter.CTkButton( master = app , text = "Valider" , command = fonction_tk , height=25 , font=("Arial" , 14))
    valider.pack(pady=8 , padx=10)

    # bouton pour que la réplique donnée par le chatbot vis-à-vis de la précedente réponse de l'utilisateur
    ok = customtkinter.CTkButton( master = app , text = "C'est OK" , command = validation_replique , height=25 , font=("Arial" , 14))
    ok.pack(pady=11 , padx=10)

    # bouton pour passer du thème clair au thème sombre et inversement
    chgt_theme = customtkinter.CTkButton( master = app , text = "Theme clair/sombre" , command = chgt_theme , height=23 , font=("Arial" , 13))
    chgt_theme.pack(pady=0 , padx=10)

    # pour accéder à la fonction de détection de touche
    app.bind("<Key>", touche)

    # affichage de la fenêtre principale
    app.mainloop()

    ######################################################################################

    # sauvegarde des datas
    if fichier_data == 1:
        with open("data/chatbot_data_" + numdata + ".json", "w") as data :
            json.dump(dicorep, data, indent = 4, separators = (",", ":"))
            print('sauvegarde du fichier chatbot_data_' + numdata + '.json terminée')
            numdata="chatbot_data_ " + numdata

    elif fichier_data == 3:
        with open("data/chat_bot_data.json", "w") as data :
            json.dump(dicorep, data, indent = 4, separators = (",", ":"))
            print('sauvegarde du fichier chat_bot_data.json terminée')
            numdata="chat_bot_data"

    else :
        with open("data/chatbot_data_0.json", "w") as data :
            json.dump(dicorep, data, indent = 4, separators = (",", ":"))
            print('sauvegarde du fichier chatbot_data_0.json terminée')
            numdata="chatbot_data_0"
    print("avec ",len(list(dicorep)), "répliques différentes disponibles")

    # création de la fenêtre indiquant la sauvegarde réussite du dictionnaire
    save = customtkinter.CTk()
    save.geometry(str(largeur)+"x25")
    save.title('chatbot_V_7.0.0 : sauvegarde')

    txt = customtkinter.CTkLabel(master=save , text='sauvegarde du fichier ' + numdata + '.json terminée' , font=("Arial" , 18) )
    txt.pack()

    # affichage de la fenêtre
    save.mainloop()

except ModuleNotFoundError :
    print("les modules suivants sont requis pour l'exécution du programme : \nrandom \njson \nos \ncustomtkinter \ntkinterdnd2 \nsys \n\npour les installer, exécutez la commande pip install NomDuModule dans votre terminal ou la console python")
