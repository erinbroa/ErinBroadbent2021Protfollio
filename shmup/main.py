import pygame as pg
import random as r
import math
from os import *


#attribution section
######################################################
#code by:Erin Broadbent
#art work credit "Kenney.nl" or "www.kenney.nl"


######################################################


#folder varibles
######################################################
game_folder = path.dirname(__file__)
imgs_folder = path.join(game_folder,"imgs")
scores_folder = path.join(game_folder,"scores")
snds_folder = path.join(game_folder,"smds")
player_img_folder = path.join(imgs_folder,"playerImgs")
enemy_img_folder = path.join(imgs_folder,"enemyImgs")
background_img_folder = path.join(imgs_folder,"backgroundImgs")
animation_folder = path.join(imgs_folder,"animation")
player_animation_folder = path.join(animation_folder,"player_animation")
npc_animation_folder = path.join(animation_folder,"npc_animation")
power_up_folder = path.join(imgs_folder,"pows")
######################################################

#class object classes
######################################################

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.sheild = 100
        # self.image = pg.Surface((50,40))
        # self.image.fill(GREEN)
        self.image = player_img
        self.image = pg.transform.scale(player_img,(50,38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius =  int(self.rect.width*.85/2)
        #pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = (WIDTH/2)
        self.rect.bottom = (HEIGHT- (HEIGHT*.05))
        self.speedx = 0
        self.shoot_delay = 250
        self.last_shot = pg.time.get_ticks()
        self.last_bomb = pg.time.get_ticks()
        self.lives = 3
        self.hide_timer = pg.time.get_ticks()
        self.hiden = False
        self.power_level = 1
        self.pow_timer = pg.time.get_ticks()
        self.bomb = 3


    def hide(self):
        #hide the player tempolarily
        self.lives -=1
        self.hiden = True
        self.hide_timer = pg.time.get_ticks()
        self.rect.center = (WIDTH/2,HEIGHT +200)


    def update(self):
        if self.power_level >= 2 and pg.time.get_ticks() - self.pow_timer > POWERUP_TIME:
            self.power_level -= 1
            self.pow_timer = pg.time.get_ticks()

        if self.hiden and (pg.time.get_ticks() - self.hide_timer > 3000):
            self.hiden = False
            self.rect.bottom = (HEIGHT- (HEIGHT*.05))
            self.rect.centerx = (WIDTH / 2)
            self.sheild = 100

        self.rect.x += self.speedx
        self.speedx = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
             self.speedx = -5
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.speedx = 5
        if keystate[pg.K_SPACE] and not self.hiden:
            player.shoot()
        if keystate[pg.K_z]:
            player.bomb_timer()


    def bomb_timer(self):
        now = pg.time.get_ticks()
        if now - self.last_bomb > self.shoot_delay:
            self.last_bomb = now
            if self.bomb >0:
                b = Bomb(self.rect.centerx, self.rect.top + 1)
                all_sprites.add(b)
                bullet_group.add(b)
                self.bomb -= 1

    def shoot(self):
        now = pg.time.get_ticks()
        if now - self.last_shot>self.shoot_delay:
            self.last_shot = now
            if self.power_level == 1:
                b = Bullet(self.rect.centerx,self.rect.top+1)
                all_sprites.add(b)
                bullet_group.add(b)
                shoot_snd.play()
            elif self.power_level == 2:
                b1 = Bullet(self.rect.left, self.rect.centery)
                b2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(b1)
                bullet_group.add(b1)
                all_sprites.add(b2)
                bullet_group.add(b2)
                shoot_snd.play()
            elif self.power_level >= 3:
                b = Bullet(self.rect.centerx, self.rect.top + 1)
                b1 = Bullet(self.rect.left, self.rect.centery)
                b1.inc_spreed(-5)
                b2 = Bullet(self.rect.right, self.rect.centery)
                b2.inc_spreed(5)
                all_sprites.add(b)
                bullet_group.add(b)
                all_sprites.add(b1)
                bullet_group.add(b1)
                all_sprites.add(b2)
                bullet_group.add(b2)
                shoot_snd.play()



    def pow_sheild(self,num):
        self.sheild += num
        if self.sheild >= 100:
            self.sheild = 100

    def pow_gun(self):
        self.power_level += 1
        self.pow_timer = pg.time.get_ticks()




class Bullet(pg.sprite.Sprite):
    def __init__(self,x,y):
        super(Bullet, self).__init__()
        # self.image = pg.Surface((5, 10))
        # self.image.fill(BLUE)
        self.image = bullet_img
        self.image = pg.transform.scale(bullet_img, (5, 10))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius =  int(self.rect.width*.75/2)
        #pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = -10
        self.spreed = 0
        self.type = "bullet"

    def inc_spreed(self,num):
        self.spreed = num

    def update(self):
        self.rect.y += self.speed
        self.rect.x+=self.spreed
        # kill bullet when bottom <0
        if self.rect.bottom < 0:
            self.kill()

class Bomb(pg.sprite.Sprite):
    def __init__(self,x,y):
        super(Bomb, self).__init__()
        # self.image = pg.Surface((5, 10))
        # self.image.fill(BLUE)
        self.image = mini_bomb
        self.image = pg.transform.scale(mini_bomb, (10, 20))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius =  int(self.rect.width*.75/2)
        #pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = -10
        self.spreed = 0
        self.type = "bomb"


    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.spreed
        # kill bullet when bottom <0
        if self.rect.bottom < 70:
            self.explosion()

    def explosion(self):
        self.speed = 0
        self.spreed = 0
        expl = Explosion((self.rect.centerx, self.rect.centery), "lg")
        all_sprites.add(expl)
        explo_sprites.add(expl)

class Npc(pg.sprite.Sprite):
    def __init__(self):
        super(Npc,self).__init__()
        # self.image = pg.Surface((25, 25))
        # self.image.fill(RED)
        self.image_orig= r.choice(meteor_images)
        #self.image_orig = pg.transform.scale(self.image_orig, (50, 50))
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width*.75/2)
        #pg.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.rect.centerx = (r.randint(0,WIDTH))
        self.rect.top = (0)
        self.speedy = r.randint( 1,5)
        self.speedx = r.randint( -5,5)
        self.rot = 0
        self.rot_speed = r.randint(-8,8)
        self.last_update = pg.time.get_ticks()

    def rotate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 60:
            self.last_update = now
            # do the rotation
            self.rot = (self.rot+ self.rot_speed)%360
            new_image = pg.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.image_orig.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.center = old_center


    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx



        if self.rect.centery > HEIGHT:
            self.rect.centerx = (r.randint(25, WIDTH-25))
            self.rect.centery = 0
            self.speedx = r.randint(-5,5)

        if self.rect.centerx  > WIDTH:
            self.speedx = -(self.speedx)
        if self.rect.centerx  < 0:
            self.speedx = -(self.speedx)

        if self.rect.centery  < 0:
            self.rect.centery = HEIGHT

    def spawn(self):
        npc = Npc()
        npc_group.add(npc)
        all_sprites.add(npc)



        #if self.times == 10:
            #spw_new_npc(WIDTH/2,0 )

class Star(pg.sprite.Sprite):
    def __init__(self):
        super(Star,self).__init__()
        ran = r.randint(1,5)
        self.image = pg.Surface((ran,ran))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = (r.randint(25, WIDTH - 25))
        self.rect.centery = (r.randint(0, HEIGHT-15))
        self.speedy = r.randint(1, 5)


    def update(self):
        self.rect.centery += self.speedy

        if self.rect.centery > HEIGHT:
            self.rect.centerx = (r.randint(25, WIDTH-25))
            self.rect.centery = 0
            self.speedy = r.randint(1,5)

class Explosion(pg.sprite.Sprite):
    def __init__(self,center,size):
        super(Explosion,self).__init__()
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class Pow(pg.sprite.Sprite):
    def __init__(self,center):
        super(Pow,self).__init__()
        self.type = r.choice(powerUps_chance )
        self.image = pows_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()

#game functions
######################################################
def draw_text(surf,text,size,x,y,color):
    font = pg.font.Font(font_name,size)
    text_surface = font.render(text,True,color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface,text_rect)

def draw_bar(surf,x,y,pct):
    if pct <0:
        pct = 0
    bar_len = 200
    bar_hei = 20
    fill = (pct/100)*bar_len
    outline_rect = pg.Rect(x,y,bar_len,bar_hei )
    fill_rect = pg.Rect(x,y,fill,bar_hei)
    pg.draw.rect(surf,GREEN,fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect,4)

def draw_lives(surf,x,y,num,img):
    for i in range(num):
        img_rect = img.get_rect()
        img_rect.x = x+30*i
        img_rect.y = y
        surf.blit(img,img_rect)

def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen,"Shmup!",64,WIDTH/2,HEIGHT/4,WHITE)
    draw_text(screen, "Arrow keys move, Press space fire", 22, WIDTH / 2, HEIGHT / 2,WHITE)
    draw_text(screen, "Press a key to begin", 18, WIDTH / 2, HEIGHT *3/ 4,WHITE)
    pg.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYUP:
                waiting = False

