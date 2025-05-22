#Script principal du jeu du pendu
#Un mot est selectionné de facon aléatoire dans un fichier texte
#L'utilisateur à 6 chances pour trouver toutes les lettres
#Apres avoir gangé ou perdu, l'utilisateur peut rejouter

print('- JEU DU PENDU -')
print()
from module_fonctions import choisir_fichier, jouer_pendu
#Initialiser la condition
jouer = True
#Boucle tant que l'utilisateur veut jouer
while jouer :
    #Initialisater la condition
    correct = False
    reponse = ""
    #Boucler tant que la réponse n'est pas dans le bon format
    while not correct :
        #Demander si l'utilisateur veut jouer avec son fichier ou non
        reponse = input ('Veux-tu jouer avec ton propre fichier de mot ? '
                         '(oui/non) :').strip().lower()
        if reponse not in ["oui","non"]:
            print('Réponse invalide')
        else :
            correct = True

    #Lancer le jeu
    fichier = choisir_fichier (reponse)
    resultat = jouer_pendu (fichier)
    print (f'La réponse etait {resultat}')

    #Demander si l'utilisateur veux faire une nouvelle partie
    correct = False
    nouvelle_partie = ""
    # Boucler tant que la réponse n'est pas dans le bon format
    while not correct:
        # Demander si l'utilisateur veut jouer avec son fichier ou non
        nouvelle_partie = input('Veux-tu jouer de nouveau ? (oui/non) :').strip().lower()
        if nouvelle_partie not in ["oui", "non"]:
            print('Réponse invalide')
        else:
            correct = True

    if nouvelle_partie == 'oui':
        continue
    else :
        jouer = False
