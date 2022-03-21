import pygame

pygame.init()
screen = pygame.display.set_mode((640, 240))

pygame.display.set_caption(f"OMG! Look at this cool snowman!")

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
ORANGE = (255,69,0)
BROWN = (139,69,19)
BLUE = (135,206,235)

background = BLUE
screen.fill(background)
pygame.draw.ellipse(screen, WHITE, (245, 130, 100, 100))
pygame.draw.ellipse(screen, WHITE, (260, 65, 75, 75))
pygame.draw.ellipse(screen, WHITE, (272, 27, 50, 50))
pygame.draw.ellipse(screen, BLACK, (285, 43, 5, 5))
pygame.draw.ellipse(screen, BLACK, (305, 43, 5, 5))
pygame.draw.ellipse(screen, BLACK, (295, 83, 5, 5))
pygame.draw.ellipse(screen, BLACK, (295, 113, 5, 5))
pygame.draw.ellipse(screen, BLACK, (295, 163, 5, 5))
pygame.draw.ellipse(screen, BLACK, (295, 193, 5, 5))
pygame.draw.polygon(surface=screen, color=(ORANGE),points=[(300, 53), (290, 53), (285, 73)])
pygame.draw.line(screen, BROWN, (260,90),(230,70))
pygame.draw.line(screen, BROWN, (361,70),(331,90))


pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()