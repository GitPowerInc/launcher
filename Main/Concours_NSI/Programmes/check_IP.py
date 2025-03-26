

def is_IP_valide(IP):
    if type(IP)==list and len(IP)==4:
        for e in IP:
            if not type(e)==int or not 0<=e<=255:
                return False
        return True
    return False

#les tests ont été faits par chatgpt

assert is_IP_valide([192, 168, 1, 1]) == True  # Adresse IP valide
assert is_IP_valide([255, 255, 255, 255]) == True  # Adresse de broadcast ( dans le doute je l'accepte )
assert is_IP_valide([0, 0, 0, 0]) == True  # Adresse de réseau ( dans le doute je l'accepre )
assert is_IP_valide([256, 168, 1, 1]) == False  # 256 dépasse la limite
assert is_IP_valide([-1, 168, 1, 1]) == False  # Valeur négative
assert is_IP_valide([192, "168", 1, 1]) == False  # Contient une chaîne de caractères
assert is_IP_valide([192, 168, 1]) == False  # Trop peu d'octets
assert is_IP_valide([192, 168, 1, 1, 5]) == False  # Trop d'octets
assert is_IP_valide([192, 168, 1, 300]) == False  # 300 dépasse la limite
assert is_IP_valide([192.5, 168, 1, 1]) == False  # Nombre flottant

print("Tous les tests sont passés avec succès.")



def to_bin(octet):
    if type(octet)!=int or octet<0 or octet>255:
        return False
    result= ""
    for i in range(8):
        if octet-2**(7-i)<0:
            result+= "0"
        else:
            result+= "1"
            octet-= 2**(7-i)
    return result

#les tests ont été faits par chatgpt

assert to_bin(0) == "00000000"  # Cas minimal
assert to_bin(1) == "00000001"  # Petit nombre
assert to_bin(2) == "00000010"  # Puissance de 2
assert to_bin(127) == "01111111"  # Valeur élevée mais valide
assert to_bin(128) == "10000000"  # Moitié de la plage
assert to_bin(255) == "11111111"  # Cas maximal

# Cas invalides : doivent lever une exception
assert to_bin(-1)== False  # Négatif
assert to_bin(256)== False  # Trop grand
assert to_bin(3.5)== False  # Nombre flottant
assert to_bin("100")== False  # Chaîne de caractères

print("Tous les tests sont passés avec succès.")

#Exercice III

def et_logique(octet1, octet2):
    if type(octet1)!=str or len(octet1)!=8 or type(octet2)!=str or len(octet2)!=8:
        return False
    ET=""
    for i in range(8):
        if octet1[i]=="1" and octet2[i]=="1":
            ET+="1"
        else:
            ET+="0"
    return ET

#les tests ont été faits par chatgpt

assert et_logique("00000000", "00000000") == "00000000"  # Cas minimal
assert et_logique("11111111", "11111111") == "11111111"  # Cas maximal
assert et_logique("10101010", "01010101") == "00000000"  # Bits opposés
assert et_logique("11110000", "00001111") == "00000000"  # Aucun bit commun
assert et_logique("11001100", "10101010") == "10001000"  # Mélange de 0 et 1
assert et_logique("00001111", "11110000") == "00000000"  # Inverses parfaits
assert et_logique("11110000", "11111111") == "11110000"  # Un octet tout à 1

print("Tous les tests sont passés avec succès.")



def to_dec(octet):
    if type(octet)!=str or len(octet)!=8:
        return False
    Dec=0
    for i in range(8):
        if octet[7-i]!="1" and octet[7-i]!="0":
            return False
        if octet[7-i]=="1":
            Dec+=2**i
    return Dec

#les tests ont été faits par chatgpt

assert to_dec("00000000") == 0  
assert to_dec("00000001") == 1  
assert to_dec("00000010") == 2  
assert to_dec("01111111") == 127  
assert to_dec("10000000") == 128  
assert to_dec("11111111") == 255  
assert to_dec("10101010") == 170  
assert to_dec("000000000") == False  
assert to_dec("0000000") == False  
assert to_dec("ABCDEFGH") == False  
assert to_dec("10201010") == False  
assert to_dec(10101010) == False 

print("Tous les tests sont passés avec succès.")



def adresse_reseau(IP, mask):
    if not is_IP_valide(IP) or not is_IP_valide(mask):
        return False
    Mask=[]
    for i in range(4):
        ip=to_bin(IP[i])
        m=to_bin(mask[i])
        Intern = et_logique(ip,m)
        Intern = to_dec(Intern)
        Mask+=[Intern]
    return Mask