######################################################
#
# def spw_new_npc(x,y):
#     new_npc = Npc()
#     new_npc.rect.center = (x, y)
#     new_npc.speedx = r.randint(-10, 10)
#     new_npc.speedy = r.randint(0, 10)
#     all_sprites.add(new_npc)
#     npc_group.add(new_npc)

######################################################



#game constants
######################################################
HEIGHT = 900
WIDTH = 600
FPS = 60

# colors (R,G,B)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN =(0,255,0)
BLUE = (0,0,255)

title = "Shmup"
font_name = pg.font.match_font("arial")

powerUps_list = ["sheild","gun","bomb"]
powerUps_chance = ["sheild","sheild","sheild","sheild","sheild","sheild","gun","gun","bomb","bomb"]
POWERUP_TIME = 10000


######################################################

# initialize pygame and create window
######################################################
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()
######################################################

#load images
######################################################
#background img loaded
background = pg.image.load(path.join(background_img_folder,"starfield.png")).convert()
background = pg.transform.scale(background,(WIDTH,HEIGHT))
background_rect = background.get_rect()
#player img loaded
player_img = pg.image.load(path.join(player_img_folder,"playerShip1_orange.png")).convert()

player_mini_img = pg.transform.scale(player_img,(25,19))
player_mini_img.set_colorkey(BLACK)

