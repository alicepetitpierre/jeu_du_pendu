
def choisir_fichier (reponse) :
    if reponse == 'oui' :
        print ('Suivre instruction README pour ajouter votre fichier')
        fichier = input ('Donner nom du fichier, sous format nom.txt :')
    else :
        fichier ='mots_pendu.txt'
    return fichier

def selectionner_mot (fichier_txt):
    import random
    with open(fichier_txt, "r") as fichier:
        liste_mots = [ligne.strip() for ligne in fichier.readlines()]
    return random.choice(liste_mots)

def enlever_caracteres_speciaux(mot):
    import unicodedata
    normalized_word = unicodedata.normalize('NFKD',mot)
    return ''.join([char for char in normalized_word if not unicodedata.combining(char)])

def jouer_pendu (mot) :
    mot_normalise = enlever_caracteres_speciaux(mot)
    mot_cache = '_'*len(mot)
    print(mot_cache)

    chance = 6
    lettre_teste = []

    while chance > 0 :
        lettre = input (f'Il te reste {chance} chance(s), essayer la lettre :').lower()
        lettre = enlever_caracteres_speciaux(lettre)

        #Verifier que la lettre n'a pas deja été joué
        if lettre in lettre_teste :
            print ('Lettre deja testée')
            continue
        else :
            lettre_teste += [lettre]


        trouve = False
        for i in range(len(mot_normalise)):
            if lettre == mot_normalise[i]:
                mot_cache = mot_cache[:i]+lettre+mot_cache[i+1:]
                trouve = True

        if mot_cache == mot_normalise :
            break
        elif trouve :
            print(mot_cache)
        else :
            chance -= 1
            print(mot_cache)
            print ("-> La lettre n'est pas dans le mot")

    if mot_cache == mot_normalise :
        print (f'Gagné tu as trouvé le mot : {mot_normalise}')
    if chance == 0 :
        print ('Perdu, tu as epuisé tes chances...')

    return mot_normalise