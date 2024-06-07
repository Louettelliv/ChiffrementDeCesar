"""
Programme de chiffrement et de déchiffrement utilisant le code de César en Python.
Ce programme permet de chiffrer et déchiffrer des textes ou des fichiers texte en utilisant une clé spécifiée.
Il peut également tenter de déchiffrer des textes sans clé en utilisant une analyse fréquentielle des caractères ou
par essai-erreur en vérifiant le pourcentage de mots appartenant aux mots français les plus fréquents.

Auteurs : Lou-Anne Villette, Thomas Chambeyron
Date : 25/05/2024
"""


import string


def chiffrement_cesar(texte, cle):
    """
    Chiffre un texte en utilisant le chiffre de César avec une clé donnée.
    Paramètres:
        texte (str): Le texte à chiffrer.
        cle (int): La clé de chiffrement.
    Retour:
        str: Le texte chiffré.
    """
    # Initialisation d'une liste pour stocker les caractères chiffrés
    resultat = []

    # Définition de l'alphabet en majuscules et en minuscules
    alphabet_maj = string.ascii_uppercase
    alphabet_min = string.ascii_lowercase

    # Parcours de chaque caractère dans le texte
    for char in texte:
        if char.isupper():
            # Chiffrement des lettres majuscules en appliquant le décalage avec la clé
            resultat.append(alphabet_maj[(alphabet_maj.find(char) + cle) % 26])
        elif char.islower():
            # Chiffrement des lettres minuscules en appliquant le décalage avec la clé
            resultat.append(alphabet_min[(alphabet_min.find(char) + cle) % 26])
        else:
            # Conservation des caractères qui ne sont pas des lettres (ponctuations, espaces, etc.)
            resultat.append(char)

    # Concaténation des caractères chiffrés pour former le texte chiffré final
    return ''.join(resultat)


def encryptage(texte, cle):
    """
    Chiffre un texte en utilisant la fonction chiffrement_cesar.
    Paramètres:
        texte (str): Le texte à chiffrer.
        cle (int): La clé de chiffrement.
    Retour:
        str: Le texte chiffré.
    """

    # Appel de la fonction chiffrement_cesar avec le texte et la clé spécifiée
    return chiffrement_cesar(texte, cle)


def analyse_frequentielle(texte_chiffre):
    """
    Analyse la fréquence des lettres dans un texte chiffré pour deviner la clé de chiffrement. La lettre e étant la plus
    fréquente dans la langue française, on suppose donc que la lettre la plus fréquente dans le texte correspond à "e".
    Paramètres:
        texte_chiffre (str): Le texte chiffré.
    Retours:
        int: La clé estimée.
    """
    # Définition de l'alphabet
    alphabet = string.ascii_lowercase
    # Initialisation d'une liste pour compter l'occurrence de chaque lettre de l'alphabet
    occurrence = [0]*26

    # Parcours du texte chiffré
    for char in texte_chiffre:
        # Vérification si le caractère est une lettre minuscule
        if char.islower():
            # Incrémentation du compteur pour la lettre correspondante dans l'alphabet
            occurrence[alphabet.find(char.lower())] += 1

    # Recherche de la lettre la plus fréquente dans le texte chiffré
    max_occurrence = occurrence[0]
    index_max = 0
    for i in range(len(occurrence)):
        if max_occurrence < occurrence[i]:
            max_occurrence = occurrence[i]
            index_max = i

    # Calcul de la clé estimée en comparant la lettre la plus fréquente avec 'e'
    cle = (index_max - alphabet.find('e')) % 26

    return cle


# Fonction pour vérifier si un mot est français
def est_francais(texte, mots_francais):
    """
    Vérifie si un texte est en français en comparant les mots avec une liste de mots français.
    Paramètres:
        texte (str): Le texte à vérifier.
        mots_francais (set): L'ensemble des mots français.
    Retour:
        bool: True si le texte est en français, False sinon.
    """
    # Séparation du texte en mots en minuscules
    mots = texte.lower().split()
    # Initialisation du compteur de correspondance
    correspondance = 0

    # Parcours de chaque mot dans le texte
    for mot in mots:
        # Suppression des caractères de ponctuation et vérification de l'appartenance du mot à la liste de mots français
        if mot.strip(string.punctuation) in mots_francais:
            # Incrémentation du compteur si le mot est trouvé dans la liste de mots français
            correspondance += 1

    # Calcul du pourcentage de mots français dans le texte
    # Renvoie True s'il y a plus de 30% des mots correspondant aux mots français les plus fréquents
    return correspondance/len(mots) > 0.3


def brute_force(texte_chiffre, mots_francais):
    """
    Tente de déchiffrer un texte sans clé en utilisant l'analyse fréquentielle et la force brute.
    Paramètres:
        texte_chiffre (str): Le texte chiffré.
        mots_francais (set): L'ensemble des mots français.
    Retour:
        str: Le texte déchiffré ou None si le déchiffrement échoue.
    """
    # Déchiffrement du texte avec la clé obtenue à partir de l'analyse fréquentielle
    texte_dechiffre = chiffrement_cesar(texte_chiffre, analyse_frequentielle(texte_chiffre))
    # Vérification si le texte déchiffré est en français
    if est_francais(texte_dechiffre, mots_francais):
        return texte_dechiffre
    else:
        # Si le texte déchiffré n'est pas en français, essayer toutes les clés possibles avec la force brute
        for cle in range(1, 26):
            texte_dechiffre = chiffrement_cesar(texte_chiffre, -cle)
            # Vérification si le texte déchiffré avec la clé actuelle est en français
            if est_francais(texte_dechiffre, mots_francais):
                return texte_dechiffre
    # Si aucun texte déchiffré n'est en français, afficher un message d'échec
    print("Echec du décryptage sans la clé")
    return None


def decryptage(texte, cle, mots_francais):
    """
    Déchiffre un texte en utilisant une clé spécifiée ou en utilisant brute_force si la clé est inconnue.
    Paramètres:
        texte (str): Le texte à déchiffrer.
        cle (int): La clé de déchiffrement (0 si inconnue).
        mots_francais (set): L'ensemble des mots français.
    Retour:
        str: Le texte déchiffré.
    """
    # Si la clé est inconnue (0), utiliser la méthode de la force brute pour déchiffrer le texte
    if cle == 0:
        return brute_force(texte, mots_francais)

    # Sinon, déchiffrer le texte avec la clé spécifiée
    return chiffrement_cesar(texte, -cle)