#les tests ont été faits par chatgpt

assert adresse_reseau([192, 168, 1, 10], [255, 255, 255, 0]) == [192, 168, 1, 0]  
assert adresse_reseau([192, 168, 1, 10], [255, 255, 0, 0]) == [192, 168, 0, 0]  
assert adresse_reseau([192, 168, 1, 10], [255, 0, 0, 0]) == [192, 0, 0, 0]  
assert adresse_reseau([10, 0, 5, 200], [255, 255, 255, 0]) == [10, 0, 5, 0]  
assert adresse_reseau([172, 16, 45, 78], [255, 255, 0, 0]) == [172, 16, 0, 0]  
assert adresse_reseau([192, 168, 1, 255], [255, 255, 255, 128]) == [192, 168, 1, 128]  

# Cas invalides (doivent renvoyer False)
assert adresse_reseau([192, 168, 1], [255, 255, 255, 0]) == False  # IP trop courte  
assert adresse_reseau([192, 168, 1, 10, 5], [255, 255, 255, 0]) == False  # IP trop longue  
assert adresse_reseau([192, 168, 1, 10], [255, 255, 255]) == False  # Masque trop court  
assert adresse_reseau([192, 168, 1, 10], [255, 255, 255, 0, 128]) == False  # Masque trop long  
assert adresse_reseau([300, 168, 1, 10], [255, 255, 255, 0]) == False  # Valeur IP invalide  
assert adresse_reseau([192, 168, 1, 10], [300, 255, 255, 0]) == False  # Valeur masque invalide  
assert adresse_reseau([192, 168, "1", 10], [255, 255, 255, 0]) == False  # Type invalide dans IP  
assert adresse_reseau([192, 168, 1, 10], [255, "255", 255, 0]) == False  # Type invalide dans masque  

print("Tous les tests sont passés avec succès.")



def communication_IP(IP1, IP2, mask):
    First= adresse_reseau(IP1, mask)
    Second= adresse_reseau(IP2, mask) 
    if First!= False and Second!=False and First==Second:
        return True
    return False

#les tests ont été faits par chatgpt

assert communication_IP([192, 168, 1, 10], [192, 168, 1, 20], [255, 255, 255, 0]) == True  # Même sous-réseau  
assert communication_IP([192, 168, 1, 10], [192, 168, 2, 20], [255, 255, 255, 0]) == False  # Sous-réseaux différents  
assert communication_IP([10, 0, 0, 1], [10, 0, 0, 2], [255, 255, 255, 0]) == True  # Même sous-réseau  
assert communication_IP([172, 16, 1, 5], [172, 16, 2, 5], [255, 255, 0, 0]) == True  # Même sous-réseau  
assert communication_IP([172, 16, 1, 5], [172, 17, 2, 5], [255, 255, 0, 0]) == False  # Sous-réseaux différents  
assert communication_IP([192, 168, 1, 100], [192, 168, 1, 200], [255, 255, 255, 128]) == False    
assert communication_IP([192, 168, 1, 100], [192, 168, 1, 200], [255, 255, 255, 192]) == False  # Sous-réseaux différents  

# Cas invalides (doivent renvoyer False)
assert communication_IP([192, 168, 1], [192, 168, 1, 20], [255, 255, 255, 0]) == False  # IP1 trop courte  
assert communication_IP([192, 168, 1, 10, 5], [192, 168, 1, 20], [255, 255, 255, 0]) == False  # IP1 trop longue  
assert communication_IP([192, 168, 1, 10], [192, 168, 1], [255, 255, 255, 0]) == False  # IP2 trop courte  
assert communication_IP([192, 168, 1, 10], [192, 168, 1, 20, 5], [255, 255, 255, 0]) == False  # IP2 trop longue  
assert communication_IP([192, 168, 1, 10], [192, 168, 1, 20], [255, 255, 255]) == False  # Masque trop court  
assert communication_IP([192, 168, 1, 10], [192, 168, 1, 20], [255, 255, 255, 0, 128]) == False  # Masque trop long  
assert communication_IP([300, 168, 1, 10], [192, 168, 1, 20], [255, 255, 255, 0]) == False  # Valeur IP1 invalide  
assert communication_IP([192, 168, 1, 10], [300, 168, 1, 20], [255, 255, 255, 0]) == False  # Valeur IP2 invalide  
assert communication_IP([192, 168, 1, 10], [192, 168, 1, 20], [300, 255, 255, 0]) == False  # Valeur masque invalide  
assert communication_IP([192, 168, "1", 10], [192, 168, 1, 20], [255, 255, 255, 0]) == False  # Type invalide dans IP1  
assert communication_IP([192, 168, 1, 10], [192, 168, "1", 20], [255, 255, 255, 0]) == False  # Type invalide dans IP2  
assert communication_IP([192, 168, 1, 10], [192, 168, 1, 20], [255, "255", 255, 0]) == False  # Type invalide dans masque  


