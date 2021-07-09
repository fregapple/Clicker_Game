import pygame, sys, os
from pygame import HWSURFACE, DOUBLEBUF, RESIZABLE

r = "%.2f"


class Window():
    def __init__(self):
        pygame.display.set_caption(f"Clicker Game - Score: {r % sc.score}")
        self.res = (800, 600)
        self.screen = pygame.display.set_mode(self.res)
        pygame.init()
        self.display = 1
        self.clock = pygame.time.Clock()

    def resize (self):
        pass

    def tick(self, fps):
        self.clock.tick(fps)

    def refresh(self):
        pygame.display.flip()
    
class Score():
    
    def __init__(self):
        self.score = 0

    def __call__(self):
        self.score
        pygame.display.set_caption(f"Clicker Game - Score: {r % self.score}")      
    

class Time():

    def __init__(self):
        self.time_delay = 100
        self.timer_event = pygame.USEREVENT+1
        pygame.time.set_timer(self.timer_event, self.time_delay)
 

class ClickValue():
    def __init__(self):
        ClickValue.__objectValue__(self)
        ClickValue.__upgradeModifier__(self)
    
    def __objectValue__(self):
        self.click = 1

    def __upgradeModifier__(self):
        self.clicks = 1

    def clickBuy(self):
        self.click = self.click + 1


class GPUValue():
    def __init__(self):
        GPUValue.__objectValue__(self)
        GPUValue.__upgradeModifier__(self)
        GPUValue.__upgradeMValue__(self)       

    def __objectValue__(self):
        self.gpu = 0

    def __upgradeMValue__(self):
        self.a = 3

    def __upgradeModifier__(self):
        self.gpus = 1

    def gpuBuy(self):
        self.gpu = self.gpu + 0.01



s = Window()
sc = Score()
clv = ClickValue()
gv = GPUValue()
t = Time()
    





    

    



        
        
       

