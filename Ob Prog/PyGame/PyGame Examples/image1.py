"""Move an image with the mouse."""

import pygame
from pygame.locals import *

RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()
w, h = 640, 240
screen = pygame.display.set_mode((w, h))
running = True

img = pygame.image.load('bird.png').convert()
img.convert()
# img = pygame.image.load('bird.png').convert()
rect = img.get_rect()  # creates rect same size as img
rect.center = w//2, h//2
moving = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False

        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
    
    screen.fill(GRAY)

    screen.blit(img, rect)  # https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
    pygame.draw.rect(screen, RED, rect, 1)

    pygame.display.update()

pygame.quit()