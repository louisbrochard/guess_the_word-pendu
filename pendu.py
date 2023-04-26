#! usr/local/bin/python3
# -*-coding:Utf-8 -*

# Exercice Pratique du pendu. Réalisé par Louis Brochard le 1er Août 2020
# Dans le cadre du MOOC : "Apprenez à programmer en Python" du site OpenClassroom

import time
from donnees import*
from fonctions import*

print("Bienvenue dans le jeu du Pendu")
print("Ce jeu a été créé par Louis Brochard, le 1er août 2020.")
print("\n")
time.sleep(3)

regles = input("Si vous voulez un rappel des règles tapez 'r', si vous ne voulez pas, appuyez sur entrée : ")
regles = str(regles)
regles = regles.lower()

if regles == 'r' :
	print("Petit rappel des règles...")
	time.sleep(2)
	print("\n")
	print("Votre objectif est de découvrir le mot mystère, qui se composera toujours de 8 lettres, le plus rapidement possible.")
	time.sleep(2)
	print("\n")
	print("Pour cela, vous devrez me proposer des lettres, je vous dirais alors si elles composent le mot mystère ou bien si c'est un échec")
	time.sleep(2)
	print("Si vous arrivez à 8 échecs, alors malheureusement pour vous, le jeu sera perdu")
	print("\n")
	time.sleep(3)
	print("A chaque tentative de lettre, vous aurez aussi le droit de faire une tentative pour trouver le mot")
	time.sleep(2)
	print("Si vous trouvez le mot mystère avant d'avoir 8 échecs aux lettres, le jeu est gagné.")
	print("Alors, le score que vous obtiendrez sera de 8 - nb échecs.")
	time.sleep(3)
	print("\n")
	print("Par exemple, 3 fois j'ai proposé des lettres qui ne se trouvaient pas dans le mot mais j'ai tout de même fini par trouver le mot. Mon score est alors de 8 - 3 = 5")
	print("Les meilleurs scores, sont enregistrés dans le jeu, c'est pourquoi on vous demandera votre nom avant de commencer la partie.")
	print("\n")
	print('Vous êtes prêts ? Nous allons commencer...')
	print("\n")
	time.sleep(3)
	regles = ''

continuer_partie = True
scores = recup_scores()
ID = recup_id()
print("\n")

if ID not in scores.keys():
    scores[ID] = 0 # 0 point pour commencer

while continuer_partie == True :
	
	mot = choisir_mot()
	mot_list = list(mot)
	print("Le mot que vous devez deviner se présente ainsi : '_ _ _ _ _ _ _ _' ")
	print("\n")


	fail = 0
	lapartiecontinue = True
	target = "_ _ _ _ _ _ _ _"

	target_list = target.split()
	while fail != 8 and lapartiecontinue == True : 

		
		lettre = recup_lettre()
		print("\n")


		if lettre in mot_list : 

			i = 0
			while i != 8 : 
				if lettre == mot[i] : 
					del target_list[i]
					str_inser = str(mot[i])
					target_list.insert(i, str_inser)
					print("Félicitations la lettre ", lettre, " apparaît dans le mot à la ", i, "ième position.")
					print("Voici le mot qui apparaît petit à petit : ", " ".join(target_list)) 
					print("\n")

					i += 1
				else :
					i += 1
                                       

		else : 
			print("Désolé, malheureusement la lettre : ", lettre, "n'apparaît pas dans le mot recherché")
			fail += 1 
			if fail == 8 : 
				print("Vous avez atteint votre quotas d'erreurs, malheureusement le jeu est perdu pour vous, mais vous pouvez recommencer...")
				print("\n")
				print("Le mot mystère était : ", mot)
				continuer_partie = False
			else : 
				print("Vous avez commis ", fail, "erreurs. A 8 erreurs, le jeu sera perdu")
				print("\n")

		if fail != 8 :		
			tentative = input("Vous pouvez effectuer une tentative pour tenter de deviner le mot : ")
			tentative = tentative.lower()

			if tentative == mot : 
				trofor = 8 - fail 
				print("Félicitations, vous avez trouvé le bon mot, votre score à cette partie est de : ", trofor, " points")
				scores[ID] = trofor
				enregistrer_scores(scores)
				lapartiecontinue = False
				break
			else :
				print("Désolé, ce n'est pas le bon mot, continuez de chercher")
				print("\n")

				lapartiecontinue = True 
	break



mscores = input("Maintenant que la partie est finie, voulez vous afficher les meilleurs scores ? Tapez [o] pour les afficher")

mscores = str(mscores)
mscores = mscores.lower()
if mscores == 'o' :
	afficher_mscores()
	mscores = ''


	









