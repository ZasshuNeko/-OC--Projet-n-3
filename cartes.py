# -*-coding:Utf-8 -*

"""permet de ramener les informations de la carte
"""

import sys
import os
from labyrinthe import *


class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = lab_txt(chaine)#Module qui ramène la chaine de carractère de la carte

    def __repr__(self):
        return "<Carte {}>".format(self.nom)
