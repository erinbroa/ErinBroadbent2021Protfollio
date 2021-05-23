import pygame as pg
import random
from os import path
from settings import *
from sprites import *


class Game(object):

    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()
        self.last_arrow = 0
        self.delay = 1000
        self.num_of_arrows = 0
        self.lives = 5



    def load_data(self):
        #load high score
        game_folder = path.dirname(__file__)
        image_folder = path.join(game_folder, "imgs")
        with open(path.join(game_folder,HS_FILE),"r") as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        self.left_arrow_img = pg.image.load(path.join(image_folder,LEFT_ARROW_IMG)).convert_alpha()
        self.right_arrow_img = pg.image.load(path.join(image_folder, RIGHT_ARROW_IMG)).convert_alpha()
        self.up_arrow_img = pg.image.load(path.join(image_folder, UP_ARROW_IMG)).convert_alpha()
        self.down_arrow_img = pg.image.load(path.join(image_folder,DOWN_ARROW_IMG)).convert_alpha()
        self.player_img =pg.image.load(path.join(image_folder,"dave.png")).convert_alpha()
        self.hand_img = pg.image.load(path.join(image_folder, "hand.png")).convert_alpha()


    def new(self):
        #start a new game
        #create sprite groups
        self.score = 0
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.arrows = pg.sprite.Group()
        self.player = Player(self)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        self.events_list =  pg.event.get()
        for event in self.events_list:
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False


    def update(self):
        now = pg.time.get_ticks()
        self.all_sprites.update()
        if now - self.last_arrow > self.delay:
            self.last_arrow = now
            Attack(self,random.choice(ARROW_CHOICE))
        if self.lives <= 0:
            self.running = False



    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score),22,WHITE,WIDTH/2,15)
        self.draw_text(str(self.lives), 22,WHITE,WIDTH/4*5, 15)
        pg.display.flip()

    def show_start_screen(self):
        self.screen.fill(BGCOLOR)
        self.draw_text(title, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Press the arrow key to block the attack", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        self.draw_text("highscore:" + str(self.highscore), 22, WHITE, WIDTH / 2, 15)
        pg.display.flip()
        self.wait_for_key()

    def show_GO_screen(self):
        if not self.running:
            return
        self.screen.fill(BGCOLOR)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score:" + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH SCORE!", 22, WHITE, WIDTH / 2, HEIGHT /2+40)
            with open(path.join(self.dir,HS_FILE),"w")as f:
                f.write(str(self.score))
        else:
            self.draw_text("highscore:" + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT /2+40)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self,text,size,color,x,y):
        font = pg.font.Font(self.font_name,size)
        text_surface = font.render(text,True,color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface,text_rect)

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_GO_screen()

pg.quit()