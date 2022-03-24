
import pygame
from pygame.locals import *
pygame.init()

#Set some basic things
height = 640
width = 440
screen = pygame.display.set_mode((height, width))
WHITE = (255,255,255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (135,206,235)
FPS = 100


background = BLUE
pygame.display.set_caption(f"Click the shapes to move!")
clock = pygame.time.Clock()

font = pygame.font.SysFont('consolas', 50)



# creating 4 buttons
Up_text = font.render(f'Up', True, WHITE)
up_rect = Up_text.get_rect()
up_but = pygame.Rect(height/2,width/4,up_rect.w,up_rect.h)

Down_text = font.render(f'Down', True, WHITE)
down_rect = Down_text.get_rect()
down_but = pygame.Rect(height/2,width*(3/4),down_rect.w,down_rect.h)

Left_text = font.render(f'Left', True, WHITE)
left_rect= Left_text.get_rect()
left_but = pygame.Rect(height*(2/5),width/2,left_rect.w,left_rect.h)

Right_text = font.render(f'Right', True, WHITE)
right_rect = Right_text.get_rect()
right_but = pygame.Rect(height*(3/5),width/2,right_rect.w,right_rect.h)






# create moveable rectangle
rectangle1= Rect(80, 4,90,99)




running = True
while running:
      
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  running = False

            if event.type == MOUSEBUTTONDOWN:
                  if up_but.collidepoint(event.pos):
                        rectangle1.move_ip(0,-5)
                  
                  if down_but.collidepoint(event.pos):
                        rectangle1.move_ip(0,5)

                  if left_but.collidepoint(event.pos):
                        rectangle1.move_ip(-5,0)

                  if right_but.collidepoint(event.pos):
                        rectangle1.move_ip(5,0)
 



      #moveable square
      screen.fill(background)
      pygame.draw.rect(screen, BLACK, rectangle1)
      

      # The buttons
      pygame.draw.rect(screen, GRAY, up_but)
      screen.blit(Up_text,up_but)
      
      pygame.draw.rect(screen, GRAY, down_but)
      screen.blit(Down_text,down_but)

      pygame.draw.rect(screen, GRAY, left_but)
      screen.blit(Left_text,left_but)

      pygame.draw.rect(screen, GRAY, right_but)
      screen.blit(Right_text,right_but)





      pygame.display.flip()




clock.tick(FPS)