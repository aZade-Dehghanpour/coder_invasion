import pygame
from pygame.sprite import Sprite

class Aliens(Sprite):
    """Class to create an alien"""

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = ai_game.screen.get_rect
        self.settings = ai_game.settings
        self.rect.x = self.rect.height
        self.rect.y = self.rect.width
        self.x = float(self.rect.x)        

    