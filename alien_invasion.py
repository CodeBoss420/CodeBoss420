#day-1
import sys
import pygame

class AlienInavsion:
    """Overall class to manage game assets and behavior. """
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
    def run_game(self):
        """start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #make it most recently drawn screen visible
            pygame.display.flip()
if __name__ == "__main__":
    #make a game insatance , and run the game
    ai = AlienInavsion()
    ai.run_game()                                    