import sys
import pygame
class AlienInvasion:
    """ Overall Class to manage game assets and behaviours"""
    def __init__(self):
        """ Initialize the game and set game resources"""
        #initialize the background setting
        pygame.init()
        # Initialize a window or screen for display
        self.screen = pygame.display.set_mode((1200,800))
        # Set background color
        self.bg_color = (30,30,30)
        # Set the current window caption
        pygame.display.set_caption("Alien Invasion")
    def run_game(self):
        """ Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #Re-draw the screen during each pass through the loop
                self.screen.fill(self.bg_color)
                #Make the most recently drawn screen visible.
                pygame.display.flip()
if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()

