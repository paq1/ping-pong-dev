import sys
import pygame
from pygame.locals import *

from models import TileTextures
from services import TileDrawService, MapGeneratorService


def game():
    pygame.init()
    fps: float = 60.0
    fps_clock = pygame.time.Clock()
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    delta_time = 1 / fps

    tilemap = MapGeneratorService.generator_random_map()
    print(str(tilemap))

    tile_textures = TileTextures()
    tile_draw_service = TileDrawService(tile_textures, screen)

    while True:
        update(delta_time)
        draw(screen, tile_draw_service)
        delta_time = fps_clock.tick(int(fps))


def update(dt):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


def draw(screen_game, tile_draw_service: TileDrawService):
    screen_game.fill((100, 100, 0))
    tile_draw_service.draw_tile(0, (32, 32))
    pygame.display.flip()


if __name__ == "__main__":
    game()
