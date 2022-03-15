import pygame
pygame.init()

screen = pygame.display.set_mode((640, 240))
pygame.display.set_caption(f"First PyGame")


FPS = 60 
fpsClock = pygame.time.Clock() 

width, height = 640, 320
size = (width, height)
PURPLE = (138,43,226)
ball = pygame.image.load("death_star.png")
rect = ball.get_rect()
speed = [2, 2]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.K_w:
            rect = rect.move(speed)

    screen.fill(PURPLE)
    screen.blit(ball, rect)
    pygame.display.update()
    fpsClock.tick(FPS)
    
    pygame.display.update()

pygame.quit()