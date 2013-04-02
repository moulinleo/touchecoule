from random import randint
from random import shuffle
from tkinter import *


#----------------------------------------entrees joueur        OK

def transforme_joueur_ordi(tir): 
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
	
def transforme_ordi_joueur(case): 
	"""
	Transforme une liste de 2 nombres par une case sur la grille.
	
	Arguments:
		case(list): liste de 2 nombres
		
	Valeurs de retour:
		tir(str): coordonnées entrées par le joueur
		
	Exemple:
		print(transforme_ordi_joueur([9,4]))
		>>>J5
	"""									#[9, 4] => J5
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
	Exemple:
		
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
	
#----------------------------------------lit fichier navires.dat        OK
def lit_fichier(): 
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
	
def liste_fichier():    
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
#---------------------------------------interface graphique avec Tkinter        peut etre art ascii

def art_ascii(tableau):
	"""
	
	Arguments:
		
	Valeurs de retour:
		
	Exemple:
		
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
					print("°", end="")
				else:
					print(" ", end="")
		print("|")
		
def art_ascii2(tableau):
	"""
	
	
	Arguments:
		
	Valeurs de retour:
		
	Exemple:
		
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
					print("P ", end="")
				else:
					print("  ", end="")
		print("|")


#--------------------------------------verification navire détruit


#--------------------------------------tir joueur      OK

def verif_si_deja_tire(tir, tableau_IA):
	"""
	
	Arguments:
		
	Valeurs de retour:
		
	Exemple:
		
	"""	
	if tableau[tir[0]][tir[1]][1] == False:
		return True
	else:
		print("Vous avez déjâ tiré sur cette case\nVeuillez recommencer")
		return False

def tir_joueur(tableau_IA, navires, tirs_precedent): 
	"""
	
	Arguments:
		
	Valeurs de retour:
		
	Exemple:
		
	"""	
	tir_possible = False
	
	while not(tir_possible):
		tir = str(input("Entrez votre tir (ex:J7): "))
		tir_possible = verif_si_entree_possible(tir, tableau_IA)
		if tir_possible:
			tir = transforme_joueur_ordi(tir)
			tir_possible = verif_si_deja_tire(tir, tableau_IA)
			
		if tir_possible:
			tableau[tir[0]][tir[1]][1] = True
			
	tirs_precedent.append(tir)
		


