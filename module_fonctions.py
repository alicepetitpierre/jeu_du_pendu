#Fonction qui retourne un fichier fonction du choix de l'utilisateur
def choisir_fichier (reponse) :
    if reponse == 'oui' :
        print ('Suivre instruction README pour ajouter votre fichier')
        fichier = input ('Donner nom du fichier, sous format nom.txt :')
    else :
        fichier ='mots_pendu.txt'
    return fichier

#Fonction qui selectionne un mot aléatoire dans un fichier txt
def selectionner_mot (fichier_txt):
    import random
    with open(fichier_txt, "r") as fichier:
        liste_mots = [ligne.strip().lower() for ligne in fichier.readlines()]
        mot = random.choice(liste_mots)
        mot_normalise = enlever_caracteres_speciaux(mot)
    return mot_normalise

#Fonction qui enlève les caractères speciaux present dans un mot
def enlever_caracteres_speciaux(mot):
    import unicodedata
    normalized_word = unicodedata.normalize('NFKD',mot)
    return ''.join([char for char in normalized_word \
                    if not unicodedata.combining(char)])

#Fonction qui renvoie une lettre indice, non presente dans mot
def trouver_indice (mot) :
    import string
    import random
    alphabet = string.ascii_lowercase
    indice = [lettre for lettre in alphabet if lettre not in mot]
    return random.choice(indice)

#Fonction pour jouer au pendu à partir d'un fichier de mots
def jouer_pendu (fichier) :

    mot = selectionner_mot(fichier)

    mot_cache = '_' * len(mot)
    print(f'Mot à deviner : {mot_cache}')

    chance = 6
    lettre_teste = []

    while chance > 0 :
        lettre = input (f'Essayer la lettre (tu as {chance} chance(s)) :').lower()
        lettre = enlever_caracteres_speciaux(lettre)

        #Verifier que la lettre n'a pas deja été joué
        if lettre in lettre_teste :
            print ('Lettre deja testée')
            continue
        else :
            lettre_teste += [lettre]

        #Ajouter la lettre lorsqu'elle est dans le mot
        trouve = False
        for i in range(len(mot)):
            if lettre == mot[i]:
                mot_cache = mot_cache[:i]+lettre+mot_cache[i+1:]
                trouve = True

        #Sortie de la boucle si le mot est trouvé en entier avant la fin des 6 chances
        if mot_cache == mot :
            break
        elif trouve :
            print(mot_cache)
        else :
            chance -= 1
            print(mot_cache)
            print ("-> La lettre n'est pas dans le mot")
            #Bonus donner un indice pour la dernière chance
            if chance == 1 :
                lettre_indice = trouver_indice(mot)
                print (f"Indice : {lettre_indice} n'est pas dans le mot")

    if mot_cache == mot :
        print ('Gagné, tu as trouvé le mot !!')
    if chance == 0 :
        print ('Perdu, tu as epuisé tes chances...')

    return mot