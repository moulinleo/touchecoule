from random import randint
from random import shuffle
from tkinter import *


#----------------------------------------entrees joueur

dico = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9}
def transforme_joueur_ordi(tir):                                        #J5 => [9, 4]
	case = [dico[str.lower(tir[0])]]
	y=""
	for i in range(len(tir)-1):
		y = y+tir[i+1]
	case.append(int(y)-1)
	return case
	
def transforme_ordi_joueur(case):                                        #[9, 4] => J5
	dico = ["A","B","C","D","E","F","G","H","I","J"]
	return dico[case[0]] + str(case[1]+1)
	
def verif_si_entree_possible(entree):
	dico = ["A","B","C","D","E","F","G","H","I","J"]
	nombre = ""
	result = True
	
	if not(str.upper(entree[0]) in dico):
		result = False
		
	for i in range(len(entree)-1):
		nombre = nombre + entree[i+1]
		if not(entree[i+1].isnumeric()):
			result = False
			
	if result != False and (int(nombre)>10 or int(nombre)<1):
		result = False
	return result
	
#----------------------------------------lit fichier navires.dat
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
#---------------------------------------interface graphique avec Tkinter


#--------------------------------------verification navire détruit


#--------------------------------------tir joueur

def verif_tir_joueur(tir, tableau_IA):
	"""
	
	"""
	if tir[0]<0:
		a=0

def tir_joueur(tableau_IA, navires, tirs_precedent):
	"""
	"""
	
	tir_possible = False
	
	while not(tir_possible):
		tir = transforme_joueur_ordi(str(input("Entrez votre tir (ex:J7): ")))
		tir_possible = verif_tir_joueur(tir, tableau_IA)
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
	
def tir_aleatoire(tableau_joueur, liste_tir):
	"""
	Fait tirer aléatoirement l'IA sur une case de coordonnées x, y , 
	et modifie la variable "tableau_joueur" en fonction du tir (touché ou coulé)
	
	Arguments:
		tableau_joueur(list): liste de listes contenant
		
	Valeurs de retour:
		tir_valide(bool): True si le tir est valide, False si non.
	"""    
	case = liste_tir.pop(0)
	x = case // 10
	y = case % 10
	if tableau_joueur[x][y][1] == True:
		tir_valide = False
	else:
		tableau_joueur[x][y][1] = True
		tir_valide = True
	print("")
	print(x,y)
	return tir_valide
	
def tir_IA(tableau_joueur, tir_precedent):
	"""
	
	"""    
	liste_tir = cree_liste_100_cases()
	shuffle(liste_tir)
	tir_valide = False
	
	while not(tir_valide):
		if tir_precedent[0] == -1:
			tir_valide = tir_aleatoire(tableau_joueur, liste_tir)
			
	     #peut etre renvoyer les coor x et y pour la verif de tir
		
	
	

#----------------------------------------phase de tir

def phase_de_tir(navires,tableau_IA,tableau_joueur):
	"""
	Phase de tir principale, faisant tirer à tour de rôle l'IA et le joueur,
	si la partie n'est pas encore finie.
	
	Arguments:
		navires(list): liste de listes contenant toutes les informations sur les navires : du type [["navire1",nombre,taille],["navires2",nombre,taille]...]
		tableau_IA(list): liste de listes de type : [[["",False],["",False]..],[["",False]..]...], représente la grille de l'IA
		tableau_joueur(list): liste de listes de type : [[["",False],["",False]..],[["",False]..]...], représente la grille du joueur
		
	Valeurs de retour:
		Aucune
	"""
	fin_partie = False
	tirs_precedent_joueur = []
	tir_precedent_IA = [-1,0,0]   #[orientation, x, y] si veux tir aléatoire orientation = -1
	while not(fin_partie):                       #une variable qui compte le nombre de navire détruit chez chacun ?????
		touche_joueur = tir_joueur(tableau_IA, navires, tirs_precedent_joueur)
		tir_IA(tableau_joueur, tir_precedent_IA)
		
		fin_partie = verif_victoire(tableau_IA, tableau_joueur)


#--------------------------------------placement navire joueur (doit etre polyvalent si multijoueur)

