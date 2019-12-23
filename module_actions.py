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

def liste_item(map_select):
	down_item = []
	for i, item_liste in enumerate(map_select):
		if item_liste.isdecimal() == True:
			down_item.append(item_liste)
	return down_item



