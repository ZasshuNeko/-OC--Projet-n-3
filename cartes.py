# -*-coding:Utf-8 -*

"""permet de ramener les informations de la carte
"""

import sys
import os
import pygame
from pygame.locals import * 
from module_actions import *
from labyrinthe import *

class item:
	#Classe gérant les items à ramasser

	def __init__(self,grp_item,dict_lvl):
		self.dictionary = dict_lvl
		self.listing = grp_item
	def creating_item(self,screen,liste_item):
		self.item_ether = pygame.image.load('ressources/ether-little.png').convert_alpha()
		self.item_aiguille = pygame.image.load('ressources/aiguille-little.png').convert_alpha()
		self.item_plastic = pygame.image.load('ressources/tube_plastique-little.png').convert_alpha()
		self.item_seringue = pygame.image.load('ressources/seringue-little.png').convert_alpha()

		for cle, str_map in self.listing.items():
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
		var_pos_true_liste = var_pos in self.listing.keys()
		var_pos_false_search = var_pos in item_search.keys()
		if var_pos_true_liste == True and var_pos_false_search == False:
			item_search[var_pos] = self.listing[var_pos]

	def inventory(self,screen,item_search,pos_max,img_size): 
		tuple_pos = (img_size,pos_max+img_size)
		font = pygame.font.Font(None,36)
		text = font.render("Inventaire",1,(10,10,10))
		screen.blit(text,tuple_pos)	
		nw_item = 0
		pos_item = img_size*2
		for cle,str_map in item_search.items():
			var_false = cle in item_search.keys()
			item_pos = (img_size+nw_item,pos_max+pos_item)
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

	def inventory_max_pos(self):
		maxi = None
		for k in self.dictionary[0].keys():
			if k[1] > 1:
				if maxi is None or k[1] > maxi:
					maxi = k[1]
		return maxi


class personnage:

	#Classe personnage

	def __init__(self,dict_lvl,filename,img_size):
		self.symbol = "X"
		self.pos = pos_token(dict_lvl[0],self.symbol)
		self.entire_map = dict_lvl[0]
		self.image = pygame.image.load(filename).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = self.pos[0]
		self.rect.y = self.pos[1]
		self.pos_x = self.rect.x
		self.pos_y = self.rect.y
		self.img_size = img_size

		self.max = max_lenght(self.entire_map)

		self.moving_left = False
		self.moving_right = False
		self.moving_up = False
		self.moving_down = False

	def moving(self):
		if self.moving_left:
			self.pos_x -= self.img_size
			self.moving_left = False
		if self.moving_right:
			self.pos_x += self.img_size
			self.moving_right = False
		if self.moving_up:
			self.pos_y -= self.img_size
			self.moving_up = False
		if self.moving_down:
			self.pos_y += self.img_size
			self.moving_down = False
	def keys_event(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				self.moving_left = True
			elif event.key == pygame.K_RIGHT:
				self.moving_right = True
			elif event.key == pygame.K_UP:
				self.moving_up = True
			elif event.key == pygame.K_DOWN:
				self.moving_down = True

	def draw(self,screen):
		if self.pos_x <= self.max[0] and self.pos_y <= self.max[1] :
			cle_test = (self.pos_x,self.pos_y)
			if self.entire_map[cle_test] != "O":
				self.rect.x = self.pos_x
				self.rect.y = self.pos_y
				screen.blit(self.image,self.rect)
			else:
				sound = pygame.mixer.Sound("ressources/chute-3-SF.ogg")
				sound.play()
				self.pos_x = self.rect.x
				self.pos_y = self.rect.y
				screen.blit(self.image,self.rect)
		else:
			self.pos_x = self.rect.x
			self.pos_y = self.rect.y
			screen.blit(self.image,self.rect)


	def game_over(self,item_search,token_win,screen):
		var_cle = (self.rect.x,self.rect.y)
		if len(item_search) == 4 and self.entire_map[var_cle] == "E":
			token_win = True
			win = pygame.image.load('ressources/win.png').convert()
			screen.blit(win,(0,0))
		elif len(item_search) < 4 and self.entire_map[var_cle] == "E":
			token_win = False
			win = pygame.image.load('ressources/lose.png').convert()
			screen.blit(win,(0,0))
		return token_win

def max_lenght(entire_map):
	max_x = None
	max_y = None
	for k in entire_map.keys():
		if k[0] > 1:
			if max_x is None or k[0] > max_x:
				max_x = k[0]
		if k[1] > 1:
			if max_y is None or k[1] > max_y:
				max_y = k[1]
	return [max_x,max_y]


class maze:
	#définis la classe du niveau mettre des attributs utilisable
	def __init__(self):

		self.maze_map = take_maze() # dictionnaire contenant le niveau / dictionary containing the level
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


def crea_dict(liste_map):
	#Constants
	img_size = 40
	origin_leftpos = 10
	origin_toppos = 5 
	#Variable
	ligne_liste = 1
	col_liste = 0
	dict_map = {}
	liste_cle = {}

	for i, enu_liste in enumerate(liste_map):
		col_liste += 1

		if enu_liste == "\n":
			col_liste = 0
			ligne_liste +=1

		pos_ligne = ligne_liste*img_size + origin_leftpos
		pos_col = col_liste*img_size + origin_toppos

		if enu_liste == "I":
			val_item = rand_item(liste_cle)
			#liste_cle.append(val_item)
			liste_map[i] = str(val_item)
			enu_liste = str(val_item)
			liste_cle[pos_col,pos_ligne] = enu_liste

		if 	enu_liste != "\n":
			dict_map[pos_col,pos_ligne] = enu_liste
			

	return [dict_map,liste_cle]


class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = list(chaine)#Module qui ramène la chaine de carractère de la carte

    def __repr__(self):
        return "<Carte {}>".format(self.nom)

def take_maze():
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
	map_select = cartes[0].labyrinthe
	map_dict = crea_dict(map_select)
	return map_dict
	
