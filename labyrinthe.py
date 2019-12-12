# -*-coding:Utf-8 -*

"""Ce fichier contient le module qui ramène le labyrinthe
"""

import sys
import os
from module_actions import *
import pygame
from pygame.locals import *

def lab_txt(cible):#Permet de lire le fichier carte puis de ramener les informations
	string = list(cible)
	return string

def nw_map(back_map, list_map, inv_num): #génère une map

	background = back_map

	x = 0
	y = 0
	z = 0

	for img_lab in list_map:
		ind_left = 40 * x
		ind_top = 40 * y
		save_pos_left = 20 + ind_left
		save_pos_top = 50 + ind_top

		if img_lab == "O":
			wall = pygame.image.load('ressources/One-tiles-20x20-Big.png').convert()
			background.blit(wall,(save_pos_left,save_pos_top))
		elif img_lab == " ":
			floor = pygame.image.load('ressources/One-tiles-20x20-Floor-Big.png').convert()
			background.blit(floor,(save_pos_left,save_pos_top))
		elif img_lab == ".":
			floor = pygame.image.load('ressources/One-tiles-20x20-Floor-Big.png').convert()
			background.blit(floor,(save_pos_left,save_pos_top))
			door = pygame.image.load('ressources/door_ver-Big.png').convert_alpha()
			background.blit(door,(save_pos_left,save_pos_top))	
		elif img_lab == "X":
			floor = pygame.image.load('ressources/One-tiles-20x20-Floor-Big.png').convert()
			background.blit(floor,(save_pos_left,save_pos_top))
			mac_img = pygame.image.load('ressources/MacGyver-Big.png').convert_alpha()
			background.blit(mac_img,(save_pos_left,save_pos_top))
		elif img_lab == "E":
			floor = pygame.image.load('ressources/One-tiles-20x20-Floor-Big.png').convert()
			background.blit(floor,(save_pos_left,save_pos_top))
			keeper_img = pygame.image.load('ressources/Gardien-Big.png').convert_alpha()
			background.blit(keeper_img,(save_pos_left,save_pos_top))
		elif img_lab == ",":
			floor = pygame.image.load('ressources/One-tiles-20x20-Floor-Big.png').convert()
			background.blit(floor,(save_pos_left,save_pos_top))
			door = pygame.image.load('ressources/door_hor-Big.png').convert_alpha()
			background.blit(door,(save_pos_left,save_pos_top))
		elif img_lab == "I":
			if z == 0:
				item = pygame.image.load('ressources/').convert_alpha()
			elif z == 1:
				item = pygame.image.load('ressources/').convert_alpha()
			elif z == 2:
				item = pygame.image.load('ressources/').convert_alpha()
			elif z == 3:
				item = pygame.image.load('ressources/').convert_alpha()


		x += 1

		if img_lab == "\n":
			x = 0
			y += 1

	print(y)
	#position de l'inventaire / Inventory position
	inv_pos_top = save_pos_top + 40
	inv_pos_left = 40
	font = pygame.font.Font(None,36)
	text = font.render("Inventaire",1,(10,10,10))
	background.blit(text,(40,inv_pos_top))	
	#Création de l'équipement / equipement creation
	inv_form = inv_mod(background,inv_pos_top,inv_pos_left,inv_num)
	return [background,inv_form]
	
