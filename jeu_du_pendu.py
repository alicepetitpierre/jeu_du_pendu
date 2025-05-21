#-----------------------------------------------
#Nom du fichier : jeu_du_pendu.py
#Description    : Jeu du pendu
#Auteur         : Alice Petitpierre
#Python Version : 3.13
#-----------------------------------------------

print ('- JEU DU PENDU -')

from module_fonctions import choisir_fichier, jouer_pendu

print ()

while True :
    #Demander si l'utilisateur veux jouer avec son fichier ou non
    reponse = ""
    while reponse not in ["oui","non"]:
        reponse = input ('Veux-tu jouer avec ton propre fichier de mot ? (oui/non) :').strip().lower()
        if reponse not in ["oui","non"]:
            print('Réponse invalide')

    #Lancer le jeu
    fichier = choisir_fichier (reponse)
    resultat = jouer_pendu (fichier)
    print (f'La réponse etait {resultat}')

    #Demander si l'utilisateur veux faire une nouvelle partie
    nouvelle_partie = input ('Veux-tu jouer de nouveau ? (oui/non) :')
    if nouvelle_partie == 'oui':
        continue
    else :
        break
