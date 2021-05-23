import pygame as pg
import random
import os

#set up folder assets
#game_folder = os.path.dirname(__file__)
#img_folder = os.join(game_folder,"img")
#sound_folder = os.join(game_folder,"snd")


HEIGHT = 600
WIDTH = 480
FPS = 60
title = "Jumpy"
FONT_NAME = "arial"
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"


# player propertys
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAY_GRAV = 0.8
PLAYER_JUMP = 20

# Game propertieties
BOOST_POWER = 60
POW_SPAWN_PCT = 7
MOB_FREQ = 5000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0


# Starting platforms
PLATFORM_LIST = [(0,HEIGHT-60),
                 (WIDTH/2 - 50, HEIGHT * 3/4 - 50),
                 (125,HEIGHT-350),
                 (350,200),
                 (175,100)]

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
colors= [BLACK,WHITE,RED,GREEN,BLUE,YELLOW,VIOLET,SEAGREEN,ROYALBLUE,CORNFLOWER,GOLD,FIREBRICK,FORESTGREEN]

