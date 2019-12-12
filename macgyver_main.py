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

print("C'est le jeu")

def main():
	#Initialization
	pygame.init()
	screen = pygame.display.set_mode((650,680))
	pygame.display.set_caption('MacGyver')

	#Fond de l'écran chargé / Background of the loaded screen
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250,250,250))
	# On charge les cartes existantes / We load the existing cards
	cartes = []
	for nom_fichier in os.listdir("cartes"):
		if nom_fichier.endswith(".txt"):
			chemin = os.path.join("cartes", nom_fichier)
			nom_carte = nom_fichier[:-4].lower() #Passer de -3 à -4 pour retirer le point
			with open(chemin, "r") as fichier:
				contenu = fichier.read()
				Carte_Save = Carte(nom_carte, contenu)
				if not(cartes):
					cartes = [Carte_Save]
				else:
					cartes.append(Carte_Save)
	item_search = 0
	# On positionne le titre / set up the title
	font = pygame.font.Font(None,36)
	text = font.render("Partez à l'aventure avec MacGyver",1,(10,10,10))
	text_pos = text.get_rect()
	text_pos.centerx = background.get_rect().centerx
	background.blit(text,text_pos)
	#Création de la map / creation of the map
	map_select = cartes[0].labyrinthe
	map_lvl = nw_map(background,map_select,item_search)
	#Afficher sur l'écran / Show on screen
	screen.blit(background,(0,0))
	pygame.display.flip()
	#Boucle du programme / Loop of the program
	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
		screen.blit(map_lvl[0],(0,0))
		screen.blit(map_lvl[0],(0,0))
		pygame.display.flip()

if __name__=='__main__' : main()

