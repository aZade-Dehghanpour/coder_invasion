import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    def __init__(self,ai_game):
        super.__init__()
        self.screen = ai_game.screen()
        self.screen_rect = ai_game.get_rect()
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.speed = self.settings.bullet_speed
        self.rect = pygame.rect((0,0),self.settings.rect_height,self.settings.rect_width)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -=self.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self) :
        pygame.draw(self.screen_rect,self.color,self.rect)
