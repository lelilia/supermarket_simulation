'''SupermarketMap class'''

import cv2
import numpy as np

from supermarket_simulation.utils.constants import TILE_SIZE, OFS, MARKET

class SupermarketMap():
    '''Visualize the supermarket background'''

    def __init__(self, layout, tiles):
        self.tiles = tiles
        self.contents = [list(row) for row in layout.split('\n')]
        self.x_size = len(self.contents[0])
        self.y_size = len(self.contents)
        self.image = np.zeros(
            (self.y_size * TILE_SIZE, self.x_size * TILE_SIZE, 3), dtype=np.uint8
        )
        self.prepare_map()

    def get_tile(self, char):
        """returns the array for a given tile character"""
        if char == "#":
            return self.tiles[0:32, 0:32]
        elif char == "G":
            return self.tiles[7 * 32 : 8 * 32, 3 * 32 : 4 * 32]
        elif char == "C":
            return self.tiles[2 * 32 : 3 * 32, 8 * 32 : 9 * 32]
        else:
            return self.tiles[32:64, 64:96]

    def prepare_map(self):
        '''prepares the entire image as a big numpy array'''
        for y, row in enumerate(self.contents):
            for x, tile in enumerate(row):
                bm = self.get_tile(tile)
                self.image[
                    y * TILE_SIZE : (y + 1) * TILE_SIZE,
                    x * TILE_SIZE : (x + 1) * TILE_SIZE ] = bm

    def draw(self, frame, offset=OFS):
        '''
        draws the image into a frame
        offset pixels from the top left corner
        '''
        frame [
            OFS : OFS + self.image.shape[0],
            OFS : OFS + self.image.shape[1]
        ] = self.image

    def write_image(self, filename):
        '''
        writes the image into a file
        '''
        cv2.imwrite(filename, self.image)
        
