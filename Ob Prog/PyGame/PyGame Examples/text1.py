"""Draw text to the screen."""

#           3 steps
# 1. create a Font object
# 2. render the text into an image
# 3. blit the image to the screen (or another Surface)

from itertools import count
import pygame
from pygame.locals import *
import time
 
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

BLACK = (0, 0, 0)
WHITE = (235, 235, 235)
GRAY = (200, 200, 200)
DARK_BLUE = (35, 35, 155)
DARK_RED = (145, 25, 26)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

sysfont = pygame.font.get_default_font()
print('system font :', sysfont)

font1 = pygame.font.SysFont('consolas', 50)
text_img1 = font1.render("LIVES: 0", True, WHITE)
text_img1_rect = text_img1.get_rect() # creating a rect from the font will give you the dimensions of the text, which can be used for positioning.

font2 = pygame.font.SysFont('edwardianscriptitc', 72)
text_img2 = font2.render('edwardianscriptitc', True, DARK_BLUE)

font3 = pygame.font.SysFont('jetbrainsmono', 72)
text_img3 = font3.render('jetbrainsmono', True, DARK_RED)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(GRAY)

    pygame.draw.rect(screen, BLACK, (0, 0, 800, text_img1_rect.h))
    screen.blit(text_img1, (SCREEN_WIDTH - text_img1_rect.w - 10, 3))

    screen.blit(text_img2, (20, 225))
    screen.blit(text_img3, (20, 500))

    pygame.display.update()

pygame.quit()