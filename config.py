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
            with open("./config.txt", "w") as self.configfile:
                self.config.write(self.configfile)
ConfigFile()