import pygame


class TileTextures:
    def __init__(self):
        self.surfaces = [
            pygame.image.load("assets/grass.png").convert()
        ]
