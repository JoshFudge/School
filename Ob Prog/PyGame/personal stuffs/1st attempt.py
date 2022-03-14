import pygame
pygame.init()
screen = pygame.display.set_mode((640, 240))


PURPLE = (138,43,226)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(PURPLE)
    pygame.display.update()

pygame.quit()