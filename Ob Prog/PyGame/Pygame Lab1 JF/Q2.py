

import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640, 240))
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLUE = (135,206,235)
FPS = 60
background = BLUE


pygame.display.set_caption(f"Yooooo these shapes can move")


dir = {K_LEFT: (-15, 0), K_RIGHT: (15, 0), K_UP: (0, -15), K_DOWN: (0, 15)}
dir_2 = {K_a: (-15, 0), K_d: (15, 0), K_w: (0, -15), K_s: (0, 15)}



rectangle1= Rect(80, 4,90,99)
rectangle2= Rect(300, 4,90,99)








running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key in dir:
                v = dir[event.key]
                rectangle1.move_ip(v)

        if event.type == KEYDOWN:
            if event.key in dir_2:
                v = dir_2[event.key]
                rectangle2.move_ip(v)


    screen.fill(background)
    pygame.draw.rect(screen, YELLOW, rectangle1)
    pygame.draw.rect(screen, MAGENTA, rectangle2)
    pygame.display.flip()
    
pygame.quit()