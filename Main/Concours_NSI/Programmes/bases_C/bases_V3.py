def dec_to_base(nb : int , base : int) -> str:
    """
    dec_to_base(nb : int , base : int) -> str
    préconditions : - nb est un entier positif de la base 10
                    - base est un entier qui est votre base matfématiques de destination
    postconditions : renvoie une chaîne de caractère qui est votre  nombre dans la base demandée, le chiffre de poids fort est le plus à gauche
    """
    nb= int(nb)     # on s'assure que les nombres rentrés soit bien des entiers
    base = int(base)#
    list_index=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F",] #initialisation de la liste qui permet d'associer un chiffre de la base donnée au résultat du calcul
    result="" # initialisation de la valeur et du type de départ du résultat
    if base==0 or base==1 :             #
        print("demande impossible")     #
        return None                     #
    else :                              #
        if nb == 0:                     # tests des cas particuliers pour éviter des calculs non nécessaires
            return 0                    #
        elif nb == 10  and base >= 10 : #
            return 10                   #
        elif base==10:                  #
            return nb                   #
        else :
            while nb != 0 :
                result = str(list_index[nb % base]) + result # calcul permettant de déterminer la valeur des chiffres dans la base donnée
                nb = nb // base                              # en effectuant des divisions euclidiennes successives selon le modèle nb|_base
            return result                                    #                                                                        |


def base_to_dec(nb : str , base :int) -> int:
    """
    base_to_dec(nb : str , base :int) -> int
    préconditions : - nb est une chaîne de caractère représentant un nombre entier positif dans la base, tous les caractères doivent des nombres de votre base
                    - base est un entier qui est votre base mathématique de départ, 2<= base <= 16
    postconditions : renvoie un entier positif qui est votre nombre dans la base 10
    """
    base = int(base)  # on s'assure que le nombre en entrée est bien un entier
    list_index=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F",] #initialisation de la liste qui permet d'associer à un chiffre de la base donnée sa valeur en base 10
    result = 0
    if nb == 0 :                    #
        return 0                    #
    elif base==0 or base==1 :       #
        print("demande impossible") # tests des cas particuliers pour éviter des calculs non nécessaires
        return None                 #
    elif base==10:                  #
        return nb                   #
    else :
        for i in range(len(nb)) :
            result += int( list_index.index(nb[i]) * base**(len(nb) - i-1) ) # calcul attribuant une valeur en base 10 au chiffre de la donnée
        return result                                                        # selon la formule (valeur décimale du chiffre) * base^(position du chiffre en partant de droite)


def complement(binary : str) -> str:
    """
    complement(binary : str) -> str
    précondition : binary est une chaîne de caractères représentant votre nombre binaire avec le bit de poids fort à gauche
    postconditions : renvoie une chaîne de caractère correspondant au complément à 2 de binary
    """
    binary = str(binary) # on s'assure de bien avoir un string
    if binary == "0" :     #
        return "10"     # cas particuliers
    elif binary == "1" :   #
        return "1"      #
    l = len(binary) # permet de remonter la chaîne la chaîne de caractère par la droite dans une boucle for selon la formule l-i-1
    result = ""
    state = False # indique si un 1 a été croisé dans le nombre binary en partant de la droite
    for i in range(l):                                               #
        if state :                                                   #
            #result = str(int(not(bool(int( binary[l-i-1] ))))) + result # :les deux inversent le bit de position l-i-1
            result = str(1 - int(binary[l-i-1])) + result               #  :
        else :                                                       #
            if binary[l-i-1] == "1" :                                   # pour le complément à 2, à l'exeption de 0 et 1, on remonte le nombre binaire de la droite vers la gauche (le bit de poids fort à gauche)
                state = True                                         # jusqu'à trouver un 1, à partir de là tous les bits sont inversés à l'exeption du premier 1
            result = binary[l-i-1] + result                             # c'est le rôle de cette boucle for et de son contenu

    return result


def addition_bit_binaire (bit_1 : str , bit_2 : str , retenue="0") -> tuple :
    bit_1 , bit_2 , retenue = str(bit_1) , str(bit_2) , str(retenue)
    paquet = (bit_1,bit_2)
    if paquet == ("1","0") or paquet == ("0","1") :
        if retenue == "0" :
            return ("1","0") # le format de retour de la fonction est : ( le bit de résultat , retenue )
        return ("0","1")
    elif paquet == ("1","1") :
        if retenue == "0" :
            return ("0","1")
        return ("1","1")
    else :
        if retenue == "0" :
            return ("0","0")
        return ("1","0")


def addition_binaire(bin_1 : str , bin_2 : str) -> str:
    bin_1 , bin_2 = str(bin_1) , str(bin_2)
    l_1 , l_2 = len(bin_1) , len(bin_2)
    retenue = "0"
    result = ""
    if l_1 < l_2 :
        while l_1 != l_2 :
            bin_1 = "0" + bin_1
            l_1 += 1
    else :
        while l_2 != l_1 :
            bin_2 = "0" + bin_2
            l_2 += 1
    for i in range(l_1) :
        add = addition_bit_binaire(bin_1[l_1-i-1] , bin_2[l_1-i-1] , retenue)
        result = add[0] + result
        retenue = add[1]

    result = retenue + result
    return result


def soustraction_binaire(bin_1 : str , bin_2 : str) -> str :
    if len(bin_1)>=len(bin_2) :
        l=len(bin_1)
    else : l=len(bin_2)
    for _ in range(len(bin_1),l) :
        bin_1 = "0"+bin_1
    for _ in range(len(bin_2),l) :
        bin_2 = "0"+bin_2
    print(bin_1)
    print(bin_2)
    print(complement(bin_2))
    r = addition_binaire(bin_1,complement(bin_2))
    print(r)
    if len(r) > l :
        L = [e for e in r]
        while len(L) > l :
            L.pop(0)
        print(L)
        r = ""
        for e in L :
            r = r + e
    print("fin : ",r)
    return r


###############################################################################
inp = ""
while inp != "e" :
    inp=input("nombre de départ en decimal (d) ou dans une autre base(b) \ncomplément à 2 (c) \naddition binaire (a) \nexit(e) \n")

    if inp == "d" :
        rep = dec_to_base(int(input("nombre en base 10 \n")) ,int(input("base de destination \n")))
        print(rep)
        print(len(rep),"chiffres \n")

    elif inp == "b":
        rep = base_to_dec(input("nombre de départ \n") , int(input("base départ \n")))
        print(rep,"\n")

    elif inp == "c" :
        print(complement(input("votre nombre binaire \n ")), "\n")

    elif inp == "a" :
        print(addition_binaire( input("binaire 1 ?\n") , input("binaire 2 ?\n") ),"\n")

    elif inp == "e" : print("sortie de programme")

    else : print("demande erronée")
