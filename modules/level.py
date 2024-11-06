import pygame
from modules.tile import Tile
from modules.constants import *

class Level():
    def __init__(self, map: list[list[int]], spawn_point):
        self.map = []
        self.spawn_point = spawn_point

        for y in range(len(map)):
            for x in range(len(map[y])):
                tile_type = map[y][x]
                if tile_type != 0:
                    self.map.append(Tile(x * TILE_SIZE, y * TILE_SIZE, tile_type))
        

    def draw(self, screen):
        for tile in self.map:
            tile.draw(screen)

