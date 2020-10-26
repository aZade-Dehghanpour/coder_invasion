import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
class AlienInvasion:
    """ Overall Class to manage game assets and behaviours"""

    def __init__(self):
        """ Initialize the game and set game resources"""
        #initialize the background setting
        pygame.init()
        self.settings = Settings()
        # Initialize a window or screen for display
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.width =self.screen.get_rect().width
        self.settings.height = self.screen.get_rect().height
        # Set background color
        self.bg_color = self.settings.bg_color
        # Set the current window caption
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """ Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events
            self._check_event()
            #Update location of ship
            self.ship.update()
            #Update location of bullet
            self._update_bullets()
            #Delete Bullets
            
            #Re-draw the screen during each pass through the loop
            self._update_screen()
                       
    def _check_event(self):
        """responds to key press and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)    
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
                if bullet.rect.bottom<0:
                    self.bullets.remove(bullet)
                print(len(self.bullets))

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #Make the most recently drawn screen visible.
        pygame.display.flip()

    def _check_keydown_events(self, event):

        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RIGHT and self.ship.move_left == False:
            self.ship.move_right = True   
        elif event.key == pygame.K_LEFT and self.ship.move_right == False:
            self.ship.move_left = True
        elif event.key == pygame.K_UP and self.ship.move_down == False:
            self.ship.move_up = True
        elif event.key == pygame.K_DOWN and self.ship.move_up == False:
            self.ship.move_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False
        elif event.key == pygame.K_UP:
            self.ship.move_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.move_down = False

    def _fire_bullet(self):
        #create a bullet and add it to the bullet group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet) 

if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()

