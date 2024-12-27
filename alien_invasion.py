import sys
import os
import pygame
from pyvirtualdisplay import Display
from settings import Settings
from ship import Ship

# Virtual Display শুরু করা (DISPLAY environment variable সেট করা)
os.environ['DISPLAY'] = ':0'  # DISPLAY সঠিকভাবে সেট করা
display = Display(visible=0, size=(800, 600))
display.start()

class AlienInavsion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)  # Creating a ship and passing this module utility to ship 

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    # Make a game instance and run the game
    ai = AlienInavsion()
    ai.run_game()
