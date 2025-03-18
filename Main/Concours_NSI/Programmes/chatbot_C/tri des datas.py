import json

numdata = input("entrez un numéro de data \n")

with open("data/chatbot_data_" + numdata + ".json", "r") as data:
    dicorep = json.load(data)

liste  = list(dicorep)
element_liste=[]
reste_liste=[]
caractere = input("suite de caractère(s) à rechercher dans les éléments de votre data \n")


for i in range(len(liste)):
    if caractere in liste[i] :
        element_liste.append(liste[i])
    else:
        reste_liste.append(liste[i])

print("il y ",len(element_liste)," éléments contenants votre recherche : \n" , element_liste)
print(" ")
for i in range(len(element_liste)):
    print(element_liste[i])

# for _ in range(5):
#     print("|")
#
# print("voici la liste des éléments ne contenants pas votre recherche : \n" , reste_liste)
# print(" ")
# for i in range(len(reste_liste)):
#     print(reste_liste[i])
