import pygame as pg
import random
import os
from settings import *
vec = pg.math.Vector2
class Board(pg.sprite.Sprite):
    def __init__(self,game,posx,posy):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = pg.Surface((WIDTH*1/3-20,HEIGHT*1/3-20))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx =posx
        self.rect.centery =posy
        self.lives = 5
        self.has_been_clicked = False
        self.player_claimed = ""