print("Tous les tests sont passés avec succès.")



ip_dict = {
    1: [192, 168, 1, 1],     # Routeur
    2: [192, 168, 1, 10],    # PC Bureau
    3: [192, 168, 1, 20],    # PC Portable
    4: [10, 0, 0, 1],        # Serveur
    5: [172, 16, 5, 100],    # Imprimante
} # merci chatgpt pour ce dico et POUR LES TEST

def recherche_ip(dic, IP):
    if not is_IP_valide(IP):
        return False
    for e in dic:
        if dic[e]==IP:
            return True
    return False

#les tests ont été faits par chatgpt

# IP présentes dans le dictionnaire
assert recherche_ip(ip_dict, [192, 168, 1, 1]) == True
assert recherche_ip(ip_dict, [192, 168, 1, 10]) == True
assert recherche_ip(ip_dict, [10, 0, 0, 1]) == True
assert recherche_ip(ip_dict, [172, 16, 5, 100]) == True

# IP absentes du dictionnaire
assert recherche_ip(ip_dict, [192, 168, 1, 50]) == False
assert recherche_ip(ip_dict, [10, 0, 0, 2]) == False
assert recherche_ip(ip_dict, [172, 16, 5, 101]) == False
assert recherche_ip(ip_dict, [8, 8, 8, 8]) == False  # Google DNS

# Cas invalides (doivent renvoyer False)
assert recherche_ip(ip_dict, [192, 168, 1]) == False  # IP trop courte
assert recherche_ip(ip_dict, [192, 168, 1, 10, 5]) == False  # IP trop longue
assert recherche_ip(ip_dict, [300, 168, 1, 10]) == False  # Valeur IP invalide
assert recherche_ip(ip_dict, ["192", 168, 1, 10]) == False  # Type invalide dans IP
assert recherche_ip(ip_dict, (192, 168, 1, 10)) == False  # Mauvais type (tuple au lieu de liste)
assert recherche_ip({}, [192, 168, 1, 10]) == False  # Dictionnaire vide


print("Tous les tests sont passés avec succès.")



ip_dict = {
    1: [192, 168, 1, 1],     # Routeur
    2: [192, 168, 1, 10],    # PC Bureau
    3: [192, 168, 1, 20],    # PC Portable
    4: [10, 0, 0, 1],        # Serveur
    5: [172, 16, 5, 100],    # Imprimante
} # merci chatgpt pour ce dico et POUR LES TEST

def ajouter_carnet(dic, ip):
    if not is_IP_valide(ip):
        return dic
    if not recherche_ip(dic, ip):
        position = len(dic)
        dic[position+1]=ip
    return dic

#les tests ont été faits par chatgpt

# Ajout d'une nouvelle adresse IP
ajouter_carnet(ip_dict, [192, 168, 1, 50])
assert ip_dict[6] == [192, 168, 1, 50]  # La nouvelle IP doit être ajoutée à la clé 6

# Ajout d'une autre adresse IP
ajouter_carnet(ip_dict, [8, 8, 8, 8])
assert ip_dict[7] == [8, 8, 8, 8]  # La nouvelle IP doit être ajoutée à la clé 7

# Ne pas ajouter une adresse déjà présente
ajouter_carnet(ip_dict, [192, 168, 1, 10])
assert len(ip_dict) == 7  # La taille ne doit pas avoir changé

# Cas invalides (ne doivent pas modifier le dictionnaire)
ajouter_carnet(ip_dict, [192, 168, 1])  # Trop court
ajouter_carnet(ip_dict, [192, 168, 1, 300])  # Valeur invalide
ajouter_carnet(ip_dict, ["192", 168, 1, 10])  # Type invalide

# Vérification que le dictionnaire n'a pas changé après les cas invalides

assert len(ip_dict) == 7

print("Tous les tests sont passés avec succès.")



# Dictionnaire d'adresses IP
ip_dict = {
    1: [192, 168, 1, 1],  
    2: [192, 168, 1, 10],  
    3: [192, 168, 1, 20],  
    4: [10, 0, 0, 1],  
    5: [172, 16, 5, 100],  
    6: [192, 168, 2, 30],  
    7: [192, 168, 1, 50],  
}  # merci chatgpt pour ce dico et POUR LES TEST

