# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.
Ce sera lui qu'on lancera pour charger le jeu.
This file contains the main code of the game.
It will be him that we launch to load the game.
"""

import sys
import os
import pygame
from pygame.locals import *
from module_actions import *
from Class_Maze import *
from Class_Items import *
from Class_Personnage import *
from copy import copy, deepcopy

def main():
	#Constants
	display_width = 650
	display_height = 680
	display_size = (display_width, display_height)
	img_size = 40
	token_win = None
	#Initialization
	pygame.init()
	screen = pygame.display.set_mode(display_size)
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
	maze_init = Maze() #initialisation labyrinthe
	item_init = Item(maze_init.listing_item,maze_init.maze_map) #Initialisation items
	maze_init.creating_map(screen) #Création de la map
	item_init.creating_item(screen,item_search) # Création de la liste d'item à chercher
	macgyver = Personnage(maze_init.maze_map,"ressources/MacGyver-big.png", img_size) #Intialisation du personnage
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
		item_init.keep_item(item_search, macgyver.rect) #On vérifie que le personnage ne récupère pas l'item / We check that the character does not recover the item
		screen.blit(background,(0,0))#on met à jour l'affichage / Display update
		item_init.inventory(screen,item_search,img_size)#On met à jour l'inventaire / Inventory update
		maze_init.creating_map(screen)#On met à jour le labyrinthe / Maze update
		item_init.creating_item(screen,item_search)#mise à jour des items / Items update
		macgyver.draw(screen)#Affichage du personnage / charactere display
		pygame.display.update()#Mise à jour de l'affichage / display update

		token_win = macgyver.game_over(item_search,token_win,screen)#Vérification si partie gagné ou perdu / check if the game is won or lost
		pygame.display.update()#Mise à jour de l'affichage / Display update

		if token_win != None:
			return #fin du programme / End prog

if __name__=='__main__' : main()

