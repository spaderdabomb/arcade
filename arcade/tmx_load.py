from arcade import Sprite
from arcade import SpriteList

import pytiled_parser
import os


def get_layer(map_object: pytiled_parser.objects.TileMap,
              layer_name: str):

    for layer in map_object.layers:
        if layer.name == layer_name:
            return layer

    return None


def get_tile(map_object: pytiled_parser.objects.TileMap, gid: int) -> pytiled_parser.objects.Tile:
    for tileset_key, tileset in map_object.tile_sets.items():
        for tile_key, tile in tileset.tiles.items():
            tile_gid = tile.id + tileset_key
            if tile_gid == gid:
                return tile
    return None


def generate_sprites(map_object: pytiled_parser.objects.TileMap,
                     layer_name: str,
                     scaling: float = 1,
                     base_directory: str = "") -> SpriteList:

    sprite_list = SpriteList()

    layer = get_layer(map_object, layer_name)
    if layer is None:
        print(f"Warning, no layer named '{layer_name}'.")
        return sprite_list

    map_array = layer.data

    # Loop through the layer and add in the wall list
    for row_index, row in enumerate(map_array):
        for column_index, item in enumerate(row):
            # Check for empty square
            if item == 0:
                continue

            tile = get_tile(map_object, item)
            if tile is None:
                print(f"Warning, couldn't find tile for {item}")
                continue

            tmx_file = base_directory + tile.source

            my_sprite = Sprite(tmx_file, scaling)
            my_sprite.right = column_index * (map_object.tilewidth * scaling)
            my_sprite.top = (map_object.height - row_index) * (map_object.tileheight * scaling)

            if tile_info.points is not None:
                my_sprite.set_points(tile_info.points)
            sprite_list.append(my_sprite)

    return sprite_list


file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

file_name = "examples/platform_tutorial/test_map_1.tmx"
tile_map = pytiled_parser.parse_tile_map(file_name)

generate_sprites(tile_map, "Platforms")
