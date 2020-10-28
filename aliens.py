import pygame
from pygame.sprite import Sprite

class Aliens(Sprite):
    """Class to create an alien"""

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.rect.x = self.rect.height
        self.rect.y = self.rect.width
        self.x = float(self.rect.x) 
        self.y = float(self.rect.y) 
        self.speed = self.settings.alien_speed
        self.drop_speed = self.rect.height
        self.direction = 1     

    def update(self):
        self._change_alien_direction()
        self.x += self.speed*self.direction
        self.rect.x =self.x
    
    def _check_edges(self):
        if self.rect.right >= self.screen_rect.right or self.rect.left <= self.screen_rect.left:
            return True
    def _change_alien_direction(self):
        if self._check_edges():
            self.y += self.drop_speed
            self.rect.y = self.y
            self.direction *=-1

        