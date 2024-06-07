"""
Programme de chiffrement et de déchiffrement utilisant le code de César en Python.
Ce programme permet de chiffrer et déchiffrer des textes ou des fichiers texte en utilisant une clé spécifiée.
Il peut également tenter de déchiffrer des textes sans clé en utilisant une analyse fréquentielle des caractères ou
par essai-erreur en vérifiant le pourcentage de mots appartenant aux mots français les plus fréquents.

Auteurs : Lou-Anne Villette, Thomas Chambeyron
Date : 22/05/2024
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


def decryptage(texte, cle):
    """
    Déchiffre un texte en utilisant une clé spécifiée.
    Paramètres:
        texte (str): Le texte à déchiffrer.
        cle (int): La clé de déchiffrement.
    Retour:
        str: Le texte déchiffré.
    """

    # Sinon, déchiffrer le texte avec la clé spécifiée
    return chiffrement_cesar(texte, -cle)


txt = tuple(input("Quel mot souhaitez-vous crypter ?"))
cle_cryptage = int(input("Quel est la clé de cryptage ?"))
print(encryptage(txt, cle_cryptage))

txt = tuple(input("Quel mot souhaitez-vous décrypter ?"))
cle_cryptage = int(input("Quel est la clé de cryptage ?"))
print(decryptage(txt, cle_cryptage))
