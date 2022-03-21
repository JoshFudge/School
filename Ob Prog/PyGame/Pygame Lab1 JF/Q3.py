from pygame import mixer
import pygame
from pygame.locals import *
pygame.init()

#Set some basic things
height = 700
width = 600
screen = pygame.display.set_mode((height, width))
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLUE = (135,206,235)
ORANGE = (255,69,0)
FPS = 100
background = pygame.image.load('The Crock.jpg')

# Set up the background music
mixer.music.load('background.wav')
mixer.music.play(-1) 

pygame.display.set_caption(f"Yooooo these shapes can move on their own????")


rect1= Rect(80, 4,70,70)
rect2= Rect(300, 140,70,70)
speed = [2, 2]
speed2 = [-3, 5]
clock = pygame.time.Clock()

running = True
while running:
    screen.blit(background, (0, 0))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# Move the forst rectangle
    rect1.move_ip(speed)

    if rect1.left < 0:
       speed[0] *= -1
    if rect1.right > height:
        speed[0] *= -1
    if rect1.top < 0:
       speed[1] *= -1
    if rect1.bottom > width:
       speed[1] *= -1

# Move the second rectangle
    rect2.move_ip(speed2)

    if rect2.left < 0:
       speed2[0] *= -1
    if rect2.right > height:
        speed2[0] *= -1
    if rect2.top < 0:
       speed2[1] *= -1
    if rect2.bottom > width:
       speed2[1] *= -1

    
    # Collision things
    if rect1.colliderect(rect2):
        speed[0] *= -1
        speed2[0] *= -1
        speed[1] *= -1
        speed2[1] *= -1
        hit_sound = mixer.Sound('laser.wav')
        hit_sound.play()




    
    
    pygame.draw.rect(screen, ORANGE, rect1)
    pygame.draw.rect(screen, MAGENTA, rect2)

    pygame.display.flip()

    clock.tick(FPS)
pygame.quit()