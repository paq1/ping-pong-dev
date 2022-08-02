from models import Tilemap


class MapGeneratorService:

    @staticmethod
    def generator_random_map() -> Tilemap:
        return Tilemap(id="random_map_test", tiles = [])
    