import pygame

class Color:
    # Pre-defined colors
    RED = pygame.Color(255, 0, 0)
    GREEN = pygame.Color(0, 255, 0)
    BLUE = pygame.Color(0, 0, 255)
    WHITE = pygame.Color(255, 255, 255)
    BLACK = pygame.Color(0, 0, 0)
    YELLOW = pygame.Color(255, 255, 0)

    @staticmethod
    def rgb(self, rgb):
        return pygame.Color(rgb)
