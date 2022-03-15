import pygame

pygame.init()
screen = pygame.display.set_mode((640, 240))

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

background = (125, 125, 125)

# -- RECTANGLES -- #
screen.fill(background)
pygame.draw.rect(screen, RED, (50, 20, 120, 100))
pygame.draw.rect(screen, GREEN, (100, 60, 120, 100))
pygame.draw.rect(screen, BLUE, (150, 100, 120, 100))

pygame.draw.rect(screen, RED, (350, 20, 120, 100), 1)
pygame.draw.rect(screen, GREEN, (400, 60, 120, 100), 4)
pygame.draw.rect(screen, BLUE, (450, 100, 120, 100), 8)

# -- CIRCLES (ELLIPSES) -- #
screen.fill(background)
pygame.draw.ellipse(screen, RED, (50, 20, 160, 100))
pygame.draw.ellipse(screen, GREEN, (100, 60, 160, 100))
pygame.draw.ellipse(screen, BLUE, (150, 100, 160, 100))

pygame.draw.ellipse(screen, RED, (350, 20, 160, 100), 1)
pygame.draw.ellipse(screen, GREEN, (400, 60, 160, 100), 4)
pygame.draw.ellipse(screen, BLUE, (450, 100, 160, 100), 8)

pygame.display.update()  # update (redraw) the screen

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
