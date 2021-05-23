import pygame as pg
import random
import os

HEIGHT = 480
WIDTH = 480
FPS = 60
title = "Arrows"
FONT_NAME = "arial"
HS_FILE = "highscore.txt"



#layers
ARROW_LAYER = 2
PLAYER_LAYER = 1

#arrow choice
ARROW_CHOICE =["right","left","down"]


#images
UP_ARROW_IMG = "up_arrow.png"
LEFT_ARROW_IMG = "left_arrow.png"
RIGHT_ARROW_IMG = "right_arrow.png"
DOWN_ARROW_IMG = "down_arrow.png"


# colors (R,G,B)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN =(0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
VIOLET = (238,130,238)
SEAGREEN = (78,238,148)
ROYALBLUE=(65,105,225)
CORNFLOWER = (100,149,237)
GOLD= (255,215,0)
FIREBRICK = (178,34,34)
FORESTGREEN = (34,139,34)


BGCOLOR = CORNFLOWER