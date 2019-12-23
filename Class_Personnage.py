# -*-coding:Utf-8 -*

"""permet de ramener les informations de la carte
"""

import sys
import os
import pygame
from pygame.locals import * 
from module_actions import *
from Class_Maze import *
from Class_Items import *

class Personnage:

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

		self.max = [dict_lvl[2],dict_lvl[3]] #max_lenght(self.entire_map)

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



