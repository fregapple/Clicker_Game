import pygame, sys, os

from pygame.locals import *
from cogs import *
from score_updater import *


def __main__():

    while s.display == 1:
        print(r % sc.score)


        for x in pygame.event.get():
            if x.type == QUIT:
                s.display = 0
                quit()

            elif x.type == MOUSEBUTTONDOWN:
                CLICKs()
            
            elif x.type == KEYDOWN:
                if x.key == K_SPACE:
                    clv.clickBuy()
                
                elif x.key == K_LALT:
                    gv.gpuBuy()

            elif x.type == t.timer_event:
                GPUs()
                
                
        
        s.tick(60)
    
    s.refresh()

__main__()