import pygame, sys, random, time, math
from pygame.locals import *

pygame.init()

# Window dimensions and grid settings
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
YELLOW= (255, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Application")
clock = pygame.time.Clock()

# Create a canvas surface for drawing
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# Current drawing settings
current_tool = "pen"  # Options: "pen", "rect", "circle", "eraser"
current_color = BLACK
brush_size = 4
eraser_size = 20

# Function to display tool instructions on screen
def draw_instructions():
    font = pygame.font.SysFont("Verdana", 16)
    instructions = [
        "Tools: 1-Pen 2-Rectangle 3-Circle 4-Eraser",
        "Colors: R-Red G-Green B-Blue Y-Yellow",
        "Press C for Black, W for White (eraser uses white)",
    ]
    y = 5
    for line in instructions:
        text = font.render(line, True, BLACK)
        screen.blit(text, (5, y))
        y += 20

# Variables for shape drawing
start_pos = None  # Stores starting mouse position for rectangle/circle

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        # Tool selection
        if event.type == KEYDOWN:
            if event.key == K_1:
                current_tool = "pen"
            elif event.key == K_2:
                current_tool = "rect"
            elif event.key == K_3:
                current_tool = "circle"
            elif event.key == K_4:
                current_tool = "eraser"
            # Color selection
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

        # Mouse button down starts drawing for shapes
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                start_pos = event.pos
                if current_tool in ["pen", "eraser"]:
                    draw_color = WHITE if current_tool == "eraser" else current_color
                    pygame.draw.circle(canvas, draw_color, event.pos, brush_size if current_tool == "pen" else eraser_size)
        # For free drawing with pen or eraser
        if event.type == MOUSEMOTION:
            if event.buttons[0]:
                if current_tool in ["pen", "eraser"]:
                    draw_color = WHITE if current_tool == "eraser" else current_color
                    pygame.draw.circle(canvas, draw_color, event.pos, brush_size if current_tool == "pen" else eraser_size)
        # Mouse button up for finalizing shapes
        if event.type == MOUSEBUTTONUP:
            if event.button == 1 and start_pos:
                end_pos = event.pos
                if current_tool == "rect":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                    pygame.draw.rect(canvas, current_color, rect, 2)
                elif current_tool == "circle":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    radius = int(math.hypot(x2 - x1, y2 - y1))
                    pygame.draw.circle(canvas, current_color, start_pos, radius, 2)
                start_pos = None

    # Draw the canvas onto the screen
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))
    draw_instructions()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()