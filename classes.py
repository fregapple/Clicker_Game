import pygame, sys, os, configparser
from pygame import HWSURFACE, DOUBLEBUF, RESIZABLE
from pathlib import Path

r = "%.2f"                                                                               # This rounds the decimal to Two.

class Window():                                                                          #TODO Pygame Window settings.
    def __init__(self):
        pygame.display.set_caption(f"Clicker Game - Score: {r % Score().score}")         # Adds caption to the Window.
        self.res = Resolution().res                                                      # Links to Resolution Class that defines the screen size.
        self.screen = pygame.display.set_mode((self.res), HWSURFACE|DOUBLEBUF|RESIZABLE) # Sets the resolution based on self.res. 
        pygame.init()                                                                    # Initialises Pygame Window.
        self.display = 1                                                                 # Value to keep Pygame Window running.
        self.clock = pygame.time.Clock()                                                 # Sets Clock so we can have ingame timer and FPS.

    def resize(self):                                                                    # Resizes the screen and saves the changed value to config.txt. This then allows to dynamically change and scale objects and text on the screen.
        self.s = pygame.display.get_surface()
        self.w = self.s.get_width()
        self.h = self.s.get_height()
        self.config = configparser.ConfigParser()
        self.config.read("./config.txt")
        self.config.set('Display Settings', 'resolution width', f'{self.w}')
        self.config.set('Display Settings', 'resolution height', f'{self.h}')
        with open("./config.txt", "w") as self.configfile:
            self.config.write(self.configfile)
            self.config.read("./config.txt")
            self.ds = self.config['Display Settings']
            self.sw = int(self.ds['resolution width'])
            self.sh = int(self.ds['resolution height'])
            
    def reso(self):
        self.screen = pygame.display.set_mode((self.res), HWSURFACE|DOUBLEBUF|RESIZABLE) 

    def tick(self, fps):                                                                # Call this to adjust FPS. Though probably won't be called again past what is initially set.
        self.clock.tick(fps)

    def refresh(self):                                                                  # Call this to refresh display.
        pygame.display.update() 

    def textRef(self, blit):
        pygame.display.update(blit)

    def screenClear(self):
        self.screen.fill(c.black)

class Resolution():                                                         
    def __init__(self):
        Resolution.__call__(self)

    def __call__(self):
        self.config = configparser.ConfigParser()
        self.config.read("./config.txt")
        self.ds = self.config['Display Settings']
        self.sw = int(self.ds['resolution width'])
        self.sh = int(self.ds['resolution height'])
        self.res = (self.sw,self.sh)

class Colours():
    def __init__(self):
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (255,0,0)
        self.blue = (0,0,255)
        self.green = (0,255,0)
        self.purple = (255,0,255)
        self.yellow = (255,255,0)
        
class Score():                                                              #TODO Game Score.
    
    def __init__(self):                                                     # Initial Score upon start up. #TODO Perhaps we can have this as a saved value for if you'd like to save the game?
        self.score = 0

    def __call__(self):                                                     # Call this to get score and refresh Window Caption to new Value.
        self.score
        pygame.display.set_caption(f"Clicker Game - Score: {r % self.score}")  

class Text():
    
    def __init__(self, font, size, text, antialias, colour, background):
        pygame.font.init()
        self.font = font
        self.size = size
        self.text = text
        self.antialias = antialias
        self.colour = colour
        self.background = background
        texts = pygame.font.SysFont(self.font, self.size)
        self.text = texts.render(self.text, self.antialias, self.colour, self.background)

    def scoreText(self):
        self.text_rect = self.text.get_rect(center=(Resolution().sw/2, Resolution().sh/2))
        
        w.textRef(w.screen.blit(self.text, self.text_rect))   

    def altScoreText(self):
        w.textRef(w.screen.blit(self.text, (5,10)))
class Texts():
    def __init__(self):
        pygame.font.init()

    def ScoreText(self):    
        self.scoreText = Text('comic sans ms', 50, f'Score - {r % sc.score}', True, c.green, False).scoreText()
        self.scoreText

    def AltScoreText(self):
        self.altscoreText = Text('arial', 50, f'Score - {r % sc.score}', True, c.blue, True).altScoreText()

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




w = Window()                                                                # This section is needed for other pages to use the shortcuts effectively. #TODO ADD NEW CLASSES HERE. 
sc = Score()
clv = ClickValue()
gv = GPUValue()
t = Time()
c = Colours()
txs = Texts()

    





    

    



        
        
       

