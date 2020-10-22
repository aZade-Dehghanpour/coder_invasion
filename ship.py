import pygame
class Ship:
    """ A class to manage the ship"""
    
    def __init__(self, ai_game):
        # Initialize the ship and set its starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # Load the ship image and get its rect
        self.image = pygame.image.load("images/my_ship.png")
        #self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        #self.image.set_colorkey((2,253,255))
        #Movement Flag
        self.move_right = False
        self.move_left = False

    def update(self):
        """ Update location of ship based on movement flag"""
        if self.move_right:
            self.rect.x +=1
        elif self.move_left:
            self.rect.x -=1

    def blitme(self):
        """ Draw the ship at the current location"""
        self.screen.blit(self.image,self.rect) 