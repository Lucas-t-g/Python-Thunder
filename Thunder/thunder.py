import pygame
import threading
from time import sleep
import random
import math as mt
from pygame.locals import*


class thunder:
    def __init__(self, initial_point):
        self.initial_point = initial_point
        # self.direction = randon.randint(0, 360)
        # self.length = random.randint(10, 20)
        self.final_point  = (self.initial_point[0] + random.randint(-10,10), self.initial_point[1] + random.randint(10,20))
        self.num_sons = 0
        # random.randint(0,5)
        self.sons = []
        # for i in range(self.num_sons-1):
        #     self.sons.append(thunder(self.final_point))

    def lighten(self):
        self.num_sons = 1
        #random.randint(1,1)
        if ( self.final_point[1] < 1000 and self.final_point[1] > 0 ):

            for i in range(self.num_sons):
                self.sons.append(thunder(self.final_point))
                self.sons[i].lighten()
    
    def drawn_thunder(self, win):
        # x = self.final_point[0] - self.initial_point[0]
        # y = self.final_point[1] - self.initial_point[1]
        # tam = mt.sqrt(x**2 + y**2)
        # x1 = x/tam
        # y1 = y/tam
        # x = self.initial_point[0]
        # y = self.initial_point[1]
        # while (y < self.final_point[1]):
        #     win.set_at((int(x), int(y)), (0, 0, 255))
        #     x += x1
        #     y += y1
        pygame.draw.line(win, (0, 255, 255), self.initial_point, self.final_point, 5)

        for elem in self.sons:
            elem.drawn_thunder(win)
        



if __name__ == "__main__":

    # LEITURA DOS DADOS E INCIALIZAÇÃO DA JANELA
    pygame.init()
    win = pygame.display.set_mode()
    win = pygame.display.set_mode((1000, 1000), 0, 8)
    win.fill((0, 0, 0))
    pygame.display.flip()
    pygame.draw.line(win, (0, 255, 255), (500, 500), (500,250), 5)
    print("444")
    thor = thunder((700,500))
    pygame.draw.line(win, (0, 0, 255), thor.initial_point, thor.final_point)
    thor.lighten()
    thor.drawn_thunder(win)



    while(True):
        for event in pygame.event.get():
            if ( event.type == pygame.KEYDOWN ):
                if ( event.key == pygame.K_SPACE ):
                    pygame.display.quit()
                    break