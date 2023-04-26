#! usr/local/bin/python3
# -*-coding:Utf-8 -*


# Exercice Pratique du pendu. Réalisé par Louis Brochard le 1er Août 2020
# Dans le cadre du MOOC : "Apprenez à programmer en Python" du site OpenClassroom

import pickle
from random import choice 
from donnees import*
import os


def recup_scores():
    """Cette fonction récupère les scores enregistrés si le fichier existe.
    Dans tous les cas, on renvoie un dictionnaire, 
    soit l'objet dépicklé,
    soit un dictionnaire vide.

    On s'appuie sur nom_fichier_scores défini dans donnees.py"""
    
    if os.path.exists("scores.txt"): # Le fichier existe
        # On le récupère
        fichier_scores = open("scores.txt", "rb")
        mon_depickler = pickle.Unpickler(fichier_scores)
        scores = mon_depickler.load()
        fichier_scores.close()
    else: # Le fichier n'existe pas
        scores = {}
    return scores


def recup_id() :
	"""Cette fonction permet de récup un nom d'utilisateur pour le mec qui va jouer"""

	ID = input ("Entrez votre nom : ")
	ID = ID.capitalize()
	if not ID.isalnum() : 
		print("Le nom inséré n'est pas correct ou pas assez long")
		return recup_id
	else : 
		return ID



def choisir_mot () :
	"""Cette Fonction permet de sélectionner un mot depuis la liste 
	qui est dans le fichier des données"""

	return choice(liste_des_mots)


def recup_lettre() :
	"""Cette fonction permet de récupérer la lettre insérée par l'utilisateur"""

	lettre = input("Insérez la lettre de votre choix : ")
	lettre = lettre.lower()
	if len(lettre) > 1 or not lettre.isalpha() : 
		print("Le contenu saisi n'est pas correct ou pas autorisé.")
		return recup_lettre
	else : 
		return lettre 


def enregistrer_scores(scores) :
    """Cette fonction se charge d'enregistrer les scores dans le fichier
    nom_fichier_scores. Elle reçoit en paramètre le dictionnaire des scores
    à enregistrer"""

    fichier_scores = open("score.txt", "wb") # On écrase les anciens scores
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()


def afficher_mscores() : 
    """Cette fonction se charge d'afficher les meilleurs scores"""
    fs = open("score.txt", "rb")
    mon_pickler = pickle.Unpickler(fs)
    scores = mon_pickler.load()
    print(scores)
    fs.close()






