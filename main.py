import pygame, sys, os

from pygame.locals import *
from config import *
from classes import *
from gamesave import *
from score_updater import *


def __main__():

    while w.display == 1:

        for x in pygame.event.get():
            if x.type == QUIT:
                GameSave().__call__()  # Calling this will save the game.
                w.display = 0
                quit()

            elif x.type == VIDEORESIZE:
                w.resize()

            elif x.type == MOUSEBUTTONDOWN:
                CLICKs()
            
            elif x.type == KEYDOWN:
                if x.key == K_SPACE:
                    clv.clickBuy()
                
                elif x.key == K_LALT:
                    gv.gpuBuy()

                elif x.key == K_s:
                    GameSave().__call__()

            elif x.type == t.timer_event:
                GPUs()
                
                
                

                
                
        w.screenClear()
        w.tick(60)

        # Text on Screen
        txs.WelcomeText()
        txs.ScoreText()
        txs.AltScoreText()
        txs.SaveInfo()
        
        w.refresh()
__main__()