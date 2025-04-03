import pygame, sys, random, time
from pygame.locals import *

pygame.init()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
CELL_SIZE = 20
COLS = WINDOW_WIDTH // CELL_SIZE
ROWS = WINDOW_HEIGHT // CELL_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game with Levels")
clock = pygame.time.Clock()

def generate_food(snake_body):
    while True:
        x = random.randint(0, COLS - 1)
        y = random.randint(0, ROWS - 1)
        if (x, y) not in snake_body:
            return (x, y)

snake = [(COLS // 2, ROWS // 2)]
direction = (1, 0)
food = generate_food(snake)
score = 0
level = 1
foods_eaten = 0
speed = 3
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == K_RIGHT and direction != (-1, 0):
                direction = (1, 0)
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])
    if new_head[0] < 0 or new_head[0] >= COLS or new_head[1] < 0 or new_head[1] >= ROWS or new_head in snake:
        running = False
    snake.insert(0, new_head)
    if new_head == food:
        score += 10
        foods_eaten += 1
        food = generate_food(snake)
        if foods_eaten % 3 == 0:
            level += 1
            speed += 1
    else:
        snake.pop()
    screen.fill(BLACK)
    food_rect = pygame.Rect(food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, RED, food_rect)
    for segment in snake:
        seg_rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, GREEN, seg_rect)
    info_text = pygame.font.SysFont("Verdana", 20).render("Score: " + str(score) + "  Level: " + str(level), True, WHITE)
    screen.blit(info_text, (10, 10))
    pygame.display.update()
    clock.tick(speed)

pygame.quit()
sys.exit()