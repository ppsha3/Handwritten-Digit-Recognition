from pygame import *
from Colours import *


class Window():

    def run(self):
        display.update()
        self.gameDisplay.fill(colours['white'])


    def makeWindow(self, title):
        self.clock = time.Clock()

        gameDisplay = display.set_mode((self.display_width, self.display_height))
        display.set_caption(title)

        return gameDisplay


    def __init__(self, display_width, display_height, title):
        init()  # pygame init

        self.display_width = display_width
        self.display_height = display_height

        self.gameDisplay = self.makeWindow(title)
