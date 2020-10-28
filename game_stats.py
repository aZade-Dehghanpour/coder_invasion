import sys
import pygame

class GameStats:
    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.game_active = True
        self.reset_stats()
   
    def reset_stats(self):
        self.ship_left = self.settings.ship_limit

    def game_over(self):
        
        self.image = pygame.image.load("images/game_over.png")
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center
        self.screen.blit(self.image,self.rect)
