import pygame
from models import TileTextures


class TileDrawService:

    def __init__(self, tile_textures: TileTextures, screen: pygame.display):
        self.tile_textures = tile_textures
        self.screen = screen

    def draw_tile(self, index: int, position: tuple[int, int]):
        self.screen.blit(self.tile_textures.surfaces[index], position)

    @staticmethod
    def draw_texture_at(
        tile_textures: TileTextures,
        screen: pygame.display,
        index: int,
        position: tuple[int, int]
    ):
        screen.blit(tile_textures.surfaces[index], position)
