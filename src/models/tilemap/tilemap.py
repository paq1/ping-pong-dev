from dataclasses import dataclass
from enums import TileEnum

@dataclass
class Tilemap():
    id: str
    tiles: list[list[TileEnum]]

    def __str__(self):
        return f"id : {self.id}"
