from random import randint
from random import shuffle
from tkinter import *

"""
-------------Projet 2 INFO-H-100----------------
--------Alexis Rouvroy et Léo Moulin------------

Apports personnels:
	- Mode multijoueur
	- Affichage amélioré grâce à l'art ascii
	- Navires de tailles variables ( Modifier le nombre ou la taille 
	des navires dans le fichier navires.dat )

Pour le placement des navires, on commence par choisir la case d'origine du navire
puis on décide de le faire partir par la droite ou le haut.

Pour la lecture du tableau,
R = Raté
T = Touché
"""

#----------------------------------------entrees joueur        

def transforme_joueur_ordi(tir):                #J5 => [9, 4]
	"""
	Transforme une entrée du joueur en une liste de 2 nombres plus facile à manipuler.
	
	Arguments:
		tir(str): coordonnées rentrées par le joueur							
	Valeurs de retour:
		case(list): liste de 2 nombres 
	Exemple:
		print(transforme_joueur_ordi(J5))
		>>>[9,4]
	"""				
	dico = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9}
	case = [dico[str.lower(tir[0])]]
	y=""
	for i in range(len(tir)-1):
		y = y+tir[i+1]
	case.append(int(y)-1)
	return case
	
def transforme_ordi_joueur(case):                                        #[9, 4] => J5
	"""
	Transforme une liste de 2 nombres par une case sur la grille.
	
	Arguments:
		case(list): liste de 2 nombres
		
	Valeurs de retour:
		tir(str): coordonnées entrées par le joueur
		
	Exemple:
		print(transforme_ordi_joueur([9,4]))
		>>>J5
	"""	
	dico = ["A","B","C","D","E","F","G","H","I","J"]
	return dico[case[0]] + str(case[1]+1)
	
def verif_si_entree_possible(entree, tableau):
	"""
	Vérifie si le tir entré par le joueur est valide.
	
	Arguments:
		entree(list): 
		tableau(list): 
		 
	Valeurs de retour:
		result(bool): True si le tir est valide, False si non
	"""	
	dico = ["A","B","C","D","E","F","G","H","I","J"]
	nombre = ""
	result = True
	
	if not(str.upper(entree[0]) in dico):
		result = False
		
	for i in range(len(entree)-1):
		nombre = nombre + entree[i+1]
		if not(entree[i+1].isnumeric()):
			result = False
			
	if result != False and (int(nombre)>len(tableau) or int(nombre)<1):
		result = False
		
	if not(result):
		print("Votre tir n'est pas correct, veuillez recommencer")
		
	return result
	
#----------------------------------------lit fichier navires.dat        
def lit_fichier():                    #['porte-avions 1 5\n', 'cuirasse 1 4\n', 'sous-marin 1 3\n', 'destroyer 1 2 \n']
	"""	
	Lit le fichier "navires.dat" et le convertit en une liste du type 
	['porte-avions 1 5\n', 'cuirasse 1 4\n', 'sous-marin 1 3\n', 'destroyer 1 2 \n']
	
	Arguments:
		Aucun
		
	Valeurs de retour:
		contenu(list): liste contenant le nom, le nombre et la taille des différents navires
	"""
	fichier = open("navires.dat", "r")
	contenu = fichier.readlines()
	fichier.close()
	return contenu
	
def liste_fichier():                  #[['porte-avions', 1, 5], ['cuirasse', 1, 4], ['sous-marin', 1, 3], ['destroyer', 1, 2]]
	"""
	Réarrange la liste renvoyée par la fonction lit_fichier() en une liste de listes du type
	[['porte-avions', 1, 5], ['cuirasse', 1, 4], ['sous-marin', 1, 3], ['destroyer', 1, 2]], 
	la rendant plus facile à manipuler par la suite.
	
	Arguments:
		Aucun
		
	Valeurs de retour:
		contenu(list): liste de listes contenant le nom, le nombre et la taille des différents navires
		
	Exemple:
		print(liste_fichier())
		>>> [['porte-avions', 1, 5], ['cuirasse', 1, 4], ['sous-marin', 1, 3], ['destroyer', 1, 2]]
	"""
	contenu = lit_fichier() 
	    
	for i in range(len(contenu)):
		result = ""
		result_liste = []
		for j in range(len(contenu[i])):
			if contenu[i][j].isalpha() or contenu[i][j].isnumeric() or contenu[i][j] == "-":
				result = result + contenu[i][j]
			elif (contenu[i][j] == "\n" or contenu[i][j] == " ") and contenu[i][j-1].isnumeric():
				result_liste.append(int(result))
				result = ""
			elif(contenu[i][j] == "\n" or contenu[i][j] == " ") and contenu[i][j-1].isalpha():
				result_liste.append(result)
				result = ""
			else:
				pass
		contenu[i] = result_liste
		
	return contenu
