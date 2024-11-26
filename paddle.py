import pygame

class Player():

    def __init__(self, rect):
        super().__init__()
        self.rect = pygame.Rect(rect)