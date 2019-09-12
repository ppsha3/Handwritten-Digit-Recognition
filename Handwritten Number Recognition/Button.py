import pygame
from Colours import *


class Button():

    def setText(self, text):

        self.txt_surf = pygame.font.Font(None, 25).render(text, True, colours['black'])
        txt_width, txt_height = self.txt_surf.get_size()

        x_point = self.button_location[0] + (self.button_size[0]/2) - (txt_width/2)
        y_point = self.button_location[1] + (self.button_size[1]/2) - (txt_height/2)

        self.txt_loc = (x_point, y_point)


    def __init__(self, gameDisplay, colour, button_location, button_size):

        self.button_location = button_location
        self.colour = colour
        self.button_size = button_size
        self.gameDisplay = gameDisplay


    def draw(self):

        self.rect = pygame.draw.rect(
            self.gameDisplay,
            self.colour,
            (self.button_location[0], self.button_location[1],
                self.button_size[0], self.button_size[1]),
             2
        )

        self.gameDisplay.blit(self.txt_surf, self.txt_loc)