def extraire_sousReseau(dic, adresseReseau,mask):
    if not is_IP_valide(adresseReseau) or not is_IP_valide(mask) or type(dic)!=dict:
        return False
    if dic=={}:
        return []
    List=[]
    for e in dic:
        if communication_IP(dic[e], adresseReseau, mask):
            List+=[dic[e]]
    return List
        

#les tests ont été faits par chatgpt

assert extraire_sousReseau(ip_dict, [192, 168, 1, 0], [255, 255, 255, 0]) == [
    [192, 168, 1, 1],
    [192, 168, 1, 10],
    [192, 168, 1, 20],
    [192, 168, 1, 50],
]

# Sous-réseau 10.0.0.0/8 (255.0.0.0) → seul 10.0.0.1 doit être inclus
assert extraire_sousReseau(ip_dict, [10, 0, 0, 0], [255, 0, 0, 0]) == [[10, 0, 0, 1]]

# Sous-réseau 172.16.0.0/16 (255.255.0.0) → seul 172.16.5.100 doit être inclus
assert extraire_sousReseau(ip_dict, [172, 16, 0, 0], [255, 255, 0, 0]) == [[172, 16, 5, 100]]

# Sous-réseau 192.168.2.0/24 (255.255.255.0) → seul 192.168.2.30 doit être inclus
assert extraire_sousReseau(ip_dict, [192, 168, 2, 0], [255, 255, 255, 0]) == [[192, 168, 2, 30]]

# Aucun résultat attendu (sous-réseau inexistant dans le dico)
assert extraire_sousReseau(ip_dict, [192, 169, 1, 0], [255, 255, 255, 0]) == []

# Cas limites (IP invalides → doit renvoyer [])
assert extraire_sousReseau(ip_dict, [192, 168, 1], [255, 255, 255, 0]) == False  # Mauvais format
assert extraire_sousReseau(ip_dict, [300, 168, 1, 0], [255, 255, 255, 0]) == False  # Valeur invalide
assert extraire_sousReseau({}, [192, 168, 1, 0], [255, 255, 255, 0]) == []  # Dico vide


print("Tous les tests sont passés avec succès.")



# Dictionnaire initial
ip_dict = {
    1: [192, 168, 1, 1],  
    2: [192, 168, 1, 10],  
    3: [192, 168, 1, 20],  
    4: [10, 0, 0, 1],  
    5: [172, 16, 5, 100],  
    6: [192, 168, 2, 30],  
    7: [192, 168, 1, 50],  
}  # merci chatgpt pour ce dico et POUR LES TEST

def supprimer_carnet(dic, ip):
    if not is_IP_valide(ip) or type(dic)!=dict:
        return False
    if dic=={}:
        return {}
    cond=False
    longueur=len(dic)
    a=0
    dic2={}
    for i in range(longueur-a):
        if dic[i+1]==ip:
            a=1
        else:
            dic2[i+1-a]=dic[i+1]
    return dic2


    
#les tests ont été faits par chatgpt

# Suppression d'une adresse existante
ip_dict=supprimer_carnet(ip_dict, [192, 168, 1, 10])
assert len(ip_dict) == 6  # Une entrée en moins
assert ip_dict == {
    1: [192, 168, 1, 1],
    2: [192, 168, 1, 20],  # La clé 3 devient 2
    3: [10, 0, 0, 1],  # La clé 4 devient 3
    4: [172, 16, 5, 100],  # La clé 5 devient 4
    5: [192, 168, 2, 30],  # La clé 6 devient 5
    6: [192, 168, 1, 50],  # La clé 7 devient 6
}

# Suppression d'une autre adresse
ip_dict=supprimer_carnet(ip_dict, [10, 0, 0, 1])
assert len(ip_dict) == 5  # Encore une entrée en moins
assert ip_dict == {
    1: [192, 168, 1, 1],
    2: [192, 168, 1, 20],
    3: [172, 16, 5, 100],  # La clé 4 devient 3
    4: [192, 168, 2, 30],  # La clé 5 devient 4
    5: [192, 168, 1, 50],  # La clé 6 devient 5
}

# Suppression d'une adresse inexistante (ne change rien)
ip_dict=supprimer_carnet(ip_dict, [8, 8, 8, 8])
assert len(ip_dict) == 5  # Pas de modification

# Vérification que le dictionnaire est inchangé après les cas invalides
assert len(ip_dict) == 5

print("Tous les tests sont passés avec succès.")

#en vrai non mais je crois qu'on a les olympiades demain