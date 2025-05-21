
from fonctions import selectionner_mot, choisir_fichier, jouer_pendu

reponse = input ('Voulez vous jouer avec votre propre ficher de mot (oui/non) :')
fichier = choisir_fichier (reponse)
mot = selectionner_mot (fichier)
resultat = jouer_pendu (mot)