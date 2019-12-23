# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.
Ce sera lui qu'on lancera pour charger le jeu.
"""

import sys
import os
import pygame
from pygame.locals import *
from module_actions import *
from labyrinthe import *
from cartes import *
from copy import copy, deepcopy

def main():
	#Constants
	DISPLAY_WIDTH = 650
	DISPLAY_HEIGHT = 680
	DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
	img_size = 40
	token_win = None
	#Initialization
	pygame.init()
	screen = pygame.display.set_mode(DISPLAY_SIZE)
	pygame.display.set_caption('MacGyver') #Windows name
	#Fond de l'écran chargé / Background of the loaded screen
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250,250,250))
	item_search = {} #Liste des items à chercher
	# On positionne le titre / set up the title
	font = pygame.font.Font(None,36)
	text = font.render("Partez à l'aventure avec MacGyver",1,(10,10,10))
	text_pos = text.get_rect()
	text_pos.centerx = background.get_rect().centerx
	background.blit(text,text_pos)
	#Création de la map / creation of the map
	maze_init = maze() #initialisation labyrinthe
	item_init = item(maze_init.listing_item,maze_init.maze_map) #Initialisation items
	maze_init.creating_map(screen) #Création de la map
	item_init.creating_item(screen,item_search) # Création de la liste d'item à chercher
	macgyver = personnage(maze_init.maze_map,"ressources/MacGyver-big.png", img_size) #Intialisation du personnage
	#Afficher sur l'écran / Show on screen
	screen.blit(background,(0,0))
	pygame.display.flip()
	#Boucle du programme / Loop of the program
	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					return
			macgyver.keys_event(event) # On récupère les events / we keep the event
		macgyver.moving() # mise à jour de la position / update
		item_init.keep_item(item_search, macgyver.rect) #On vérifie que le personnage ne récupère pas l'item
		screen.blit(background,(0,0))#on met à jour l'affichage
		item_init.inventory(screen,item_search,item_init.inventory_max_pos(),img_size)#On met à jour l'inventaire 
		maze_init.creating_map(screen)#On met à jour le labyrinthe
		item_init.creating_item(screen,item_search)#mise à jour des items
		macgyver.draw(screen)#Affichage du personnage
		pygame.display.update()#Mise à jour de l'affichage

		token_win = macgyver.game_over(item_search,token_win,screen)#Vérification si partie gagné ou perdu
		pygame.display.update()#Mise à jour de l'affichage

		if token_win != None:
			return #fin du programme

if __name__=='__main__' : main()

