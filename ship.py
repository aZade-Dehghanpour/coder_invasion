import pygame
class Ship:
    """ A class to manage the ship"""
    
    def __init__(self, ai_game):
        # Initialize the ship and set its starting position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Load the ship image and get its rect
        self.image = pygame.image.load("images/my_ship.png")
        #self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        #self.image.set_colorkey((2,253,255))
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Movement Flag
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
    
    def center_ship(self):
        
        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """ Update location of ship based on movement flag"""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            
        elif self.move_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        
        #elif self.move_up and self.rect.top >0:
           # self.y -= self.settings.ship_speed

       # elif self.move_down and self.rect.bottom < self.settings.height:
           # self.y += self.settings.ship_speed
        
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """ Draw the ship at the current location"""
        self.screen.blit(self.image,self.rect) 