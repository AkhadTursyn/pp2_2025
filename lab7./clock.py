import pygame
import sys
from datetime import datetime

pygame.init()

w, h = 650,650
screen = pygame.display.set_mode((w, h))

clock = pygame.image.load("/Users/ahadtursyn/Desktop/mickeyclock.jpeg")
minute_hand = pygame.image.load("/Users/ahadtursyn/Desktop/min_hand.png")
second_hand = pygame.image.load("/Users/ahadtursyn/Desktop/sec_hand.png")

clock = pygame.transform.scale(clock, (w, h))

center_x = w // 2
center_y = h // 2

def draw_hand(image, angle, length_offset):
    rotated_image = pygame.transform.rotate(image, -angle)
    rect = rotated_image.get_rect()
    rect.center = (center_x, center_y)
    rect.centery -= length_offset
    screen.blit(rotated_image, rect.topleft)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    now = datetime.now()
    minute = now.minute
    second = now.second

    screen.fill((255, 255, 255))

    screen.blit(clock, (0, 0))

    minute_angle = minute * 6 
    second_angle = second * 6  

    draw_hand(minute_hand, minute_angle, 0)  
    draw_hand(second_hand, second_angle, 0) 

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()