import pygame as pg
import random
import os
from settings import *
vec = pg.math.Vector2

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
        self.rect.y -= 3
        if self.rect.bottom < 0:
            self.game.lives -=1
            self.kill()
        for event in self.game.events_list:
            if event.type == pg.KEYDOWN:
                if event.key==pg.K_UP:
                    if self.dir =="up":
                        if pg.sprite.spritecollide(self,self.game.lines,False):
                            self.game.score += 10
                            self.game.draw_text("Good Job!!!", random.randint(20, 50), BLACK, WIDTH * 1 / 5, HEIGHT/2)
                            print("whoo")
                            self.kill()
                        else:
                            self.game.score -=10
                            self.game.lives -=1
                elif event.key ==pg.K_DOWN:
                    if self.dir =="down":
                        if pg.sprite.spritecollide(self,self.game.lines,False):
                            self.game.score += 10
                            self.game.draw_text("Way too go!!!", random.randint(20, 50), BLACK, WIDTH * 1 / 5, 30)
                            self.kill()
                        else:
                            self.game.score -=10
                            self.game.lives -= 1
                elif event.key==pg.K_LEFT:
                    if self.dir =="left":
                        if pg.sprite.spritecollide(self,self.game.lines,False):
                            self.game.score += 10
                            self.game.draw_text("Keep going!!!", random.randint(20, 50), BLACK, WIDTH * 1 / 5, 30)
                            self.kill()
                        else:
                            self.game.score -=10
                            self.game.lives -= 1
                elif event.key==pg.K_RIGHT:
                    if self.dir =="right":
                        if pg.sprite.spritecollide(self,self.game.lines,False):
                            self.game.score += 10
                            self.game.draw_text("Good skills!!!", random.randint(20, 50), BLACK, WIDTH * 1 / 5, 30)
                            self.kill()
                        else:
                            self.game.score -=10
                            self.game.lives -= 1



class Line(pg.sprite.Sprite):
    def __init__(self,game):
        self._layer = LINE_LAYER
        self.groups = game.all_sprites, game.lines
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = pg.surface.Surface((WIDTH,5))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT*1/8)

def Arrow_spawn(game,i):

    for line in game.file:
        game.command.append(line.strip())
    if game.command[i] == "left":
        Arrow(game, WIDTH * 1 / 5, HEIGHT - 25, game.left_arrow_img,"left")

    elif game.command[i] == "down":
        Arrow(game, WIDTH * 2 / 5, HEIGHT - 25,game.down_arrow_img,"down")

    elif game.command[i] == "up":
        Arrow(game, WIDTH * 3 / 5, HEIGHT - 25, game.up_arrow_img,"up")

    elif game.command[i] == "right":
        Arrow(game, WIDTH * 4 / 5, HEIGHT - 25, game.right_arrow_img,"right")
    game.num_of_arrows+= 1
    if game.num_of_arrows> len(game.command)-1:
        game.num_of_arrows= 0
        game.run_update +=1
        if game.run_update >= 5:
            game.draw_text("speed up",50,BLACK,WIDTH/2,HEIGHT/2)
            game.delay *= 0.75
            game.run_update = 0
