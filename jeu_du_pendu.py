import random
#Ouvrir le ficher en mode lecture
fichier=open("mots_pendu.txt","r")

#Créer un liste des mots du ficher
liste_mots = fichier.readlines()
print(liste_mots)

#Nettoyer la liste
for i in range(len(liste_mots)):
    liste_mots[i]=liste_mots[i].strip()
print(liste_mots)

#mot=random.random(liste_mots)

#etat_du_mot=x.replace('a','_')
#print(etat_du_mot)