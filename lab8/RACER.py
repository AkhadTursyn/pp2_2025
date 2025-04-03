import pygame, sys, random, datetime, os, time
from pygame.locals import *

pygame.init()


font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, (0,0,0))

background = pygame.image.load("/Users/ahadtursyn/Desktop/AnimatedStreet.png")


scr_width = 400
scr_height = 600
speed = 5
score = 0
coinscore = 0




disp = pygame.display.set_mode((scr_width,scr_height))
FPS = pygame.time.Clock()
disp.fill((255,255,255))



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/ahadtursyn/Desktop/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, scr_width - 40),0)

    def move(self):
        global score 
        self.rect.move_ip(0,speed)
        if (self.rect.bottom > scr_height):
            score+=1
            self.rect.top = 0
            self.rect.center = (random.randint(30, scr_width-30), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/ahadtursyn/Desktop/Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, scr_width-40), 320)
    
    def disappear(self):
        global coinscore
        coinscore += 1
        self.rect.center = (random.randint(40, scr_width-40), 320)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/ahadtursyn/Desktop/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (60,320)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < scr_width:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)


P = Player()
E = Enemy()
C = Coin()
Enemies = pygame.sprite.Group()
Enemies.add(E)

Coins = pygame.sprite.Group()
Coins.add(C)
all_sprites = pygame.sprite.Group()
all_sprites.add(E)
all_sprites.add(P)    
UP_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(UP_SPEED, 10000)

while True:
    for event in pygame.event.get():
        if event.type == UP_SPEED:
            speed+=1

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    disp.blit(background,(0,0))
    scores = font_small.render(str(score), True, (0,0,0))
    disp.blit(scores,(10,10))
    coinscores = font_small.render(str(coinscore), True, (0,0,0))       
    disp.blit(coinscores, (scr_width - 30,10))

    for coin in Coins:
        disp.blit(coin.image, coin.rect)


    for entity in all_sprites:
        disp.blit(entity.image,entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P, Enemies):
        pygame.mixer.Sound("/Users/ahadtursyn/Desktop/crash.wav").play()
        time.sleep(0.5)
        disp.fill((255,0,0))
        disp.blit(game_over,(30,250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollideany(P, Coins):
        pygame.mixer.Sound("/Users/ahadtursyn/Desktop/bell.wav").play()
        pygame.display.update()
        C.disappear()

    pygame.display.update()
    FPS.tick(60) 