def demande_case_et_msgerreur(navire):
	"""
	Demande au joueur la case où il veut placer son navire, et vérifie si cette case existe.
	
	Arguments:
		navires(list): liste de listes du type : [["navire1",nombre,taille],["navires2",nombre,taille]...]
		
	Valeurs de retour:
		case(int): nombre dont le premier chiffre contient la coordonnées en x et le deuxième la coordonnée en y
		
	Exemple:
		
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
					print("Le deuxiemme nombre doit etre un chiffre entre 1 et 10.")
			else:
				print("Il faut une lettre en première position entre a et j.")
		elif len(case)==3:
			if 'a' <= case[0] <= 'j':
				if case[1:] == '10':
					bonne_entree = True
				else:
					print("Le deuxiemme nombre doit etre un chiffre entre 1 et 10.")
			else:
				print("Il faut une lettre en première position entre a et j.")
		else:
			print("Ce n'est pas le bon nombre de paramètre")
				

	return case
	
def determine_orientation_joueur(x,y,navire, length):
	"""
	
	Arguments:
		Aucun
		
	Valeurs de retour:
		
		
	Exemple:
		
	"""
	if x > length-navire[2] and y < length-navire[2]:
		orientation = -1
	elif y < navire[2]:
		orientation = "droite"
	elif x > length-navire[2]:
		orientation = "haut"
	else:
		orientation = "choix"
	return orientation


def placement_navires_joueur(tableau_joueur, navires):
	"""
	
	Arguments:
		Aucun
		
	Valeurs de retour:
		
		
	Exemple:
		
	"""
	length = len(tableau_joueur)
	for navire in navires:
		for j in range(navire[1]):
			bonneplace = False
			while not bonneplace:
				bonneplace = True
				case = demande_case_et_msgerreur(navire)
				x = dico[case[0]]
				y = int(case[1:])-1
				
				if not(0 <= x < length-navire[2]) and not(0 <= y < length-navire[2]):
					print("Choisissez une autre case")
					bonneplace = False
				else:
					orientation = determine_orientation_joueur(x,y,navire, length)
					bonne_orientation = False
					while bonne_orientation == False:
						if orientation == 'choix':
							tableau_joueur, bonne_orientation = demande_orientation(orientation,tableau_joueur,navire, x, y)
						elif orientation == "droite":
							bonne_orientation=True
							for m in range(navire[2]):
								if tableau_joueur[x+m][y][0] == "":
									tableau_joueur[x+m][y][0]=navire[0]
							
						elif orientation == "haut":
							bonne_orientation=True
							for m in range(navire[2]):
								if tableau_joueur[x][y+m][0] == "":
									tableau_joueur[x][y+m][0]=navire[0]
						else:
							bonneplace = False
							bonne_orientation = True
							print("Choisissez une autre case")
					 
	return tableau_joueur
	
def demande_orientation(orientation,tableau_joueur,navire, x, y):
	"""
	
	Arguments:
		Aucun
		
	Valeurs de retour:
		
		
	Exemple:
		
	"""
	if orientation == "choix":
		orientation=int(input("Choisissez l'orientation de votre "+navire[0]+": 1 pour haut, 0 pour droite "))
		if orientation == 0:
			bonne_orientation=True
			for m in range(navire[2]):
				if tableau_joueur[x+m][y][0] == "":
					tableau_joueur[x+m][y][0] = navire[0]
				else :
					print("Ces cases ne sont pas libres. Recommencez")
		elif orientation == 1:
			bonne_orientation=True
			for m in range(navire[2]):
				print(x, y, m)
				if tableau_joueur[x][y-m][0] == "":
					tableau_joueur[x][y-m][0]=navire[0]
				else :
					print("Ces cases ne sont pas libres. Recommencez")
							
		else :
			print("Cette orientation n'existe pas. Recommencez")
			bonne_orientation=False

		return tableau_joueur, bonne_orientation

#--------------------------------------placement navire IA

def determine_orientation(tableau_IA, navire, x, y):
	"""
	
	Arguments:
		Aucun
		
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
		Aucun
		
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
		Aucun
		
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
		Aucun
		
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
	Crée un tableau vide (10x10) contenant des ["",False]
	
	Arguments:
		Aucun
		
	Valeurs de retour:
		
		
	Exemple:
		
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
		Aucun
		
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
	Fonction principale, qui relance la fonction lance_jeu si le joueur désire rejouer.
	
	Arguments:
		Aucun
		
	Valeurs de retour:
		Aucune
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

