import pygame
from pygame.locals import *

pygame.init()

# more on FPS (drawing speed):
# https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_Languages/Book%3A_Making_Games_with_Python_and_Pygame_(Sweigart)/03%3A_Pygame_Basics/3.18%3A_Frames_Per_Second_and_pygame.time.Clock_Objects
FPS = 60 
fpsClock = pygame.time.Clock() 

width, height = 640, 320
size = (width, height)
GREEN = (150, 255, 150)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode(size)

ball = pygame.image.load("death_star.png")
rect = ball.get_rect()
speed = [2, 2]

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    rect = rect.move(speed)
    if rect.left < 0 or rect.right > width:
        speed[0] = -speed[0]  # reverse the x value
    if rect.top < 0 or rect.bottom > height:
        speed[1] = -speed[1]    # reverse the y value

    screen.fill(BLACK)
    screen.blit(ball, rect)
    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()