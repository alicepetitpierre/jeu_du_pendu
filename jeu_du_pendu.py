#Script principal
#Ce script permet de jouer au jeu du pendu
#Un mot est sélectionné de facon aléatoire dans un fichier texte
#L'utilisateur a 6 chances pour trouver le mot
#Une fois les 6 chances passées l'utilisateur a perdu
#Après avoir gagné ou perdu, l'utilisateur peut rejouer

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
        #Solution obtenue sur https://stackoverflow.com/questions/44986793/remove-spaces-in-every-where-in-the-string-python
        reponse = input ('Veux-tu jouer avec ton propre fichier de mot ? '
                         '(oui/non) :').strip().lower()
        if reponse not in ["oui","non"]:
            print('Réponse invalide')
        else :
            correct = True

    #Lancer le jeu
    fichier = choisir_fichier (reponse)
    resultat = jouer_pendu (fichier)
    print (f'La réponse était {resultat}')

    #Demander si l'utilisateur veut faire une nouvelle partie
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
