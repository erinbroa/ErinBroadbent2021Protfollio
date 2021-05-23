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
        self.mousex,self.mousey = pg.mouse.get_pos()
        self.player_color = (YELLOW)
        self.player2_color = (GREEN)
        self.player1_turn = True
        self.winner = ""

    def load_data(self):
        #load high score
        game_folder = path.dirname(__file__)
        image_folder = path.join(game_folder, "imgs")

    def new(self):
        #start a new game
        #create sprite groups
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.board1 = Board(self,BOX_1x,BOX_1y)
        self.board3 =Board(self, BOX_3x, BOX_3y)
        self.board2 =Board(self, BOX_2x, BOX_2y)
        self.board4 =Board(self, BOX_4x, BOX_4y)
        self.board5 =Board(self, BOX_5x, BOX_5y)
        self.board6 =Board(self, BOX_6x, BOX_6y)
        self.board7 =Board(self, BOX_7x, BOX_7y)
        self.board8 =Board(self, BOX_8x, BOX_8y)
        self.board9 =Board(self, BOX_9x, BOX_9y)

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
            if event.type == pg.MOUSEBUTTONDOWN and self.board1.rect.collidepoint(pg.mouse.get_pos()):
                if self.board1.has_been_clicked == False:
                    if self.player1_turn:
                        self.board1.image.fill(self.player_color)
                        self.player1_turn = False
                        self.board1.has_been_clicked = True
                        self.board1.player_claimed = "Player 1"
                    else:
                        self.board1.image.fill(self.player2_color)
                        self.player1_turn = True
                        self.board1.has_been_clicked = True
                        self.board1.player_claimed = "Player 2"
            if event.type == pg.MOUSEBUTTONDOWN and self.board2.rect.collidepoint(pg.mouse.get_pos()):
                if self.board2.has_been_clicked == False:
                    if self.player1_turn:
                        self.board2.image.fill(self.player_color)
                        self.player1_turn = False
                        self.board2.has_been_clicked = True
                        self.board2.player_claimed = "Player 1"
                    else:
                        self.board2.image.fill(self.player2_color)
                        self.player1_turn = True
                        self.board2.has_been_clicked = True
                        self.board2.player_claimed = "Player 2"
            if event.type == pg.MOUSEBUTTONDOWN and self.board3.rect.collidepoint(pg.mouse.get_pos()):
                if self.board3.has_been_clicked == False:
                    if self.player1_turn:
                        self.board3.image.fill(self.player_color)
                        self.player1_turn = False
                        self.board3.has_been_clicked = True
                        self.board3.player_claimed = "Player 1"
                    else:
                        self.board3.image.fill(self.player2_color)
                        self.player1_turn = True
                        self.board3.has_been_clicked = True
                        self.board3.player_claimed = "Player 2"
            if event.type == pg.MOUSEBUTTONDOWN and self.board4.rect.collidepoint(pg.mouse.get_pos()):
                if self.board4.has_been_clicked == False:
                    if self.player1_turn:
                        self.board4.image.fill(self.player_color)
                        self.player1_turn = False
                        self.board4.has_been_clicked = True
                        self.board4.player_claimed = "Player 1"
                    else:
                        self.board4.image.fill(self.player2_color)
                        self.player1_turn = True
                        self.board4.has_been_clicked = True
                        self.board4.player_claimed = "Player 2"
            if event.type == pg.MOUSEBUTTONDOWN and self.board5.rect.collidepoint(pg.mouse.get_pos()):
                if self.board5.has_been_clicked == False:
                    if self.player1_turn:
                        self.board5.image.fill(self.player_color)
                        self.player1_turn = False
                        self.board5.has_been_clicked = True
                        self.board5.player_claimed = "Player 1"
                    else:
                        self.board5.image.fill(self.player2_color)
                        self.player1_turn = True
                        self.board5.has_been_clicked = True
                        self.board5.player_claimed = "Player 2"
            if event.type == pg.MOUSEBUTTONDOWN and self.board6.rect.collidepoint(pg.mouse.get_pos()):
                if self.board6.has_been_clicked == False:
                    if self.player1_turn:
                        self.board6.image.fill(self.player_color)
                        self.player1_turn = False
                        self.board6.has_been_clicked = True
                        self.board6.player_claimed = "Player 1"
                    else:
                        self.board6.image.fill(self.player2_color)
                        self.player1_turn = True
                        self.board6.has_been_clicked = True
                        self.board6.player_claimed = "Player 2"
            if event.type == pg.MOUSEBUTTONDOWN and self.board7.rect.collidepoint(pg.mouse.get_pos()):
                if self.board7.has_been_clicked == False:
                    if self.player1_turn:
                        self.board7.image.fill(self.player_color)
                        self.player1_turn = False
                        self.board7.has_been_clicked = True
                        self.board7.player_claimed = "Player 1"
                    else:
                        self.board7.image.fill(self.player2_color)
                        self.player1_turn = True
                        self.board7.has_been_clicked = True
                        self.board7.player_claimed = "Player 2"
            if event.type == pg.MOUSEBUTTONDOWN and self.board8.rect.collidepoint(pg.mouse.get_pos()):
                if self.board8.has_been_clicked == False:
                    if self.player1_turn:
                        self.board8.image.fill(self.player_color)
                        self.player1_turn = False
                        self.board8.has_been_clicked = True
                        self.board8.player_claimed = "Player 1"
                    else:
                        self.board8.image.fill(self.player2_color)
                        self.player1_turn = True
                        self.board8.has_been_clicked = True
                        self.board8.player_claimed = "Player 2"
            if event.type == pg.MOUSEBUTTONDOWN and self.board9.rect.collidepoint(pg.mouse.get_pos()):
                if self.board9.has_been_clicked == False:
                    if self.player1_turn:
                        self.board9.image.fill(self.player_color)
                        self.player1_turn = False
                        self.board9.has_been_clicked = True
                        self.board9.player_claimed = "Player 1"
                    else:
                        self.board9.image.fill(self.player2_color)
                        self.player1_turn = True
                        self.board9.has_been_clicked = True
                        self.board9.player_claimed = "Player 2"

        if self.board1.player_claimed == "Player 1":
            if self.board2.player_claimed == "Player 1":
                if self.board3.player_claimed == "Player 1":
                    self.playing = False
                    self.winner = "Player 1"
            if self.board4.player_claimed == "Player 1":
                if self.board7.player_claimed == "Player 1":
                    self.playing = False
                    self.winner = "Player 1"
            if self.board5.player_claimed == "Player 1":
                if self.board9.player_claimed == "Player 1":
                    self.playing = False
                    self.winner = "Player 1"
        if self.board7.player_claimed == "Player 1":
            if self.board8.player_claimed == "Player 1":
                if self.board9.player_claimed == "Player 1":
                    self.playing = False
                    self.winner = "Player 1"
            if self.board5.player_claimed == "Player 1":
                if self.board3.player_claimed == "Player 1":
                    self.playing = False
                    self.winner = "Player 1"
        if self.board4.player_claimed == "Player 1":
            if self.board5.player_claimed == "Player 1":
                if self.board6.player_claimed == "Player 1":
                    self.playing = False
                    self.winner = "Player 1"
        if self.board2.player_claimed == "Player 1":
            if self.board5.player_claimed == "Player 1":
                if self.board8.player_claimed == "Player 1":
                    self.playing = False
                    self.winner = "Player 1"
        if self.board3.player_claimed == "Player 1":
            if self.board6.player_claimed == "Player 1":
                if self.board9.player_claimed == "Player 1":
                    self.playing = False
                    self.winner = "Player 1"


        if self.board1.player_claimed == "Player 2":
            if self.board2.player_claimed == "Player 2":
                if self.board3.player_claimed == "Player 2":
                    self.playing = False
                    self.winner = "Player 2"
            if self.board4.player_claimed == "Player 2":
                if self.board7.player_claimed == "Player 2":
                    self.playing = False
                    self.winner = "Player 2"
            if self.board5.player_claimed == "Player 2":
                if self.board9.player_claimed == "Player 2":
                    self.playing = False
                    self.winner = "Player 2"
        if self.board7.player_claimed == "Player 2":
            if self.board8.player_claimed == "Player 2":
                if self.board9.player_claimed == "Player 2":
                    self.playing = False
                    self.winner = "Player 2"
            if self.board5.player_claimed == "Player 2":
                if self.board3.player_claimed == "Player 2":
                    self.playing = False
                    self.winner = "Player 2"
        if self.board4.player_claimed == "Player 2":
            if self.board5.player_claimed == "Player 2":
                if self.board6.player_claimed == "Player 2":
                    self.playing = False
                    self.winner = "Player 2"
        if self.board2.player_claimed == "Player 2":
            if self.board5.player_claimed == "Player 2":
                if self.board8.player_claimed == "Player 2":
                    self.playing = False
                    self.winner = "Player 2"
        if self.board3.player_claimed == "Player 2":
            if self.board6.player_claimed == "Player 2":
                if self.board9.player_claimed == "Player 2":
                    self.playing = False
                    self.winner = "Player 2"
        if self.board1.has_been_clicked:
            if self.board2.has_been_clicked:
                if self.board3.has_been_clicked:
                    if self.board4.has_been_clicked:
                        if self.board5.has_been_clicked:
                            if self.board6.has_been_clicked:
                                if self.board7.has_been_clicked:
                                    if self.board8.has_been_clicked:
                                        if self.board9.has_been_clicked:
                                            self.winner = "No one"



    def update(self):
        now = pg.time.get_ticks()
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        self.screen.fill(BGCOLOR)
        self.draw_text(title, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Player 1 yellow player two green", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def show_GO_screen(self):
        if not self.running:
            return
        self.screen.fill(BGCOLOR)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text(self.winner+" wins", 70, WHITE, WIDTH / 2, HEIGHT * 2 / 4)
        self.draw_text("Press a key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
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


