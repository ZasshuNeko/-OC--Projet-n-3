# -*-coding:Utf-8 -*

"""Ce fichier contient le module qui gère la class labyrinthe
"""

import sys
import os
from module_actions import *
from Class_Personnage import *
from Class_Items import *
import pygame
from pygame.locals import *
import random

class Maze:
	#définis la classe du niveau mettre des attributs utilisable
	def __init__(self):
		# On charge les cartes existantes / We load the existing cards
		cartes = []
		for nom_fichier in os.listdir("cartes"):
			if nom_fichier.endswith(".txt"):
				chemin = os.path.join("cartes", nom_fichier)
				nom_carte = nom_fichier[:-4].lower() 
				with open(chemin, "r") as fichier:
					contenu = fichier.read()
					self.nom = nom_carte
					self.labyrinthe = list(contenu)
					Carte_Save = [self.labyrinthe,self.nom]
					if not(cartes):
						cartes = [Carte_Save]
					else:
						cartes.append(Carte_Save)

		map_select = self.labyrinthe
		self.maze_map = creating_dictionary(map_select)
		self.listing_item = self.maze_map[1]

	def creating_map (self,screen):
		img_floor = pygame.image.load('ressources/One-tiles-20x20-Floor-Big.png').convert()
		img_wall = pygame.image.load('ressources/One-tiles-20x20-Big.png').convert()
		img_keeper = pygame.image.load('ressources/Gardien-Big.png').convert_alpha()
		img_door_hor = pygame.image.load('ressources/door_ver-Big.png').convert_alpha()
		img_door_ver = pygame.image.load('ressources/door_hor-Big.png').convert_alpha()

		for cle, str_map in self.maze_map[0].items():
			if str_map != "O":
				screen.blit(img_floor,cle)
			elif str_map == "O":
				screen.blit(img_wall,cle)
			if str_map == "E":
				screen.blit(img_keeper,cle)
			if str_map == ".":
				screen.blit(img_door_hor,cle)
			if str_map == ",":
				screen.blit(img_door_ver,cle)


def creating_dictionary(liste_map):
	#Constants
	img_size = 40
	origin_leftpos = 10
	origin_toppos = 5 
	#Variable
	ligne_liste = 1
	col_liste = 0
	dict_map = {}
	dict_floor = {}
	liste_cle = {}
	max_x = None
	max_y = None
	x = 0

	for i, enu_liste in enumerate(liste_map):
		col_liste += 1

		if enu_liste == "\n":
			col_liste = 0
			ligne_liste +=1

		pos_ligne = ligne_liste*img_size + origin_leftpos
		pos_col = col_liste*img_size + origin_toppos

		if 	enu_liste != "\n":
			dict_map[pos_col,pos_ligne] = enu_liste
			if enu_liste == " ":
				dict_floor[pos_col,pos_ligne] = enu_liste

	for k in dict_map.keys():
		if k[0] > 1:
			if max_x is None or k[0] > max_x:
				max_x = k[0]
		if k[1] > 1:
			if max_y is None or k[1] > max_y:
				max_y = k[1]

	while len(liste_cle) < 4:
		random_item = random.choice(list(dict_floor.keys()))
		select_choice = random_item in liste_cle.keys()
		while select_choice == True:
			random_item = random.choice(dict_floor.keys())
			select_choice = random_item in liste_cle.keys()
		liste_cle[random_item] = str(x)
		x += 1	

	return [dict_map,liste_cle,max_x,max_y]




	