#--------------------------------------tir IA

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
		
	Valeurs de retour:
		
	Exemple:
		
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
	
	Arguments:
		
	Valeurs de retour:
		
	Exemple:
		
	"""	
	tir_valide = False
	while not(tir_valide):
		tir_valide = True
		orientation = randint(0,3)
		
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
		
		if orientation == 0:
			if tirs_precedents[-1][2][0]+1 > 9:
				tir_valide = False
			elif tableau_joueur[x][y][1]:
				tir_valide = False
		elif orientation == 1:
			if tirs_precedents[-1][2][1]+1 > 9:
				tir_valide = False
			elif tableau_joueur[x][y][1]:
				tir_valide = False
		elif orientation == 2:
			if tirs_precedents[-1][2][0]-1 < 0:
				tir_valide = False
			elif tableau_joueur[x][y][1]:
				tir_valide = False
		else:
			if tirs_precedents[-1][2][1]-1 < 0:
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
		tir[0] = 2
		return False
	
def tir_non_aleatoire1(tirs_precedent, tableau_joueur, tir):
	"""
	
	
	Arguments:
		
	Valeurs de retour:
		
	Exemple:
		
	"""	
	if tirs_precedent[len(tirs_precedent)-1]:
		a=0
	
	
def tir_IA(tableau_joueur, tirs_precedents): 
	"""
	
	Arguments:
		
	Valeurs de retour:
		
	Exemple:
		
	"""	     #ex tirs_precedent: [[1,-1,[2,5]],[2,0,[3,6]]] [orientaton(-1 si aléatoire)[x,y]]  
	liste_tir = cree_liste_100_cases()
	shuffle(liste_tir)
	tir = [1,-1,[-1,-1]]
	touche = False
	
	tir_valide = False
	
	if tirs_precedents[-1][0] == 1:
		touche = tir_aleatoire(tableau_joueur, liste_tir, tir)
	elif tirs_precedents[-1][0] == 2:
		touche = tir_semi_aleatoire(tableau_joueur, tirs_precedents, tir)
	elif tirs_precedents[-1][0] == 3:
		touche = tir_non_aleatoire1(tableau_joueur, tirs_precedents, tir)
		
			
	tirs_precedents.append(tir)
		
			
	     #peut etre renvoyer les coor x et y pour la verif de tir
		
	
	

#----------------------------------------phase de tir

def phase_de_tir(navires,tableau_IA,tableau_joueur):
	"""
	
	Arguments:
		
	Valeurs de retour:
		
	Exemple:
		
	"""	
	fin_partie = False
	tirs_precedent_joueur = []
	tirs_precedent_IA = [[1,-1,[-1,-1]]]   #[orientation, x, y] si veux tir aléatoire orientation = -1
	while not(fin_partie):                       #une variable qui compte le nombre de navire détruit chez chacun ?????
		print("Vos batteaux :")
		art_ascii(tableau_joueur)
		print("Vos tirs")
		art_ascii2(tableau_IA)
		touche_joueur = tir_joueur(tableau_IA, navires, tirs_precedent_joueur)
		tir_IA(tableau_joueur, tirs_precedent_IA)
		
		fin_partie = verif_victoire(tableau_IA, tableau_joueur)


#--------------------------------------placement navire joueur (doit etre polyvalent si multijoueur)

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
#--------------------------------------placement navire IA         OK

def determine_orientation(tableau_IA, navire, x, y):
	"""
	
	Arguments:
		
	Valeurs de retour:
		
	Exemple:
		
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
	
	Arguments:
		
	Valeurs de retour:
		
	Exemple:
		
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
	
def place_navire(tableau_IA, navire, orientation, x, y):
	"""
	
	Arguments:
		
	Valeurs de retour:
		
	Exemple:
		
	"""	
	for i in range(navire[2]):
		if orientation == 0:
			tableau_IA[x+i][y][0] = navire[0]
		else:
			tableau_IA[x][y+i][0] = navire[0]
			
def placement_navires_IA(tableau_IA, navires):
	"""
	
	Arguments:
		
	Valeurs de retour:
		
	Exemple:
		
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
					place_navire(tableau_IA, navires[i], orientation, x, y)
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
	
	Arguments:
		
	Valeurs de retour:
		
	Exemple:
		
	"""	
	tableau_IA = cree_tableau()                                              #création des tableaux OK
	tableau_joueur = cree_tableau()                                          # OK
	
	placement_navires_IA(tableau_IA, navires)                                #placement des navires du joueur et de l'IA OK
	placement_navires_joueur(tableau_joueur, navires)
	
	phase_de_tir(navires,tableau_IA,tableau_joueur)
	
	
	

def touche_coule():
	"""
	
	Arguments:
		
	Valeurs de retour:
		
	Exemple:
		
	"""	
	rejouer = "o"
	
	while rejouer == "o":
		navires = liste_fichier()
		lance_jeu(navires)
		rejouer = str(input("Voulez-vous rejouer ? (o/n) : "))
	return 0
"""	
tableau = cree_tableau()
placement_navires_IA(tableau, liste_fichier())
tir_IA(tableau, [-1,0,0])
print(tableau)
"""
"""
tableau = cree_tableau()
placement_navires_joueur(tableau, liste_fichier())
print(tableau)

"""
"""
tableau = cree_tableau()
placement_navires_IA(tableau, liste_fichier())
for i in range(2):
	tir_joueur(tableau, liste_fichier, [])
art_ascii(tableau)
"""
tableau = cree_tableau()
placement_navires_joueur(tableau, liste_fichier())
art_ascii(tableau)




