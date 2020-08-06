import pygame
import threading
from time import sleep
import random
import math as mt

class thunder:
    def __init__(self, initial_point):
        self.initial_point = initial_point
        self.final_point  = (self.initial_point[0] + random.randint(-30,30), self.initial_point[1] + random.randint(10,40))
        self.num_sons = 0
        self.sons = []

    def lighten(self):
        self.num_sons = random.choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,2])
        # self.num_sons = 1
        if ( self.final_point[1] < 1000 and self.final_point[1] > 0 ):
            for i in range(self.num_sons):
                self.sons.append(thunder(self.final_point))
                self.sons[i].lighten()
    
    def drawn_thunder(self, win):
        pygame.draw.line(win, (0, 255, 255), self.initial_point, self.final_point, 5)
        pygame.display.flip()
        for elem in self.sons:
            elem.drawn_thunder(win)


if __name__ == "__main__":

    # LEITURA DOS DADOS E INCIALIZAÇÃO DA JANELA
    pygame.init()
    win = pygame.display.set_mode()
    win = pygame.display.set_mode((1000, 1000), 0, 8)
    win.fill((0, 0, 0))
    pygame.display.flip()
    init = (0,0)
    end = (10,10)
    # while(end[1] < 1000):
    #     pygame.draw.line(win, (0, 255, 255),init, end, 1)
    #     pygame.display.flip()
    #     init = end
    #     end = (end[0]+10, end[1]+5)

    thor = thunder((500,50))
    thor.lighten()
    thor.drawn_thunder(win)
    pygame.display.flip()


    while(True):
        for event in pygame.event.get():
            if ( event.type == pygame.KEYDOWN ):
                if ( event.key == pygame.K_SPACE ):
                    pygame.display.quit()
                    break