#---------------------------------------art ascii OK

def art_ascii(tableau):
	"""
	Affiche le tableau avec l'emplacement des navires et les tirs reçus
	
	Arguments:
		- tableau(list): tableau contenant l'emplacement des navires d'un joueur et les tirs reçus par un joueur
		
	Valeurs de retour:
		Aucun
	"""
	dico = ["A","B","C","D","E","F","G","H","I","J"]
	print("  ", end="")
	for k in range(len(tableau)):
		print(" ", dico[k], end="")
	print("")
	for i in range(len(tableau)):
		print(i+1, end="")
		if i < 9:
			print(" ", end="")
		for j in range(len(tableau)*3):
			if j%3 == 0:
				print("|", end="")
			elif j%3 == 1:
				if tableau[j//3][i][0] != "":
					print(str.upper(tableau[j//3][i][0][0]), end="")
				else:
					print(" ", end="")
			else:
				if tableau[j//3][i][1]:
					print("!", end="")
				else:
					print(" ", end="")
		print("|")
		
def art_ascii2(tableau):
	"""
	Affiche le tableau avec l'emplacement des tirs réussi et des tirs ratés
	
	Arguments:
		- tableau(list): tableau contenant l'emplacement des navires d'un joueur et les tirs reçus par un joueur
		
	Valeurs de retour:
		Aucun
	"""	
	dico = ["A","B","C","D","E","F","G","H","I","J"]
	print("  ", end="")
	for k in range(len(tableau)):
		print(" ", dico[k], end="")
	print("")
	for i in range(len(tableau)):
		print(i+1, end="")
		if i < 9:
			print(" ", end="")
		for j in range(len(tableau)*3):
			if j%3 == 0:
				print("|", end="")
			elif j%3 == 1:
				if tableau[j//3][i][0] != "" and tableau[j//3][i][1] == True:
					print("T ", end="")
				elif tableau[j//3][i][1] == True:
					print("R ", end="")
				else:
					print("  ", end="")
		print("|")

#--------------------------------------verification victoire
def verif_si_bateau_coule(navires, tableau_joueur, bateaux_coules):      #bateaux_coules = [0,1,0,1]
	"""
	Affiche si le joueur a coule un bateau pendant ce tour ci
	
	Arguments:
		- tableau_joueur(list): tableau contenant l'emplacement des navires d'un joueur et les tirs reçus par un joueur
		- navires(list): liste des 4 navires existants contenant leurs noms, leurs nombres, et leurs tailles
		- bateaux_coules(list): liste contenant le nombre de bateaux coulés de chaque sorte
		
	Valeurs de retour:
		Aucun
	"""
	P = 0
	C = 0
	D = 0
	S = 0
	
	for i in range(len(tableau_joueur)):
		for j in range(len(tableau_joueur)):
			if tableau_joueur[i][j][1]:
				if tableau_joueur[i][j][0] == "cuirasse":
					C = C+1
				elif tableau_joueur[i][j][0] == "destroyer":
					D = D+1
				elif tableau_joueur[i][j][0] == "sous-marin":
					S = S+1
				elif tableau_joueur[i][j][0] == "porte-avions":
					P = P+1
			
	p_coules = P // navires[0][2]
	c_coules = C // navires[1][2]
	s_coules = S // navires[2][2]
	d_coules = D // navires[3][2]
	
	if p_coules > bateaux_coules[0]:
		bateaux_coules[0] = p_coules
		print("Vous avez coulé un porte-avions")
	elif c_coules > bateaux_coules[1]:
		bateaux_coules[1] = c_coules
		print("Vous avez coulé un cuirassé")
	elif s_coules > bateaux_coules[2]:
		bateaux_coules[2] = s_coules
		print("Vous avez coulé un sous-marin")
	elif d_coules > bateaux_coules[3]:
		bateaux_coules[3] = d_coules
		print("Vous avez coulé un destroyer")

def verif_victoire(tableau_joueur_1, tableau_joueur_2, navires):
	"""
	Vérifie si l'un des joueurs a gagné
	
	Arguments:
		- tableau_joueur_1(list): tableau contenant l'emplacement des navires du joueur1 et les tirs reçus par le joueur1
		- tableau_joueur_2(list): tableau contenant l'emplacement des navires du joueur2 et les tirs reçus par le joueur2
		- navires(list): liste des 4 navires existants contenant leurs noms, leurs nombres, et leurs tailles
		
	Valeurs de retour:
		Renvoie 0 si personne n'a gagne, 1 si le joueur 1 a gagné, et 2 si le joueur 2 a gagné
	"""
	nombre_de_touches_pour_gagne = 0
	j1 = 0
	j2 = 0
	
	for i in range(len(navires)):
		nombre_de_touches_pour_gagne = nombre_de_touches_pour_gagne + navires[i][2] * navires[i][1]
		
	for i in range(len(tableau_joueur_1)):
		for j in range(len(tableau_joueur_1)):
			if tableau_joueur_1[i][j][0] != "" and tableau_joueur_1[i][j][1]:
				j2 = j2+1
				
	for i in range(len(tableau_joueur_2)):
		for j in range(len(tableau_joueur_2)):
			if tableau_joueur_2[i][j][0] != "" and tableau_joueur_2[i][j][1]:
				j1 = j1+1
				
	if j1 == nombre_de_touches_pour_gagne:
		return 1
	elif j2 == nombre_de_touches_pour_gagne:
		return 2
	else: 
		return 0

#--------------------------------------tir joueur      

def verif_si_deja_tire(tir, tableau_IA):
	"""
	Vérifie si le joueur à déjâ tiré sur la case
	
	Arguments:
		- tir(liste): liste contenant les coordonnées du tir du joueur
		- tableau_IA(list): tableau contenant l'emplacement des navires de l'IA et les tirs reçus par l'IA
		
	Valeurs de retour:
		- Un booléen valant True si le joueur n'a pas encore tiré à cette emplacement
		  et False si il a déjâ tiré
		
	"""	
	if tableau_IA[tir[0]][tir[1]][1] == False:
		return True
	else:
		print("Vous avez déjâ tiré sur cette case\nVeuillez recommencer")
		return False

def tir_joueur(tableau_joueur, navires):
	"""
	Demande au joueur où il veut tiré et tir sur cette case
	
	Arguments:
		- tableau_IA(list): tableau contenant l'emplacement des navires de l'IA et les tirs reçus par l'IA
		- navires(list): liste des 4 navires existants contenant leurs noms, leurs nombres, et leurs tailles
		
	Valeurs de retour:
		Aucun
	"""
	tir_possible = False
	
	while not(tir_possible):
		tir = str(input("Entrez votre tir (ex:J7): "))
		tir_possible = verif_si_entree_possible(tir, tableau_joueur)
		if tir_possible:
			tir = transforme_joueur_ordi(tir)
			tir_possible = verif_si_deja_tire(tir, tableau_joueur)
			tableau_joueur[tir[0]][tir[1]][1] = True

#--------------------------------------tir IA
def coule(tirs_precedents, tableau_joueur, navires, tir):
	"""
	Arguments:
		- tableau_joueur(list): tableau contenant l'emplacement des navires du joueur et les tirs reçus par le joueur
		- tirs_precedents(list): liste contenant les informations sur les tirs précédents de l'IA, la cas, l'orientation et les coordonnées
		- tir(list): informations sur le tir actuel
		- navires(list): liste des 4 navires existants contenant leurs noms, leurs nombres, et leurs tailles
	
	Valeurs de retour:
		Renvoie True si cette case a achevé un navire, False dans le cas contraire
	"""
	nom_navire_touche = tableau_joueur[tir[2][0]][tir[2][1]][0]
	navire_touche = ["",10,10]
	for i in range(len(navires)):
		if nom_navire_touche == navires[i][0]:
			navire_touche = navires[i]
	j = 1
	k = 2
	while tirs_precedents[-j][0] != 2:
		if tableau_joueur[tirs_precedents[-j][2][0]][tirs_precedents[-j][2][1]][0] == nom_navire_touche:
			k = k+1
		j = j+1
		
	print(navire_touche)
	print(k)
	
	if k >= navire_touche[2]:
		return True
	else:
		return False

def cree_liste_100_cases():
	"""
	Crée une liste contenant les 100 premiers nombres.
	
	Arguments:
		Aucun
		
	Valeurs de retour:
		l(list): liste contenant les nombres de 0 à 99
	"""
	l = []
	for i in range(100):
		l.append(i)
	return l
	
def tir_aleatoire(tableau_joueur, liste_tir, tir):
	"""
	
	Arguments:
		- tableau_joueur(list): tableau contenant l'emplacement des navires du joueur et les tirs reçus par le joueur
		- liste_tir(list): liste allant de 0 à 99 permettant de choisir aléatoirement la case où l'IA va tirer
		- tir(list): liste contenant les informations sur le tir actuel
		
	Valeurs de retour:
		- touche(bool): booléen retournant True si un navire à été touché
	"""	
	tir_valide = False
	i=0
	touche = False
	
	while not(tir_valide):
		case = liste_tir.pop(0)
		x = case // 10
		y = case % 10
		if tableau_joueur[x][y][1] == True:
			tir_valide = False
		else:
			tableau_joueur[x][y][1] = True
			tir_valide = True
		
	if tableau_joueur[x][y][0] != "":
		tir[0] = 2
		touche = True
		
	tir[2][0] = x
	tir[2][1] = y
	return touche
	
def tir_semi_aleatoire(tableau_joueur, tirs_precedents, tir):
	"""
	Si l'aléatoire a touché un navire tir autour du point d'impact
	
	Arguments:
		- tableau_joueur(list): tableau contenant l'emplacement des navires du joueur et les tirs reçus par le joueur
		- tirs_precedents(list): liste contenant les informations sur les tirs précédents de l'IA, la cas, l'orientation et les coordonnées
		- tir(list): informations sur le tir actuel
		
	Valeurs de retour:
		Renvoie True si l'IA a touché et False dans le cas contraire
	"""	
	i = 1
	
	if tirs_precedents[-i][0] == 4:
		while tirs_precedents[-i][0] != 2:
			i = i+1
		
	tir_valide = False
	while not(tir_valide):
		tir_valide = True
		orientation = randint(0,3)
		
		if orientation == 0:
			x = tirs_precedents[-i][2][0]+1
			y = tirs_precedents[-i][2][1]
		elif orientation == 1:
			x = tirs_precedents[-i][2][0]
			y = tirs_precedents[-i][2][1]+1
		elif orientation == 2:
			x = tirs_precedents[-i][2][0]-1
			y = tirs_precedents[-i][2][1]
		else:
			x = tirs_precedents[-i][2][0]
			y = tirs_precedents[-i][2][1]-1
				
		if x>9 or x<0 or y>9 or y<0:
			tir_valide = False
		elif tableau_joueur[x][y][1]:
			tir_valide = False
				
	tableau_joueur[x][y][1] = True
	
	tir[1] = orientation
	tir[2][0] = x
	tir[2][1] = y
	
	if tableau_joueur[x][y][0] != "":
		tir[0] = 3
		return True
	else:
		tir[0] = 4
		return False
		
def tir_non_aleatoire2(tableau_joueur, tirs_precedents, tir):
	"""
	Si l'IA arrive en bout de ligne d'une série de tirs et n'a toujours pas coulé, alors revient en arrière
	
	Arguments:
		- tableau_joueur(list): tableau contenant l'emplacement des navires du joueur et les tirs reçus par le joueur
		- tirs_precedents(list): liste contenant les informations sur les tirs précédents de l'IA, la cas, l'orientation et les coordonnées
		- tir(list): informations sur le tir actuel
		
	Valeurs de retour:
		Renvoie True si l'IA a touché et False dans le cas contraire
		
	"""	
	i = 1
	while tirs_precedents[-i][0] != 1:
		i = i+1
	orientation = tirs_precedents[-1][1]+2 % 4
	
	if orientation == 0:
		x = tirs_precedents[-i][2][0]+1
		y = tirs_precedents[-i][2][1]
	elif orientation == 1:
		x = tirs_precedents[-i][2][0]
		y = tirs_precedents[-i][2][1]+1
	elif orientation == 2:
		x = tirs_precedents[-i][2][0]-1
		y = tirs_precedents[-i][2][1]
	else:
		x = tirs_precedents[-i][2][0]
		y = tirs_precedents[-i][2][1]-1
		
	tir[2][0] = x
	tir[2][1] = y
	
	tableau_joueur[x][y][1] = True
	if tableau_joueur[x][y][0] != "":
		return True
	else: 
		return False
	
	
def tir_non_aleatoire1(tirs_precedents, tableau_joueur, tir, navires):
	"""
	Tir en ligne droite si deux case ont été touché
	
	Arguments:
		- tableau_joueur(list): tableau contenant l'emplacement des navires du joueur et les tirs reçus par le joueur
		- tirs_precedents(list): liste contenant les informations sur les tirs précédents de l'IA, la cas, l'orientation et les coordonnées
		- tir(list): informations sur le tir actuel
		- navires(list): liste des 4 navires existants contenant leurs noms, leurs nombres, et leurs tailles
		
	Valeurs de retour:
		Renvoie True si l'IA a touché et False dans le cas contraire
	"""
	
	orientation = tirs_precedents[-1][1]
	tir[0] = 3
	tir[1] = orientation
	
	if orientation == 0:
		x = tirs_precedents[-1][2][0]+1
		y = tirs_precedents[-1][2][1]
	elif orientation == 1:
		x = tirs_precedents[-1][2][0]
		y = tirs_precedents[-1][2][1]+1
	elif orientation == 2:
		x = tirs_precedents[-1][2][0]-1
		y = tirs_precedents[-1][2][1]
	else:
		x = tirs_precedents[-1][2][0]
		y = tirs_precedents[-1][2][1]-1
	
	tir[2][0] = x
	tir[2][1] = y
		
	if x>9 or x<0 or y>9 or y<0:
		touche = tir_non_aleatoire2(tableau_joueur, tirs_precedents, tir)
	elif tableau_joueur[x][y][1]:
		touche = tir_non_aleatoire2(tableau_joueur, tirs_precedents, tir)
	else:
		tableau_joueur[x][y][1] = True
		if tableau_joueur[x][y][0] != "":
			touche = True
		else:
			touche = False
			
	#if tableau_joueur[tirs_precedents[-1][2][0]][tirs_precedents[-1][2][1]][0] != "":
		#print(coule(tirs_precedents, tableau_joueur, navires, tir))
	
	if touche and coule(tirs_precedents, tableau_joueur, navires, tir):
		tir[0] = 1
		
	return touche
	
	
def tir_IA(tableau_joueur, tirs_precedents, navires):      #ex tirs_precedent: [[1,-1,[2,5]],[2,0,[3,6]]] [orientaton(-1 si aléatoire)[x,y]]  
	"""
	
	Arguments:
		- tableau_joueur(list): tableau contenant l'emplacement des navires du joueur et les tirs reçus par le joueur
		- tirs_precedents(list): liste contenant les informations sur les tirs précédents de l'IA, la cas, l'orientation et les coordonnées
		- navires(list): liste des 4 navires existants contenant leurs noms, leurs nombres, et leurs tailles
		
	Valeurs de retour:
		Aucun
		
	"""
	liste_tir = cree_liste_100_cases()
	shuffle(liste_tir)
	tir = [1,-1,[-1,-1]]
	touche = False
	
	tir_valide = False
	
	if tirs_precedents[-1][0] == 1:
		touche = tir_aleatoire(tableau_joueur, liste_tir, tir)
	elif tirs_precedents[-1][0] == 2 or tirs_precedents[-1][0] == 4:
		touche = tir_semi_aleatoire(tableau_joueur, tirs_precedents, tir)
	elif tirs_precedents[-1][0] == 3:
		touche = tir_non_aleatoire1(tirs_precedents, tableau_joueur, tir, navires)
		
	print("l'IA tir en " ,transforme_ordi_joueur([tir[2][0],tir[2][1]]))		
	tirs_precedents.append(tir)

#----------------------------------------phase de tir

def phase_de_tir_PvIA(navires,tableau_IA,tableau_joueur):
	"""
	Fait les tirs, affiche les tableaux et vérifie s'il y a un vainqueur
	
	Arguments:
		- navires(list): liste des 4 navires existants contenant leurs noms, leurs nombres, et leurs tailles
		- tableau_IA(list): tableau contenant l'emplacement des navires de l'IA et les tirs reçus par l'IA
		- tableau_joueur(list): tableau contenant l'emplacement des navires du joueur et les tirs reçus par le joueur
		
	Valeurs de retour:
		Aucun
	"""
	fin_partie = 0
	tirs_precedent_IA = [[1,-1,[-1,-1]]]   
	bateaux_coules_IA = [0,0,0,0]
	while fin_partie == 0:
		print("Vos bateaux :")
		art_ascii(tableau_joueur)
		print("Vos tirs")
		art_ascii2(tableau_IA)
		touche_joueur = tir_joueur(tableau_IA, navires)
		verif_si_bateau_coule(navires, tableau_IA, bateaux_coules_IA)
		tir_IA(tableau_joueur, tirs_precedent_IA, navires)
		
		fin_partie = verif_victoire(tableau_IA, tableau_joueur, navires)
		
		if fin_partie == 1:
			print("")
			print("L'IA gagne")
		elif fin_partie == 2:
			print("")
			print("Le joueur gagne")
		
def phase_de_tir_PvP(navires,tableau_joueur_1,tableau_joueur_2):
	"""
	Fait les tirs, affiche les tableaux et vérifie s'il y a un vainqueur
	
	Arguments:
		- navires(list): liste des 4 navires existants contenant leurs noms, leurs nombres, et leurs tailles
		- tableau_joueur_1(list): tableau contenant l'emplacement des navires du joueur1 et les tirs reçus par le joueur1
		- tableau_joueur_1(list): tableau contenant l'emplacement des navires du joueur2 et les tirs reçus par le joueur2
		
	Valeurs de retour:
		Aucun
	"""
	fin_partie = 0
	bateaux_coules_j2 = [0,0,0,0]
	bateaux_coules_j1 = [0,0,0,0]
	
	while fin_partie == 0:
		print("\nTir joueur1")
		print("\nVos bateaux")
		art_ascii(tableau_joueur_1)
		print("Vos tirs")
		art_ascii2(tableau_joueur_2)
		tir_joueur(tableau_joueur_2, navires)
		verif_si_bateau_coule(navires, tableau_joueur_2, bateaux_coules_j2)
		
		print("\nTir joueur2")
		print("\nVos bateaux")
		art_ascii(tableau_joueur_2)
		print("Vos tirs")
		art_ascii2(tableau_joueur_1)
		tir_joueur(tableau_joueur_1, navires)
		verif_si_bateau_coule(navires, tableau_joueur_1, bateaux_coules_j1)
		
		fin_partie = verif_victoire(tableau_joueur_1, tableau_joueur_2, navires)
		
		if fin_partie == 1:
			print("")
			print("Le joueur1 gagne\n")
		elif fin_partie == 2:
			print("")
			print("Le joueur2 gagne\n")

#--------------------------------------placement navire joueur

def demande_case_et_msgerreur(navire):
	"""
	Demande où le joueur veut placer son navire, et affiche un message 
	d'erreur si cette case n'est pas valide.
	
	Arguments:
		navire: liste contenant les informations sur un navire
		ex : ['sous-marin', 1, 3]
		
	Valeurs de retour:
		case(str): coordonnées de la case choisie en string, ex: e5
	"""	
	bonne_entree = False
	while not bonne_entree:
		bonne_entree = False
		case=str(input("A quelle case voulez-vous placer votre "+navire[0]+"? : (ex:H6) ")).lower()
		if len(case) == 2:
			if 'a' <= case[0] <= 'j':
				if '1' <= case[1] <= '9':
					bonne_entree = True
				else:
					print("Le deuxième nombre doit être un chiffre entre 1 et 10.")
			else:
				print("Il faut une lettre en première position entre a et j.")
		elif len(case)==3:
			if 'a' <= case[0] <= 'j':
				if case[1:] == '10':
					bonne_entree = True
				else:
					print("Le deuxième nombre doit être un chiffre entre 1 et 10.")
			else:
				print("Il faut une lettre en première position entre a et j.")
		else:
			print("Ce n'est pas le bon nombre de paramètres")
				

	return case
	
def determine_orientation_joueur(x,y,navire,length):
	"""
	Détermine l'orientation du navire s'il n'y en a qu'une possible, ou 
	renvoit orientation = None si l'orientation doit être définie par le joueur.
	
	Arguments:
		x(int): coordonnée en x 
		y(int): coordonnée en y 
		navire(list): informations sur le navire, ex : ['sous-marin', 1, 3]
		length(int): longueur de la liste "tableau_joueur"
		
	Valeurs de retour: 
		orientation(int/str): orientation prédéterminée
	"""

	if x > length-navire[2] and y < navire[2]:
		orientation = -1
	elif y < navire[2]:
		orientation = 0 
	elif x > length-navire[2]:
		orientation = 1
	else:
		orientation = None 
	return orientation

def placement_navires_joueur(tableau_joueur, navires):
	"""
	Fonction principale du placement des navires du joueur, demande, 
	pour chaque navire, où le joueur souhaite le placer, et modifie 
	la variable "tableau_joueur" en conséquence.
	
	Arguments:
		tableau_joueur(list): liste de listes faisant office de grille
		navires(list): liste de listes contenant les informations sur les navires
		
	Valeurs de retour:
		tableau_joueur(list): tableau complété par les bateaux du joueur
	"""
	dico = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9}
	length = len(tableau_joueur)
	for navire in navires:
		for j in range(navire[1]):
			bonneplace = False
			art_ascii(tableau_joueur)
			while not bonneplace:
				bonneplace = True
				case = demande_case_et_msgerreur(navire)
				x = dico[case[0]]
				y = int(case[1:])-1
				orientation = determine_orientation_joueur(x,y,navire, length)
				bonne_orientation = False
				while bonne_orientation == False:
					bonne_orientation = True
					
					tableau_joueur, bonne_orientation = demande_orientation(orientation,tableau_joueur,navire, x, y)

					if not bonne_orientation:
						print("Choisissez une autre case")
						bonne_orientation = True	
						bonneplace = False
					 
	return tableau_joueur
	
def demande_orientation(orientation,tableau_joueur,navire, x, y):
	"""
	En fonction de la valeur de "orientation", demande au joueur l'orientation 
	de son navire, ou défini directement l'orientation adéquate.
	Affiche un message d'erreur si les cases ne sont pas libres.
	
	Arguments:
		orientation(int/str): None si pas encore définie, 0 si droite, 1 si haut
		tableau_joueur(list): liste de listes représentant la grille du joueur
		navire(list): liste contenant les informations sur un navire
		x(int): coordonnée en x 
		y(int): coordonnée en y
		
	Valeurs de retour:
		tableau_joueur(list): liste de listes modifiée représentant la grille du joueur
		bonne_orientation(bool): True si l'orientation est valide, False si non
	"""
	if orientation is None:
		orientation=int(input("Choisissez l'orientation de votre "+navire[0]+": 1 pour haut, 0 pour droite "))
	if orientation == 0:
		bonne_orientation=True
		for m in range(navire[2]):
			if not tableau_joueur[x+m][y][0] == "":
				bonne_orientation = False
		if not bonne_orientation:
			print("Ces cases ne sont pas libres. Recommencez")

		else :
			for m in range(navire[2]):
				tableau_joueur[x+m][y][0] = navire[0]

	elif orientation == 1:
		bonne_orientation=True
		for m in range(navire[2]):
			if not tableau_joueur[x][y-m][0] == "":
				bonne_orientation = False
		if not bonne_orientation:
			print("Ces cases ne sont pas libres. Recommencez")
						
		else :
			for m in range(navire[2]):
				tableau_joueur[x][y-m][0]=navire[0]
	elif orientation == -1:
		print("Impossible de mettre le bateau à cet endroit.")
		bonne_orientation=False
	else :
		print("Cette orientation n'existe pas. Recommencez")
		bonne_orientation=False

	return tableau_joueur, bonne_orientation
#--------------------------------------placement navire IA         

def determine_orientation(tableau_IA, navire, x, y):
	"""
	En fonction de la position d'origine du navire, détermine son orientation
	
	Arguments:
		- tableau_IA(list): tableau contenant l'emplacement des navires de l'IA et les tirs reçus par l'IA
		- navires(list): liste des 4 navires existants contenant leurs noms, leurs nombres, et leurs tailles
		- x(int): coordonnée de la case d'origine du navire
		- y(int): coordonnée de la case d'origine du navire
		
	Valeurs de retour:
		renvoie l'orientation dans laquelle le navire doit être placé 0 pour la droite, 1 pour le haut, -1 s'il doit être replacé
	"""	
	if x > len(tableau_IA)-navire[2] and y > len(tableau_IA)-navire[2]:
		orientation = -1
	elif y > len(tableau_IA)-navire[2]:
		orientation = 0
	elif x > len(tableau_IA)-navire[2]:
		orientation = 1
	else:
		orientation = randint(0,1)
	return orientation
	
def verif_si_peut_placer(tableau_IA, longueur_navire, orientation, x, y):
	"""
	Vérifie si les emplacements où l'IA veut mettre ses navires ne sont pas occupés
	
	Arguments:
		- tableau_IA(list): tableau contenant l'emplacement des navires de l'IA et les tirs reçus par l'IA
		- longueur_navire(int): longueur du navire à placer
		- orientation(int): orientation dans lequel le navire doit être placé
		- x(int): coordonnée de la case d'origine du navire
		- y(int): coordonnée de la case d'origine du navire
		
	Valeurs de retour:
		booléen valant True si le navire peut être placé et False s'il ne peut être placé
	"""	
	verif = True
	
	for i in range(longueur_navire):
		if orientation == 0:
			if tableau_IA[x+i][y][0] != "":
				verif = False
		elif orientation == 1:
			if tableau_IA[x][y+i][0] != "":
				verif = False
		else:
			pass
			
	return verif
	
def place_navire(tableau_IA, navire, x, y, orientation):
	"""
	Place le navire concerné à la place indiqué
	
	Arguments:
		- navires(list): liste des 4 navires existants contenant leurs noms, leurs nombres, et leurs tailles
		- tableau_IA(list): tableau contenant l'emplacement des navires de l'IA et les tirs reçus par l'IA
		- x(int): coordonnée de l'emplacement où placer
		- y(int): coordonnée de l'emplacement où placer
		
	Valeurs de retour:
		Aucun
	"""	
	for i in range(navire[2]):
		if orientation == 0:
			tableau_IA[x+i][y][0] = navire[0]
		else:
			tableau_IA[x][y+i][0] = navire[0]
			
def placement_navires_IA(tableau_IA, navires):
	"""
	Place les navires de l'IA de façob aléatoire
	
	Arguments:
		- navires(list): liste des 4 navires existants contenant leurs noms, leurs nombres, et leurs tailles
		- tableau_IA(list): tableau contenant l'emplacement des navires de l'IA et les tirs reçus par l'IA
		
	Valeurs de retour:
		Aucun
	"""	
	for i in range(len(navires)):
		for j in range(navires[i][1]):
			bien_place = False
			while bien_place == False:
				x = randint(0, len(tableau_IA)-1)
				y = randint(0, len(tableau_IA)-1)
				
				orientation = determine_orientation(tableau_IA, navires[i], x, y)
				
				verif = verif_si_peut_placer(tableau_IA, navires[i][2], orientation, x, y)
				
				if orientation != -1 and verif == True:
					place_navire(tableau_IA, navires[i], x, y, orientation)
					bien_place = True

#---------------------------------------partie principale
def cree_tableau():
	"""
	Crée un tableau vide 10x10 contenant des ["",False]
	
	Arguments:
		Aucun
		
	Valeurs de retour:
		tableau(list): liste de listes contenant des ["",False]
	"""
	tableau = []
	for i in range(10):
		tableau.append([])
		for j in range(10):
			tableau[i].append(["",False])
	return tableau

def lance_jeu(navires):
	"""
	Propose au joueur le mode multijoueur ou non.
	Pour chacun des cas, demande au(x) joueur(s) de placer leurs navires 
	puis passe à la phase de tir
	
	Arguments:
		- navires(list): liste des 4 navires existants contenant leurs noms, leurs nombres, et leurs tailles
		
	Valeurs de retour:
		Aucun	
	"""	
	multijoueur = str(input("Mode multijoueur ? (o/n) : "))
	
	if multijoueur == "o":
		tableau_joueur_1 = cree_tableau()
		tableau_joueur_2 = cree_tableau()
		
		print("")
		print("Placement des bateaux du joueur1")
		print("")
		placement_navires_joueur(tableau_joueur_1, navires)
		
		print("")
		print("Placement des bateaux du joueur2")
		print("")
		placement_navires_joueur(tableau_joueur_2, navires)
		
		phase_de_tir_PvP(navires,tableau_joueur_1,tableau_joueur_2)
	else:
		tableau_IA = cree_tableau()                                              
		tableau_joueur = cree_tableau()                                          
	
		placement_navires_IA(tableau_IA, navires)                                
		placement_navires_joueur(tableau_joueur, navires)
	
		phase_de_tir_PvIA(navires,tableau_IA,tableau_joueur)

def touche_coule():
	"""
	Lance le jeu et propose à l'utilisateur de rejoueur en fin de partie
	
	Arguments:
		Aucun
	Valeurs de retour:
		Aucun
	"""	
	rejouer = "o"
	print("Bienvenue dans notre jeu Touché-Coulé.\nLes règles sont simples : placer d'abord vos navires, puis tenter de toucher les navires adverses. \nLe premier qui élimine tous les navires ennemis remporte la victoire. \nAttention: Pour le placement des navires, choisissez d'abord la case d'origine, puis si vous voulez faire partir votre bateau vers le haut ou vers la droite seulement. \nA vous de jouer maintenant!")
	while rejouer == "o":
		navires = liste_fichier()
		lance_jeu(navires)
		rejouer = str(input("Voulez-vous rejouer ? (o/n) : "))
	
touche_coule()




