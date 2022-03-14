import pygame

pygame.init()
screen = pygame.display.set_mode((640, 240))

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(YELLOW)
    pygame.display.update()

pygame.quit()