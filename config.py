import configparser
from pathlib import Path

class ConfigFile():                                                                     #TODO Config File Creation
    def __init__(self):
        self.configF = Path("./config.txt")
        if self.configF.is_file():                                                      # Checks to see if the file exists
            None                                                                        # If it exists, nothing happens

        else:
            self.config = configparser.ConfigParser()                                   # If it doesn't exist, it creates it with default values #TODO Potential to also include Score and other Values to implement a Save Game feature.
            self.config['Display Settings'] = {'Resolution Width': 800,
                                               'Resolution Height': 600,}
            self.config['Game Save'] = {}
            self.gamesave = self.config['Game Save']
            self.gamesave['Score'] = '0'
            self.gamesave['click value'] = '1'
            self.gamesave['click multiplier'] = '1'
            self.gamesave['gpu value'] = '0'
            self.gamesave['gpu multiplier'] = '1'
            with open("./config.txt", "w") as self.configfile:
                self.config.write(self.configfile)
ConfigFile()