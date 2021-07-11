import pygame, sys, os

from pygame.locals import *
from cogs import *
from score_updater import *

"""
Trying to figure out how we should build the GUI.
Perhaps incorperating TKinter is an option, however functional, it is quite ugly.
"""

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
                scoretext = myfont.render(f"Score = {r % sc.score}", 1, (0,240,0))
                pygame.display.set_mode((Resolution().res)).blit(scoretext, (5, 10))
                
               
        
        s.tick(60)
        
        s.refresh()

__main__()