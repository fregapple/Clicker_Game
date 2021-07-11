import pygame, sys, os
from pygame import HWSURFACE, DOUBLEBUF, RESIZABLE

r = "%.2f"                                                                  # This rounds the decimal to Two.

class Window():                                                             #TODO Pygame Window settings.
    def __init__(self):
        pygame.display.set_caption(f"Clicker Game - Score: {r % Score().score}") # Adds caption to the Window.
        self.res = Resolution().res                                               #TODO Would like to create a config file that can change Resolutions, like in my emulator, rather than being static.
        self.screen = pygame.display.set_mode(self.res)                     # Sets the resolution based on self.res.
        pygame.init()                                                       # Initialises Pygame Window.
        self.display = 1                                                    # Value to keep Pygame Window running.
        self.clock = pygame.time.Clock()                                    # Sets Clock so we can have ingame timer and FPS.

    def resize (self):                                                      #TODO Will work on this section once I have added the config file that saves the Resolution.
        pass

    def tick(self, fps):                                                    # Call this to adjust FPS. Though probably won't be called again past what is initially set.
        self.clock.tick(fps)

    def refresh(self):                                                      # Call this to refresh display.
        pygame.display.flip()  

class Resolution():
    def __init__(self):
        Resolution.__call__(self)

    def __call__(self):
        self.res = (800, 600)                                                     
    
class Score():                                                              #TODO Game Score.
    
    def __init__(self):                                                     # Initial Score upon start up. #TODO Perhaps we can have this as a saved value for if you'd like to save the game?
        self.score = 0

    def __call__(self):                                                     # Call this to get score and refresh Window Caption to new Value.
        self.score
        pygame.display.set_caption(f"Clicker Game - Score: {r % self.score}")      
    

class Time():                                                               # Time settings for time based events.

    def __init__(self):
        self.time_delay = 100
        self.timer_event = pygame.USEREVENT+1
        pygame.time.set_timer(self.timer_event, self.time_delay)
 

class ClickValue():                                                         #TODO Click Value settings.
    def __init__(self):                                                     # Initialises functions to be used straight away without being called.
        ClickValue.__objectValue__(self)
        ClickValue.__upgradeQuantity__(self)
    
    def __objectValue__(self):                                              # The Value of a click EG how many points it will give.
        self.click = 1

    def __upgradeQuantity__(self):                                          # The Modifier based on how many clickers EG if you click you get 2 if value is 2. #TODO This will probably be deleted for this Class.
        self.clicks = 1

    def clickBuy(self):                                                     # Buying extra clicks #TODO Same as above, this will probably be deleted. Instead we will use an upgrade multiplier. In for testing.
        self.click = self.click + 1


class GPUValue():                                                           #TODO GPU Value settings. 
    def __init__(self):
        GPUValue.__objectValue__(self)
        GPUValue.__upgradeModifier__(self)
        GPUValue.__upgradeQuantity__(self)       

    def __objectValue__(self):
        self.gpu = 0

    def __upgradeModifier__(self):                                            #TODO This section could be made into it's own class to be used with every xValue().
        self.a = 3                                                          # This currently doesn't do anything, but can be a section we use in conjunction with __upgradeModifier__. EG. gv.clicks = gv.clicks * gv.a.   
        self.b = 4                                                          # If kept to individual classes, each xValue can have individual upgrade multiplier paths rather than a global one.

    def __upgradeQuantity__(self):                                          #TODO Unlike Clicks, this will most likely stay as it determines how many GPUs you have.
        self.gpus = 1

    def gpuBuy(self):                                                       # Buying extra GPUs. #TODO Value is set low to allow for 1 gpu to gain 1 score after 10 seconds.
        self.gpu = self.gpu + 0.01

pygame.font.init()
myfont = pygame.font.SysFont("arial", 16)
s = Window()                                                                # This section is needed for other pages to use the shortcuts effectively. #TODO ADD NEW CLASSES HERE. 
sc = Score()
clv = ClickValue()
gv = GPUValue()
t = Time()
    





    

    



        
        
       

