import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from aliens import Aliens
from game_stats import GameStats
from time import sleep

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
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_feelt()

    def run_game(self):
        """ Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events
            self._check_event()
            if self.stats.game_active:
                #Update location of ship
                self.ship.update()
                #Update location of bullet
                self._update_bullets()
                #update location of aliens (move aliens)
                self._update_aliens()
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
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if not self.aliens:
            self.bullets.empty()
            self._create_feelt()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen)
        #Make the most recently drawn screen visible.
        if self.stats.game_active == False:
            self.stats.game_over()

        pygame.display.flip()

    def _check_keydown_events(self, event):

        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RIGHT and self.ship.move_left == False:
            self.ship.move_right = True   
        elif event.key == pygame.K_LEFT and self.ship.move_right == False:
            self.ship.move_left = True
        #elif event.key == pygame.K_UP and self.ship.move_down == False:
            #self.ship.move_up = True
        #elif event.key == pygame.K_DOWN and self.ship.move_up == False:
            #self.ship.move_down = True
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

    def _create_feelt(self):
        #create a number of aliens and add them to the fleet
        alien = Aliens(self)
        #available horizontal space
        alien_width, alien_height = alien.rect.size
        available_space_x = self.screen.get_rect().width - 2*alien_width
        availebe_space_y = self.screen.get_rect().height - self.ship.rect.height -3*alien_height
        number_of_rows = availebe_space_y//(2*alien_height)
        number_of_aliens = available_space_x//(2*alien_width)

        for row_number in range(number_of_rows):
            for alien_number in range(number_of_aliens):
                self._create_alien(alien_number,row_number)
            
    def _create_alien(self,alien_number,row_number):
        alien = Aliens(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2*alien_width*alien_number
        alien.y = alien_height + 2*alien_height*row_number
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)   

    def _update_aliens(self):
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen.get_rect().bottom:
                self._ship_hit()
                break


    def _ship_hit(self):
        self.stats.ship_left -=1
        if self.stats.ship_left>0:
            print("ship left:",self.stats.ship_left)
            self.aliens.empty()
            self.bullets.empty()
            self._create_feelt()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            self.aliens.empty()
            self.bullets.empty()

if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()

