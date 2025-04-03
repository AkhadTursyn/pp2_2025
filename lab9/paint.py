import pygame, sys, random, time, math
from pygame.locals import *

pygame.init()

# Терезе және тор параметрлері
WIDTH, HEIGHT = 850, 600
CELL_SIZE = 20

# Түстер
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Терезе жасау
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Paint Application")
clock = pygame.time.Clock()

# Сурет салу аймағы 
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# Ағымдағы параметрлер
current_tool = "pen"  # Қазіргі таңдалған құрал
current_color = BLACK  # Қазіргі түс
brush_size = 4  # Қалам өлшемі
eraser_size = 20  # Өшіргіш өлшемі
start_pos = None  # Фигураларды салуды бастау нүктесі

# Құралдарды көрсету функциясы

def draw_instructions():
    font = pygame.font.SysFont("Verdana", 16)
    instructions = [
        "Tools: 1-Pen 2-Rectangle 3-Circle 4-Eraser 5-Square 6-Right Triangle 7-Equilateral Triangle 8-Rhombus",
        "Colors: R-Red G-Green B-Blue Y-Yellow",
        "Press C for Black, W for White (eraser uses white)",
    ]
    y = 5
    for line in instructions:
        text = font.render(line, True, BLACK)
        screen.blit(text, (5, y))
        y += 20

# Тікбұрышты үшбұрыш салу функциясы

def draw_right_triangle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    pygame.draw.polygon(surface, color, [(x1, y1), (x1, y2), (x2, y2)], 2)

# Тең қабырғалы үшбұрыш салу функциясы

def draw_equilateral_triangle(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    base = abs(x2 - x1)
    height = (math.sqrt(3) / 2) * base
    pygame.draw.polygon(surface, color, [(x1, y2), (x2, y2), ((x1 + x2) // 2, y2 - height)], 2)

# Ромб салу функциясы

def draw_rhombus(surface, color, start, end):
    x1, y1 = start
    x2, y2 = end
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    pygame.draw.polygon(surface, color, [
        ((x1 + x2) // 2, y1),  
        (x2, (y1 + y2) // 2),  
        ((x1 + x2) // 2, y2),  
        (x1, (y1 + y2) // 2)   
    ], 2)

# Негізгі цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        # Құрал таңдау
        if event.type == KEYDOWN:
            if event.key == K_1:
                current_tool = "pen"
            elif event.key == K_2:
                current_tool = "rect"
            elif event.key == K_3:
                current_tool = "circle"
            elif event.key == K_4:
                current_tool = "eraser"
            elif event.key == K_5:
                current_tool = "square"
            elif event.key == K_6:
                current_tool = "right_triangle"
            elif event.key == K_7:
                current_tool = "equilateral_triangle"
            elif event.key == K_8:
                current_tool = "rhombus"
            # Түс таңдау
            elif event.key == K_r:
                current_color = RED
            elif event.key == K_g:
                current_color = GREEN
            elif event.key == K_b:
                current_color = BLUE
            elif event.key == K_y:
                current_color = YELLOW
            elif event.key == K_c:
                current_color = BLACK
            elif event.key == K_w:
                current_color = WHITE

        # Салуды бастау
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  
                start_pos = event.pos
                if current_tool in ["pen", "eraser"]:
                    draw_color = WHITE if current_tool == "eraser" else current_color
                    pygame.draw.circle(canvas, draw_color, event.pos, brush_size if current_tool == "pen" else eraser_size)

        # Қолмен сурет салу
        if event.type == MOUSEMOTION:
            if event.buttons[0]:
                if current_tool in ["pen", "eraser"]:
                    draw_color = WHITE if current_tool == "eraser" else current_color
                    pygame.draw.circle(canvas, draw_color, event.pos, brush_size if current_tool == "pen" else eraser_size)

        # Фигураны аяқтау
        if event.type == MOUSEBUTTONUP:
            if event.button == 1 and start_pos:
                end_pos = event.pos
                x1, y1 = start_pos
                x2, y2 = end_pos
                width = abs(x2 - x1)
                height = abs(y2 - y1)

                if current_tool == "rect":
                    rect = pygame.Rect(min(x1, x2), min(y1, y2), width, height)
                    pygame.draw.rect(canvas, current_color, rect, 2)

                elif current_tool == "square":
                    side = min(width, height)
                    rect = pygame.Rect(min(x1, x2), min(y1, y2), side, side)
                    pygame.draw.rect(canvas, current_color, rect, 2)

                elif current_tool == "circle":
                    radius = int(math.hypot(x2 - x1, y2 - y1))
                    pygame.draw.circle(canvas, current_color, start_pos, radius, 2)

                elif current_tool == "right_triangle":
                    draw_right_triangle(canvas, current_color, start_pos, end_pos)

                elif current_tool == "equilateral_triangle":
                    draw_equilateral_triangle(canvas, current_color, start_pos, end_pos)

                elif current_tool == "rhombus":
                    draw_rhombus(canvas, current_color, start_pos, end_pos)

                start_pos = None

    # Экранды жаңарту
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))
    draw_instructions()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()