# -*-coding:Utf-8 -*

#Fichier contenant la class item, cette dernière permet de gérer l'initialisation des items, leur ramassage et leur intentaire.

import sys
import os
import pygame
from pygame.locals import * 
from module_actions import *
from Class_Maze import *
from Class_Personnage import *

class Item:
	#Classe gérant les items à ramasser

	def __init__(self,listing_item,dictionary_map):
		self.dictionary = dictionary_map
		self.listing_item = listing_item
		self.ligne_max = dictionary_map[3]
	def creating_item(self,screen,liste_item):
		self.item_ether = pygame.image.load('ressources/ether-little.png').convert_alpha()
		self.item_aiguille = pygame.image.load('ressources/aiguille-little.png').convert_alpha()
		self.item_plastic = pygame.image.load('ressources/tube_plastique-little.png').convert_alpha()
		self.item_seringue = pygame.image.load('ressources/seringue-little.png').convert_alpha()

		for cle, str_map in self.listing_item.items():
			var_false = cle in liste_item.keys()
			if str_map == "0" and var_false == False :
				screen.blit(self.item_ether,cle)
			elif str_map == "1" and var_false == False:
				screen.blit(self.item_aiguille,cle)
			elif str_map == "2"and var_false == False:
				screen.blit(self.item_plastic,cle)
			elif str_map == "3"and var_false == False:
				screen.blit(self.item_seringue,cle)

	def keep_item(self,item_search,token_pos):
		pos_x = token_pos.x
		pos_y = token_pos.y
		var_pos = (pos_x,pos_y)
		var_pos_true_liste = var_pos in self.listing_item.keys()
		var_pos_false_search = var_pos in item_search.keys()
		if var_pos_true_liste == True and var_pos_false_search == False:
			item_search[var_pos] = self.listing_item[var_pos]

	def inventory(self,screen,item_search,img_size): 
		tuple_pos = (img_size,self.ligne_max+img_size)
		font = pygame.font.Font(None,36)
		text = font.render("Inventaire",1,(10,10,10))
		screen.blit(text,tuple_pos)	
		nw_item = 0
		pos_item = img_size*2
		for cle,str_map in item_search.items():
			var_false = cle in item_search.keys()
			item_pos = (img_size+nw_item,self.ligne_max+pos_item)
			if str_map == "0" and var_false == True :
				screen.blit(self.item_ether,item_pos)
				nw_item += img_size
			elif str_map == "1" and var_false == True:
				screen.blit(self.item_aiguille,item_pos)
				nw_item += img_size
			elif str_map == "2"and var_false == True:
				screen.blit(self.item_plastic,item_pos)
				nw_item += img_size
			elif str_map == "3"and var_false == True:
				screen.blit(self.item_seringue,item_pos)
				nw_item += img_size
