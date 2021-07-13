
import configparser
from config import ConfigFile
from pathlib import Path

class GameLoad():
    def __init__(self):
        GameLoad.__call__(self)

    def __call__(self):
        self.config = configparser.ConfigParser()
        self.config.read("./config.txt")
        self.ds = self.config['Display Settings']
        self.sw = int(self.ds['resolution width'])
        self.sh = int(self.ds['resolution height'])
        self.gs = self.config['Game Save']
        self.score = float(self.gs['score'])
        self.clickv = float(self.gs['click value'])
        self.clickm = float(self.gs['click multiplier'])
        self.gpuv = float(self.gs['gpu value'])
        self.gpum = float(self.gs['gpu multiplier'])
GameLoad()