asteroid_img = pg.image.load(path.join(enemy_img_folder,"metorBrown.png")).convert()
bullet_img = pg.image.load(path.join(player_img_folder,"laserRed16.png")).convert()
#Metor list
meteor_list = []
meteor_list = ["meteorBrown_big1.png", "meteorBrown_big2.png", "meteorBrown_big3.png",
               "meteorBrown_big4.png", "meteorBrown_med1.png", "meteorBrown_med3.png",
               "meteorBrown_small1.png", "meteorBrown_small2.png", "meteorBrown_tiny1.png",
               "meteorBrown_tiny2.png"]
meteor_images = []
for i in meteor_list:
    meteor_images.append(pg.image.load(path.join(enemy_img_folder,i)).convert())

explosion_anim = {}
explosion_anim["lg"] = []
explosion_anim["sm"] = []
explosion_anim["player"] = []
for i in range(9):
    fn = "regularExplosion0{}.png".format(i)
    img = pg.image.load(path.join(npc_animation_folder,fn)).convert()
    img.set_colorkey(BLACK)
    img_lg = pg.transform.scale(img,(100,100))
    img_sm = pg.transform.scale(img, (40, 40))
    explosion_anim["sm"].append(img_sm)
    explosion_anim["lg"].append(img_lg)
    #adding player explosion
    fn = "sonicExplosion0{}.png".format(i)
    img = pg.image.load(path.join(player_animation_folder,fn)).convert()
    img.set_colorkey(BLACK)
    explosion_anim["player"].append(img)

pows_images = {}
for i in range(len(powerUps_list)):
    fn = "img_{}.png".format(i)
    pows_images[powerUps_list[i]] = pg.image.load(path.join(power_up_folder, fn)).convert()
mini_bomb = pg.transform.scale( pows_images["bomb"],(25,19))
mini_bomb.set_colorkey(BLACK)


