import imp
from turtle import st
import pygame, sys
from settings import * 

class Game:
    def __init__(self):
        

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("He do be walking around the map tho")
        self.clock = pygame.time.Clock()

    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            
            self.screen.fill('BLACK')
            pygame.display.update()
            self.clock.tick(FPS)
           

if __name__== "__main__":
    game = Game()
    game.run()