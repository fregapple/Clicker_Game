import pygame, configparser
from loadgame import *
from classes import *

class GameSave():
    def __init__(self):
        GameSave.__call__(self)
    
    def __call__(self):
        self.config = configparser.ConfigParser()
        self.config.read("./config.txt")
        self.config.set('Game Save', 'score', f'{sc.score}')
        self.config.set('Game Save', 'click value', f'{clv.click}')
        self.config.set('Game Save', 'click multiplier', f'{clv.clicks}')
        self.config.set('Game Save', 'gpu value', f'{gv.gpu}')
        self.config.set('Game Save', 'gpu multiplier', f'{gv.gpus}')
        with open("./config.txt", "w") as self.configfile:
            self.config.write(self.configfile)
