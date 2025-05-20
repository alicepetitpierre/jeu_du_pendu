import random

#Definir fonction lire fichier et renvoyer liste des lignes du fichier
def selectionner_mot (fichier_txt):
    #ouvrir le fichier en mode lecture
    fichier = open(fichier_txt, "r")
    #creer une liste des lignes du fichier
    liste_mots = fichier.readlines()
    print(liste_mots)
    #nettoyer la liste
    for i in range(len(liste_mots)):
        liste_mots[i]=liste_mots[i].strip()
    print(liste_mots)
    #sortir un mot de facon aléatoire
    return random.choice(liste_mots)

def tester_lettre (lettre,mot):
    for i in range (len(mot)):
        if mot[i]==lettre:
            return

mot = selectionner_mot ("mots_pendu.txt")
print(mot)
