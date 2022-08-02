from models import Tilemap
from enums import TileEnum
import random


class MapGeneratorService:

    @staticmethod
    def generator_random_map(
        sizetilemap: tuple[int, int] = (10, 10)
    ) -> Tilemap:
        
        return Tilemap(id="random_map_test", tiles = [])
    
    def generate_tile_matrix_enum(size_tilemap: tuple[int, int]) -> list[list[TileEnum]]:
        tilemap = []
        for i in range(size_tilemap[0]):
            line = [random.randint(1,2) for j in range(size_tilemap[1])]
            tilemap.append(line)
        return tilemap

    def ggg(size_tilemap: tuple[int, int]) -> list[list[TileEnum]]:
        tilemap = [0 for i in range(size_tilemap[0])]
        
