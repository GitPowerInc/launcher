#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 10:56:52 2024

@author: drayen
version : 4.3

Le jeu Tueur D'Ovnis consiste en la destruction d'ovnis qui veulent anéantir
la race humaine pour prendre le contrôle de cette suberbe planète qu'est la
Terre afin d'étendre leur domination de l'univers à l'héliosphère.
Vous devez défendre notre planète et empêcher les Perséens de nous envahir.
Bon courage et Bonne chasse !!

règles :
- Le joueur se situe en bas de l'écran et peut se déplacer de droite à gauche grâce aux flêches de droites et gauches.
- Pour tirer des missiles il faut cliquer sur la flêche du haut ou sur la touche espace.
- vous avez droit à 15 missiles max à la fois
- Les ovnis apparaissent en haut de l'écran à une position aléatoire.
- Un ovni détruit vous fait gagner 1 point.
- Chaque ovni qui touche le sol vous fait perdre 5 points.

succès disponibles :
  1- nombre d'ovnis qui ont touché le sol / sont passés :
      - l'indifférent (plus de dix ovnis passés -exclus-)
      - le soldat mitigé  (2 à 10 ovnis passés -inclus-)
      - le défenseur universel (1 seul ovni passé)

  2- nombre d'ovnis touchés / détruits :
      - l'ovni (moins de 10 ovnis tués)
      - le bon soldat (10 à 175 ovnis tués non inclus)
      - le tueur aguerri (175 à 250 ovnis tués)
      - le sauveur ultime (plus de 250 ovnis tués)

  3- nombre de missile tirés :
      - le dépensier (plus de 17 missiles pour tuer un ovni)
      - le prudent (4 -non inclu- à 17 -inclu- missiles utilisés pour tuer un ovni)
      - l'économe (4 missiles utilisés pour tuer un ovni)
