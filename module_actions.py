# -*-coding:Utf-8 -*

"""Ce fichier contient les différentes actions du jeu
"""

import sys
import os
import pygame
from pygame.locals import *
import random


#Ramène la position de macgyver / Give a position of Macgyver
def pos_token(dict_map,symbol):
	for cle,valeur in dict_map.items():
		if valeur == symbol:
			pos_character = cle
			break
	return pos_character
#Dépose aléatoirement un item
def rand_item(liste_cle):
	int_cle = random.randint(0,3)
	val_in = True
	while val_in == True:
		int_cle = random.randint(0,3)
		int_cle = str(int_cle)
		val_in = int_cle in liste_cle.values()

	return int_cle

def liste_item(map_select):
	down_item = []
	for i, item_liste in enumerate(map_select):
		if item_liste.isdecimal() == True:
			down_item.append(item_liste)
	return down_item



