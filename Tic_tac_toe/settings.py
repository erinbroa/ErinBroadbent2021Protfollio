import pygame as pg
import random
import os

HEIGHT = 480
WIDTH = 480
FPS = 60
title = "TIC TAC TOE"
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

# Box numbers
BOX_1x = WIDTH*1/6
BOX_1y = HEIGHT*1/6
BOX_2x = WIDTH*3/6
BOX_2y = HEIGHT*1/6
BOX_3x = WIDTH*5/6
BOX_3y = HEIGHT*1/6

BOX_4x = WIDTH*1/6
BOX_4y = HEIGHT*3/6
BOX_5x = WIDTH*3/6
BOX_5y = HEIGHT*3/6
BOX_6x = WIDTH*5/6
BOX_6y= HEIGHT*3/6

BOX_7x = WIDTH*1/6
BOX_7y = HEIGHT*5/6
BOX_8x = WIDTH*3/6
BOX_8y = HEIGHT*5/6
BOX_9x = WIDTH*5/6
BOX_9y = HEIGHT*5/6