"""

try :
    # importation des modules requis :
    import pygame as pg
    from random import randint
    from os import path , getcwd
    from json import load , dump
    from math import ceil
    from sys import exit

    # =============================================================================
    #    fenètre de demande de difficulté
    # =============================================================================
    pg.init()

    demande_difficulte = pg.display.set_mode((1000,260))
    pg.display.set_caption("Tueur d'ovni : difficulte")
    police2 = pg.font.SysFont("Arial", 25)
    freq = pg.time.Clock()
    pas_termine = True
    pas_aide = True
    difficulte = "-1"

    debut = "tapez h pour l'aide"
    zone_debut = police2.render( debut, True, [102,205,0])
    diff = "difficulté du jeu (entre 1 et 15 -en hexadécimal- ) : "
    zone_diff = police2.render( diff, True, [102,205,0])
    zone_son = police2.render ("tapez s pour couper le son", True, [102,205,0])
    zone_bon_courage = police2.render( "Bonne chasse !  °,,°", True, [0,191,255])

    aide = ("Le jeu Tueur D'Ovnis consiste en la destruction d'ovnis qui veulent anéantir "
    "la race humaine pour prendre le contrôle de cette suberbe planète qu'est la "
    "Terre afin d'étendre leur domination de l'univers à l'héliosphère. "
    "Vous devez défendre notre planète et empêcher les Perséens de nous envahir. "
    "Bon courage et Bonne chasse !!\n"
    "\n\n"
    "règles :\n\n"
    "- Le joueur se situe en bas de l'écran et peut se déplacer de droite à gauche grâce aux flêches de droites et gauches.\n"
    "- Pour tirer des missiles il faut cliquer sur la flêche du haut ou sur la touche espace.\n"
    "- vous avez droit à 15 missiles max à la fois\n"
    "- Les ovnis apparaissent en haut de l'écran à une position aléatoire.\n"
    "- Un ovni détruit vous fait gagner 1 point.\n"
    "- Chaque ovni qui touche le sol vous fait perdre 5 points.\n"
    "\n\n"
        "\nsuccès disponibles : \n\n"
   "1- nombre d'ovnis qui ont touché le sol / sont passés :\n"
       "- l'indifférent (plus de dix ovnis passés -exclus-)\n"
       "- le soldat mitigé (2 à 10 ovnis passés -inclus-)\n"
       "- le défenseur universel (1 seul ovni passé)\n"
   "\n"
   "2- nombre d'ovnis touchés / détruits : \n"
       "- l'ovni (moins de 10 ovnis tués) \n"
       "- le bon soldat (10 à 175 ovnis tués non inclus) \n"
       "- le tueur aguerri (175 à 250 ovnis tués) \n"
       "- le sauveur ultime (plus de 250 ovnis tués) \n"
   "\n"
   "3- nombre de missiles tirés : \n"
       "- le dépensier (plus de 17 missiles pour tuer un ovni) \n"
       "- le prudent (4 -non inclu- à 17 -inclu- missiles utilisés pour tuer un ovni) \n"
       "- l'économe (4 missiles utilisés pour tuer un ovni) \n \n \n"
       "les niveaux de difficulté sont organisés en 2 parties : \n"
       "- le premier (difficulté de 1 à 4) fait seulement varier le nombre de missiles \n"
       "- le deuxième (difficulté de 5 à 15) fait varier le nombre de missiles et la fréquence d'apparition des ovnis \n"
       "De ce fait la difficulté est seulement croissante au sein de ces deux divisions \n"
       "La difficulté augmente au cours du temps à partir de la 4.3"
       "\n"
       "Le score actuel du joueur s'affiche en haut à gauche de l'écran de jeu"
       "Le temps de jeu s'affiche en haut à droite de l'écran de jeu"
       "\n")

    son = True

    while pas_termine :
        event = pg.event.Event(pg.USEREVENT)    #
        for event in pg.event.get() :           # on vérifie si l'utilisateur demande à fermar la fenêtre
            if event.type == pg.QUIT :          #  en appuyant sur la croix
               pas_termine = False              #

        KeysPressed = pg.key.get_pressed() # récupère la liste des touches appuyée
        demande_difficulte.fill([0,0,0])# met l'arrière plan en noir


        if difficulte in "aide" :
            pas_aide = False
        elif difficulte in "123456789101112131415" :
            pas_termine = False

        if not pas_aide :


            demande_difficulte.blit(pg.font.SysFont("Arial", 25).render( "pressez q pour quitter" , True, [102,205,0]),(350,22))
            demande_difficulte.blit(pg.font.SysFont("Arial", 25).render( "pour une aide plus complète, référez vous à aide.txt ou au print de la console" , True, [102,205,0]),(30,62))
            demande_difficulte.blit(pg.font.SysFont("Arial", 25).render( "déplacement joueur : flèche droite ou gauche" , True, [102,205,0]),(30,102))
            demande_difficulte.blit(pg.font.SysFont("Arial", 25).render( "tir missile : flèche haut ou espace" , True, [102,205,0]),(30,142))
            demande_difficulte.blit(pg.font.SysFont("Arial", 25).render( "1 ovni tué = +1 pt         1 ovni au sol = -5 pts" , True, [102,205,0]),(30,182))



        elif son :
            demande_difficulte.blit(zone_debut,(390,12))
            demande_difficulte.blit(zone_son,(350,42))
            demande_difficulte.blit(zone_diff,(230,82))
            demande_difficulte.blit(zone_bon_courage,(370,182))

        else :
            demande_difficulte.blit(zone_debut,(390,12))
            demande_difficulte.blit(zone_diff,(230,52))
            demande_difficulte.blit(zone_bon_courage,(370,182))

        if KeysPressed[pg.K_q] :
            pg.quit()
            print(aide)
            exit("sortie de programme avant de jouer  :( ")

        if KeysPressed[pg.K_h] :
            difficulte = "a"
        elif KeysPressed[pg.K_1] or KeysPressed[pg.K_KP1] :
            difficulte = "1"
        elif KeysPressed[pg.K_2] or KeysPressed[pg.K_KP2] :
            difficulte = "2"
        elif KeysPressed[pg.K_3] or KeysPressed[pg.K_KP3] :
            difficulte = "3"
        elif KeysPressed[pg.K_4] or KeysPressed[pg.K_KP4] :
            difficulte = "4"
        elif KeysPressed[pg.K_5] or KeysPressed[pg.K_KP5] :
            difficulte = "5"
        elif KeysPressed[pg.K_6] or KeysPressed[pg.K_KP6] :
            difficulte = "6"
        elif KeysPressed[pg.K_7] or KeysPressed[pg.K_KP7] :
            difficulte = "7"
        elif KeysPressed[pg.K_8] or KeysPressed[pg.K_KP8] :
            difficulte = "8"
        elif KeysPressed[pg.K_9] or KeysPressed[pg.K_KP9] :
            difficulte = "9"
        elif KeysPressed[pg.K_a] :
            difficulte = "10"
        elif KeysPressed[pg.K_b] :
            difficulte = "11"
        elif KeysPressed[pg.K_c] :
            difficulte = "12"
        elif KeysPressed[pg.K_d] :
            difficulte = "13"
        elif KeysPressed[pg.K_e] :
            difficulte = "14"
        elif KeysPressed[pg.K_f] :
            difficulte = "15"

        if son and KeysPressed[pg.K_s] :
            son = False

        pg.display.flip() # affiche l'image dessinée à l'écran

        freq.tick(25)


    # =============================================================================
    # initialisation des variables :
    # =============================================================================

    difficulte = int(difficulte)
    if difficulte > 15 or difficulte < 0 :
        difficulte = 10
    if ceil(difficulte/4) < 2 :
        nb_max_missiles = int(40 / difficulte)
        freq_apparition_ovni = int(70) # plus c'est petit plus il y a d'ovnis
    else :
        nb_max_missiles = int(200 / difficulte)
        freq_apparition_ovni = int(70 / ceil(difficulte/4)) # plus c'est petit plus il y a d'ovnis

    print(difficulte)
    print(nb_max_missiles)
    print(freq_apparition_ovni)


    if path.isfile("stats_du_tueur.json") :
        with open("stats_du_tueur.json", "r") as stats :
            stats_tout = load(stats)
        tbl_types = stats_tout[0]
        temps = stats_tout[1]
        max_temps = temps[str(difficulte)]
        max_score = tbl_types[str(difficulte)]
    else :
        tbl_types = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0,"13":0,"14":0,"15":0}
        temps = tbl_types
        stats = open("stats_du_tueur.json", "w")
        with open("stats_du_tueur.json", "w") as stats :
            dump([tbl_types,temps], stats, indent = 4, separators = (",", ":")) #, indent = 4, separators = (",", ":")
        max_score = 0
        max_temps = 0

    # constantes utilisées :
    Vert = [102,205,0]
    Rouge = [220,20,60]
    Blanc = [255,255,255]
    Noir = [0,0,0]
    duree_explosion = 50 #en nombre de tours (25 tours/secondes)
    nb_fps = 25

    # variables :
    not_termine = True
    nb_tours = 0
    previous_nb = 0
    nb_ovni = 1
    score = 0
    score_max_partie = 0
    # pour les animations
    a_exploser = []
    # pour les succès
    nb_ovnis_tues = 0
    nb_ovnis_arrives = 0
    nb_missiles_tires = 0

    screenWidth = 900 #600
    screenHeight = 500 #400
    pg.quit()
    Speed = { "x_ovni" : 0 , "y_ovni" : 2 ,
             "x_player" : 7 , "y_player": 0 ,
             "x_missile" : 0 , "y_missile" : 6
        }

    ovni_x = []
    ovni_y = []

    missile_x = []
    missile_y = []

    player_x = 300
    player_y = screenHeight - 10

    # =============================================================================
    # initialisation de la fenetre pygame et de l'image d'arrière plan
    # =============================================================================
    pg.init()

    if son :
        musique_de_fond = "musique_fond.mp3"
        if path.isfile(musique_de_fond) :
            pg.mixer.init()
            pg.mixer.music.load ( musique_de_fond )  #recupère la  musique de fond
            pg.mixer.music.play(-1)  #joue la  musique en boucle

    screen = pg.display.set_mode((screenWidth,screenHeight)) # Definition fenetre de jeux
    pg.display.set_caption("Tueur D'Ovnis")

    fps = pg.time.Clock()

    emplacement_image = getcwd()+'/img_font_tueur_d_ovni.jpeg'
    print(emplacement_image)
    is_image = path.isfile(emplacement_image)

    if is_image :
        arriere_plan = pg.image.load(emplacement_image)
        arriere_plan = arriere_plan.convert()

    # =============================================================================
    # définition des fonctions
    # =============================================================================

    def ovni(x,y) :
        pg.draw.circle(screen , Vert , (x,y) , 10 , 0)

    def create_ovni() :
        global ovni_x
        global ovni_y
        ovni_x.append(randint(0,screenWidth))
        ovni_y.append(10)
        ovni( ovni_x[-1] , ovni_y[-1] )

    def explosion_ovni(x,y) :
        couleur = [227,207,87]
        taille = 2
        pg.draw.rect(screen , couleur , ( (x+randint(2,4)) , (y+randint(1,4))  , taille ,taille ) , 0)
        pg.draw.rect(screen , couleur , ( (x+randint(0,1)) , (y-randint(1,3))  , taille ,taille ) , 0)
        pg.draw.rect(screen , couleur , ( (x+randint(5,7)) , (y+randint(5,8))  , taille ,taille ) , 0)
        pg.draw.rect(screen , couleur , ( (x+randint(8,11)) , (y+randint(9,12))  , taille ,taille ) , 0)
        pg.draw.rect(screen , couleur , ( (x-randint(3,5)) , (y-randint(8,11))  , taille ,taille ) , 0)
        pg.draw.rect(screen , couleur , ( (x-randint(7,9)) , (y+randint(0,1))  , taille ,taille ) , 0)
        pg.draw.rect(screen , couleur , ( (x-randint(4,6)) , (y+randint(1,4))  , taille ,taille ) , 0)
        pg.draw.rect(screen , couleur , ( (x-randint(2,5)) , (y-randint(3,5))  , taille ,taille ) , 0)
        pg.draw.rect(screen , couleur , ( (x+randint(1,3)) , (y+randint(6,8))  , taille ,taille ) , 0)
        pg.draw.rect(screen , couleur , ( (x+randint(12,16)) , (y-randint(10,12))  , taille ,taille ) , 0)
        pg.draw.rect(screen , couleur , ( (x-randint(2,4)) , (y-randint(6,8))  , taille ,taille ) , 0)
        pg.draw.rect(screen , couleur , ( (x+randint(7,9)) , (y+randint(6,9))  , taille ,taille ) , 0)
        pg.draw.rect(screen , couleur , ( (x+randint(5,7)) , (y-randint(11,13))  , taille ,taille ) , 0)
        pg.draw.rect(screen , couleur , ( (x+randint(8,10)) , (y+randint(12,14))  , taille ,taille ) , 0)
        pg.draw.rect(screen , couleur , ( (x+randint(16,18)) , (y-randint(4,6))  , taille ,taille ) , 0)
        pg.draw.rect(screen , couleur , ( (x+randint(6,8)) , (y+randint(0,1))  , taille ,taille ) , 0)
        pg.draw.rect(screen , couleur , ( (x+randint(7,9)) , (y-randint(1,4))  , taille ,taille ) , 0)




    def missile(x,y) :
        pg.draw.rect(screen , Blanc , (x,y , 4 ,8 ) , 0)

    def create_missile() :
        global missile_x
        global missile_y
        missile_x.append(player_x+10)
        missile_y.append(player_y)

        missile( missile_x[-1] , missile_y[-1] )

    def player(x,y) :
        pg.draw.rect(screen , Blanc , (x,y , 25 , 10) , 0)


    nb_ovnis_tues
    def test_colision(num_ovni,num_missile) :
        if missile_x[num_missile] > ovni_x[num_ovni]-10 and missile_x[num_missile] < ovni_x[num_ovni]+10 :
            if missile_y[num_missile] > ovni_y[num_ovni]-10 and missile_y[num_missile] < ovni_y[num_ovni]+10 :
                return True
        return False


    def suprimer_ovni(i) :
        global ovni_x
        global ovni_y
        global a_exploser

        global nb_ovni
        global previous_nb

        nb_ovni -= 1
        previous_nb -= 1

        a_exploser.append((ovni_x[i],ovni_y[i]))
        ovni_x.pop(i)
        ovni_y.pop(i)


    def suprimer_missile(i) :
        global missile_x
        global missile_y

        missile_x.pop(i)
        missile_y.pop(i)


    def out_of_zone() :
        global score
        global nb_ovnis_arrives

        num_ovni = 0
        while num_ovni < (len(ovni_y)):
            if ovni_y[num_ovni] > screenHeight:
                suprimer_ovni(num_ovni)
                score -= 5
            num_ovni += 1

        num_missile = 0
        while num_missile < len(missile_y):
            if missile_y[num_missile] < 0 :
                suprimer_missile(num_missile)
                nb_ovnis_arrives += 1
            num_missile += 1


    def ovni_X_missile() : # un ovni croise un missile
        global score
        global nb_ovnis_tues

        if missile_x != [] and ovni_x != [] :
            num_ovni = 0
            while num_ovni < len(ovni_y) :
                num_missile = 0
                while num_missile < len(missile_x) and num_ovni<len(ovni_x) :
                    if test_colision(num_ovni, num_missile):
                        suprimer_ovni(num_ovni)
                        suprimer_missile(num_missile)
                        score += 1
                        nb_ovnis_tues += 1
                    num_missile += 1
                num_ovni += 1


    def scan_disparition():
        out_of_zone()

        ovni_X_missile()


    # =============================================================================
    # boucle pricipale :
    # =============================================================================


    while not_termine :
        event = pg.event.Event(pg.USEREVENT)    #
        for event in pg.event.get() :           # on vérifie si l'utilisateur demande à fermar la fenêtre
            if event.type == pg.QUIT :          #  en appuyant sur la croix
               not_termine = False              #

        if is_image :
            screen.blit(arriere_plan, (0,0))# met une image de l'espace (prise par le JWST) en arrière plan
        else :
            screen.fill(Noir)# met l'arrière plan en noir

        if score <= -10 :
            not_termine = False
        if score > max_score  :
            max_score = score
        if score > score_max_partie :
            score_max_partie = score

        KeysPressed = pg.key.get_pressed() # récupère la liste des touches appuyée


        if KeysPressed[pg.K_RIGHT] and player_x < screenWidth-20 :      #
            player_x += Speed["x_player"]                               # modifie la position du joueur
        if KeysPressed[pg.K_LEFT] and player_x > 0 :                    # en fonction de la flêche appuyée
            player_x -= Speed["x_player"]                               #

        if (KeysPressed[pg.K_UP] or KeysPressed[pg.K_SPACE]) and len(missile_x) <= nb_max_missiles :  # création de missiles si on appuie sur la flêche du haut
            create_missile()                                                                          # ou sur espace et si il y a moins de nb_max_missiles
            nb_missiles_tires += 1


        l = len(ovni_y)                         #
        for i in range(l) :                     #
            ovni_x[i] += Speed["x_ovni"]        #
            ovni_y[i] += Speed["y_ovni"]        #
                                                # modifie la position des missiles et des ovnis en fonction de leur vitesse
        L=len(missile_y)                        #
        for i in range(L) :                     #
            missile_x[i] -= Speed["x_missile"]  #
            missile_y[i] -= Speed["y_missile"]  #


        if previous_nb+1 == nb_ovni :
            create_ovni()
            previous_nb += 1


        for i in range(nb_ovni) :                   #
            ovni( ovni_x[i] , ovni_y[i] )           #
                                                    #
        for i in range(L) :                         # fait avancer les missiles, les ovnis et le joueur à chaque tour de boucle
            missile( missile_x[i] , missile_y[i] )  #
                                                    #
        player(player_x,player_y)                   #

        if nb_tours % ( freq_apparition_ovni ) == 0 :
            nb_ovni += 1

        scan_disparition()

        for i in range(len(a_exploser)) :
            explosion_ovni(a_exploser[i][0] , a_exploser[i][1])

        if nb_tours % duree_explosion == 0 :
            a_exploser = []

        if nb_tours % (20 * nb_fps) == 0 and freq_apparition_ovni > 18 :
            freq_apparition_ovni -= 2
            print(freq_apparition_ovni)
        if nb_tours % (25 * nb_fps) == 0 and nb_max_missiles > 10 :
            nb_max_missiles -= 2
            print(nb_max_missiles)
            print("")

        screen.blit(pg.font.SysFont("Arial", 25).render( str(score), True, Vert),(5,10))
        screen.blit(pg.font.SysFont("Arial", 25).render( str(nb_tours/nb_fps), True, Vert),(820,10))

        nb_tours += 1
        pg.display.flip() # affiche l'image dessinée à l'écran

        fps.tick(nb_fps)

    pg.quit()

    if nb_tours/nb_fps > max_temps : max_temps = nb_tours/nb_fps

    # =============================================================================
    # affichage des messages après défaite :
    # =============================================================================

    pg.init()
    fenetre_fin_Width = 600 #600
    fenetre_fin_Height = 400 #200
    fenetre_fin = pg.display.set_mode( ( fenetre_fin_Width , fenetre_fin_Height ) )
    pg.display.set_caption("Tueur D'Ovnis : messages")
    not_termine = True

    if is_image :
        fenetre_fin.blit(arriere_plan, (0,0))# met une image de l'espace (prise par le JWST) en arrière plan
    else :
        fenetre_fin.fill(Noir)# met l'arrière plan en noir


    succes_obtenus_liste = []

    if nb_ovnis_arrives > 10 :
        succes_obtenus_liste.append("l'indifférent")
    elif nb_ovnis_arrives >= 2 and nb_ovnis_arrives > 10 :
        succes_obtenus_liste.append("le soldat mitigé")
    elif nb_ovnis_arrives <= 1 :
        succes_obtenus_liste.append("le défenseur universel")

    if nb_ovnis_tues <= 10 :
        succes_obtenus_liste.append("l'ovni")
    elif nb_ovnis_tues > 10 and nb_ovnis_tues < 175 :
        succes_obtenus_liste.append("le bon soldat")
    elif nb_ovnis_tues >= 175 and nb_ovnis_tues <= 250 :
        succes_obtenus_liste.append("le tueur aguerri")
    elif nb_ovnis_tues > 250 :
        succes_obtenus_liste.append("le sauveur ultime")

    if nb_missiles_tires !=0 and nb_ovnis_tues != 0:
        ratio = nb_missiles_tires / nb_ovnis_tues
        if ratio > 17 :
            succes_obtenus_liste.append("le dépensier")
        elif ratio <= 17 and ratio > 4 :
            succes_obtenus_liste.append("le prudent")
        elif ratio <= 4 :
            succes_obtenus_liste.append("l'économe")
    else :
        succes_obtenus_liste = ["Joue au moins !"]


    # _m => message de fin de partie
    # _s => message de score
    # _a => messages pour les succés(achievment)
    police = pg.font.SysFont("Arial", 25)

    if score <= -10 :               #
        texte = "PERDU !"           # 1er message
    else : texte = "Fin De Partie !"#
    zone_m = police.render( texte, True, Rouge)
    fenetre_fin.blit(zone_m,(230,10))

    zone2_m = police.render( "Lv "+str(difficulte), True, [227,207,87])
    fenetre_fin.blit(zone2_m,(230,40))

    zone_temps = police.render( str(nb_tours/nb_fps) + " s de jeu", True, [0,201,87] )
    fenetre_fin.blit(zone_temps, (230,68))

    zone_temps_2 = police.render( "MAX : " + str(max_temps) + " s", True, [0,201,87] )
    fenetre_fin.blit(zone_temps_2, (230,95))

    resultat_score = "score : "+str(score) # 2e message
    zone2_s = police.render( resultat_score, True, Vert)
    fenetre_fin.blit(zone2_s,(230,125))

    score_max_affichage = "max partie : "+str(score_max_partie) # 4e message
    zone4_s = police.render( score_max_affichage, True, Vert)
    fenetre_fin.blit(zone4_s,(230,150))

    score_max_affichage = "MAX : "+str(max_score) # 3e message
    zone3_s = police.render( score_max_affichage, True, Vert)
    fenetre_fin.blit(zone3_s,(230,175))


    coord = (230,205)
    couleur = [72,209,204]
    if len(succes_obtenus_liste) == 1 :
        zone5_a = police.render( succes_obtenus_liste[0] , True, couleur)
        fenetre_fin.blit(zone5_a,coord)
    else :
        zone5_a = police.render( "Succès :" , True, couleur)
        fenetre_fin.blit(zone5_a,coord)
        coord = (230,coord[1]+25)
        for i in range(len(succes_obtenus_liste)) :
            zone5_a = police.render( succes_obtenus_liste[i], True, couleur)
            fenetre_fin.blit(zone5_a,coord)
            coord = (230,coord[1]+25)



    police_fin = pg.font.SysFont("Arial",16)
    auteur_et_merci = "Merci d'avoir joué à Tueur D'Ovnis V4.3    auteur : Adrien Lachaize"
    zone_fin = police_fin.render(auteur_et_merci, True, [0,127,255])
    fenetre_fin.blit(zone_fin, (80,fenetre_fin_Height-20))

    pg.display.flip()

    freq = pg.time.Clock()
    while not_termine :
        event = pg.event.Event(pg.USEREVENT)
        for event in pg.event.get() :
            if event.type == pg.QUIT :
               not_termine = False

        freq.tick(25)


    pg.quit()

    # =============================================================================
    # sauvegarde du score
    # =============================================================================

    tbl_types[str(difficulte)] = max_score
    temps[str(difficulte)] = max_temps
    stats = open("stats_du_tueur.json", "w")
    with open("stats_du_tueur.json", "w") as stats :
        dump([tbl_types,temps], stats, indent = 4, separators = (",", ":"))

except ModuleNotFoundError :
    print("les modules suivants sont requis pour l'exécution du programme : \n\t- random \n\t- json \n\t- os \n\t- pygame \n\t- math \n\t- sys \n\npour les installer, exécutez la commande pip install NomDuModule dans votre terminal ou la console python")