#####################################################
#load sounds
#####################################################
shoot_snd = pg.mixer.Sound(path.join(snds_folder,"pew.wav"))
expl_sounds = []
for snd in ["expl3.wav","expl6.wav"]:
    expl_sounds.append(pg.mixer.Sound(path.join(snds_folder,snd)))

pg.mixer.music.load(path.join(snds_folder,"tgfcoder-FrozenJam-SeamlessLoop.ogg"))
pg.mixer.music.set_volume(0.4)
pg.mixer.music.play(loops= -1)
#####################################################





#create game loop
############################################################################
#game update varibles
################################
playing = True
game_over = True
score = 0
################################


###############################################
while playing:

    if game_over:

        show_go_screen()

        game_over = False
        # create sprite groups
        ######################################################
        all_sprites = pg.sprite.Group()
        players_group = pg.sprite.Group()
        npc_group = pg.sprite.Group()
        bullet_group = pg.sprite.Group()
        pow_group = pg.sprite.Group()
        explo_sprites = pg.sprite.Group()
        ######################################################
        # create game objects
        ######################################################
        player = Player()
        star = Star()
        for i in range(10):
            npc = Npc()
            npc_group.add(npc)

        for i in range(20):
            star = Star()
            players_group.add(star)
        # bullet = Bullet(HEIGHT,WIDTH/2)
        ######################################################

        # add objects to sprite groups
        ######################################################
        players_group.add(player)
        # bullet_group.add(bullet)

        for i in players_group:
            all_sprites.add(i)
        for i in npc_group:
            all_sprites.add(i)
        # for i in bullet_group:
        # all_sprites.add(i)

        ######################################################


    #timing
    ##################################
    clock.tick(FPS)
    ##################################

    #collecting info
    ##################################

    #quiting the game when we hit the X
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
        #     if event.key == pg.K_SPACE:
        #         player.shoot()
            if event.key == pg.K_ESCAPE:
                playing = False
        if event.type == pg.QUIT:
            playing = False

    ##################################
    #update
    ##################################
    all_sprites.update()

    # if npc hits player
    hits = pg.sprite.spritecollide(player, npc_group, True,pg.sprite.collide_circle)
    for hit in hits:
        #playing = False
        npc.spawn()
        r.choice(expl_sounds).play()
        player.sheild -= hit.radius*2
        exlp = Explosion(hit.rect.center, "sm")
        all_sprites.add(exlp)
        if player.sheild <= 0:
            deat_expl = Explosion(player.rect.center,"player")
            all_sprites.add(deat_expl)
            player.hide()

            if player.lives <= 0:
                game_over = True


    # if bullet hits npc
    hits = pg.sprite.groupcollide(npc_group,bullet_group,True,True)
    for hit in hits:
        score += 50 - hit.radius
        exlp = Explosion(hit.rect.center,"lg")
        all_sprites.add(exlp)
        npc.spawn()
        r.choice(expl_sounds).play()
        if r.random()>.85:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            pow_group.add(pow)
    hits = pg.sprite.groupcollide(npc_group, explo_sprites, True, True)
    for hit in hits:
        score += 50 - hit.radius
        exlp = Explosion(hit.rect.center, "lg")
        all_sprites.add(exlp)
        npc.spawn()
        r.choice(expl_sounds).play()



    hits = pg.sprite.spritecollide(player, pow_group, True, pg.sprite.collide_circle)
    for hit in hits:
        if hit.type == "sheild":
            num = r.randint(15,50)
            player.pow_sheild(num)
        elif hit.type == "gun":
            player.pow_gun()
        elif hit.type == "bomb":
            player.bomb += 1
            if player.bomb >= 5:
                player.bomb = 5


    ##################################
    #Render
    ##################################
    #print(score)
    screen.fill(BLACK)
    screen.blit(background,background_rect)
    all_sprites.draw(screen)
    #draw hud
    draw_text(screen,"Score:"+str(score),18,WIDTH/2,10,WHITE)
    draw_bar(screen,5,10,player.sheild)
    draw_lives(screen, WIDTH-100,10,player.lives,player_mini_img)
    draw_lives(screen,0,HEIGHT-25,player.bomb, mini_bomb)
    pg.display.flip()
    ##################################


pg.quit()
###############################################
############################################################################