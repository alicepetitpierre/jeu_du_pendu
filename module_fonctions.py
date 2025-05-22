#Module avec les fonctions pour le jeu du pendu

#Fonction qui retourne un fichier fonction du choix de l'utilisateur
def choisir_fichier (reponse) :
    #Si l'utilisateur veut utiliser son fichier
    if reponse == 'oui' :
        print ('Suivre instruction README')
        fichier = input ('Donner le nom du fichier, sous format nom.txt :')
    #Par defaut choix du fichier mots_pendu
    else :
        fichier ='mots_pendu.txt'
    return fichier

#Fonction qui selectionne un mot aléatoire dans un fichier txt
def selectionner_mot (fichier_txt):
    #importer bibliothèque
    import random
    #ouverture et lecture du fichier et selectionner un mot aléatoire
    with open(fichier_txt, "r", encoding='utf8') as f:
        #lire le contenu du fichier
        mots = f.readlines()
    #enlever retour à la ligne
    liste_mots = []
    for ligne in mots:
        mot = ligne.replace('\n', '').lower()
        liste_mots.append(mot)
    #selectionner un mot aléatoire dans la liste
    mot = random.choice(liste_mots)
    mot_normalise = enlever_caracteres_speciaux(mot)
    return mot_normalise

#Fonction qui enlève les caractères speciaux present dans un mot
def enlever_caracteres_speciaux(mot):
    #importation bibliothèque unicodedata
    import unicodedata
    mot_normalise = unicodedata.normalize('NFKD',mot)
    return ''.join([char for char in mot_normalise \
                    if not unicodedata.combining(char)])

#Fonction qui renvoie une indice, non testee et non presente dans mot
def trouver_indice (mot,lettre_testee) :
    #importer bibliothèques
    import string
    import random
    alphabet = string.ascii_lowercase
    #creer la liste des lettres qui ne peuvent pas etre un indice
    non_indice = list(mot) + lettre_testee
    indice = []
    #creer la liste des lettres qui peuvent etre un indice
    for lettre in alphabet :
        if lettre not in non_indice :
            indice.append(lettre)
    #selectionner une lettre dans la liste
    return random.choice(indice)

#Fonction pour jouer au pendu à partir d'un fichier de mots
def jouer_pendu (fichier) :
    #selectionner un mot et le cacher
    mot = selectionner_mot(fichier)
    mot_cache = '_' * len(mot)
    #afficher l'etat du mot cache
    print(f'Mot à deviner : {mot_cache}')
    #initialiser le nombre de chances
    chance = 6
    lettre_testee = []
    #boucler tant qu'il reste une chance
    while chance > 0 :
        lettre = input (f'Essayer la lettre (tu as {chance} chance(s)) :').lower()
        lettre = enlever_caracteres_speciaux(lettre)

        #Verifier que la lettre n'a pas deja été joué
        if lettre in lettre_testee :
            print ('Lettre deja testée')
            continue
        else :
            lettre_testee += [lettre]

        #initialisation
        trouve = False
        #tester si la lettre est dans le mot
        for i in range(len(mot)):
            if lettre == mot[i]:
                #modifier le mot caché
                mot_cache = mot_cache[:i] + lettre + mot_cache[i+1:]
                trouve = True

        #Sortir de la boucle si le mot est trouvé en entier
        if mot_cache == mot :
            break
        elif trouve:
            print(mot_cache)
        else :
            chance -= 1
            print(mot_cache)
            print ("-> La lettre n'est pas dans le mot")
            #Bonus donner un indice pour la dernière chance
            if chance == 1 :
                lettre_indice = trouver_indice(mot,lettre_testee)
                print (f"Indice : {lettre_indice} n'est pas dans le mot")

    if mot_cache == mot :
        print ('Gagné, tu as trouvé le mot !!')
    if chance == 0 :
        print ('Perdu, tu as epuisé tes chances...')
    return mot