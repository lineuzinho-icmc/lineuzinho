from os import path, listdir
from random import choice

class Ainer:
    def __init__(self):
        self.ainRepo = './resources/ains' # Relative to project's root
        self.ains = listdir(path.join('..', self.ainRepo))

    def getRandomAinPath(self):
        return path.join(self.ainRepo, choice(self.ains))