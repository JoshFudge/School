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

start = (0, 0)
size = (0, 0)
drawing = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = event.pos
            size = 0, 0
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]

    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, (start, size), 2)
    pygame.display.update()

pygame.quit()
