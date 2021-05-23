import pygame as pg
import random
import os
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self,game):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites,game.arrows
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = game.player_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT-37)
        self.dir = "right"
        self.lives = 5

    def update(self):
        for event in self.game.events_list:
            if event.type == pg.KEYDOWN:
                if event.key==pg.K_UP:
                    self.dir = "up"
                elif event.key == pg.K_LEFT:
                    self.dir = "left"
                elif event.key == pg.K_RIGHT:
                    self.dir = "right"
        Hand(self.game, self.rect.centerx, self.rect.centery, self.dir)
        if pg.sprite.spritecollide(self, self.game.arrows, False):
            self.lives -= 1

class Hand(pg.sprite.Sprite):
    def __init__(self, game,x,y,dir):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.hand_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.offsetx = self.check_dir(dir)
        self.offsety = self.check_diry(dir)
        self.rect.center = (x-self.offsetx, y + self.offsety)


    def check_dir(self,dir):
        if dir == "up":
            return 0
        elif dir == "left":
            return 35
        else:
            return -35

    def check_diry(self,dir):
        if dir == "up":
            return -40
        elif dir == "left":
            return 10
        else:
            return 10
    def update(self):
        pg.sprite.spritecollide(self, self.game.arrows, False)



class Arrow(pg.sprite.Sprite):
    def __init__(self,game,x,y,img,dir):
        self._layer = ARROW_LAYER
        self.groups = game.all_sprites,game.arrows
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.dir = dir

    def update(self):
        if self.dir =="left":
            self.rect.x-=5
        if self.dir =="right":
            self.rect.x+=5
        if self.dir =="down":
            self.rect.y+=5

def Attack(game,arrow):
    if arrow == "left":
        Arrow(game,WIDTH, HEIGHT - 30, game.left_arrow_img, "left")
    elif arrow == "down":
        Arrow(game, WIDTH/2, 0, game.down_arrow_img, "down")
    elif arrow == "right":
        Arrow(game, 0, HEIGHT - 30, game.right_arrow_img, "right")


