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


def lire_fichier(nom_fichier):
    """
    Lit le contenu d'un fichier texte.
    Paramètre:
        nom_fichier (str): Le chemin du fichier à lire.
    Retour:
        str: Le contenu du fichier ou None si le fichier est introuvable.
    """
    try:
        # Ouvre le fichier en mode lecture ('r') avec l'encodage UTF-8
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            # Lit le contenu du fichier et le retourne
            return fichier.read()
    except FileNotFoundError:
        # Si le fichier n'est pas trouvé, affiche un message d'erreur et retourne None
        print(f"Erreur : fichier '{nom_fichier}' non trouvé.")
        return None


def ecrire_fichier(nom_fichier, texte):
    """
    Écrit un texte dans un fichier.
    Paramètres:
        nom_fichier (str): Le chemin du fichier à écrire.
        texte (str): Le texte à écrire.
    """
    # Ouvre le fichier en mode écriture ('w') avec l'encodage UTF-8
    with open(nom_fichier, 'w', encoding='utf-8') as fichier:
        # Écrit le texte dans le fichier
        fichier.write(texte)


txt = tuple(input("Quel mot souhaitez-vous crypter ?"))
cle_cryptage = int(input("Quel est la clé de cryptage ?"))
print(encryptage(txt, cle_cryptage))

txt = tuple(input("Quel mot souhaitez-vous décrypter ?"))
cle_cryptage = int(input("Quel est la clé de cryptage ?"))
print(decryptage(txt, cle_cryptage))

nom = input("Entrez le chemin du fichier à lire (nom du fichier compris) : ")
txt = lire_fichier(nom)
print(txt)

fichier_sortie = input("Entrez le nom du fichier de sortie: ")
ecrire_fichier(fichier_sortie, txt)
