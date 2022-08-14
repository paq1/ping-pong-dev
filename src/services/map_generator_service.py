from models import Tilemap
from enums import TileEnum
import random


class MapGeneratorService:

    @staticmethod
    def generator_random_map(
        sizetilemap: tuple[int, int] = (10, 10)
    ) -> Tilemap:
        return Tilemap(id="random_map_test", tiles = MapGeneratorService.generate_tile_matrix_enum(sizetilemap))
    
    @staticmethod
    def generate_tile_matrix_enum(size_tilemap: tuple[int, int]) -> list[list[TileEnum]]:
        rows, cols = size_tilemap
        return [[MapGeneratorService.get_rand_tile()] * cols] * rows

    @staticmethod
    def get_rand_tile() -> int:
        random.randint(1,2)
