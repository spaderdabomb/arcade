from arcade import Sprite
from arcade import SpriteList

import pytiled_parser
import os


def generate_sprites(map_object: pytiled_parser.objects.TileMap,
                     layer_name: str,
                     scaling: float = 1,
                     base_directory: str = "") -> SpriteList:

    for layer in map_object.layers:
        if layer.name == layer_name:
            break

    sprite_list = SpriteList()

    if layer.name != layer_name:
        print(f"Warning, no layer named '{layer_name}'.")
        return sprite_list

    map_array = layer.data

    # Loop through the layer and add in the wall list
    for row_index, row in enumerate(map_array):
        for column_index, item in enumerate(row):

            if str(item) in map_object.global_tile_set:
                tile_info = map_object.global_tile_set[str(item)]
                tmx_file = base_directory + tile_info.source

                my_sprite = Sprite(tmx_file, scaling)
                my_sprite.right = column_index * (map_object.tilewidth * scaling)
                my_sprite.top = (map_object.height - row_index) * (map_object.tileheight * scaling)

                if tile_info.points is not None:
                    my_sprite.set_points(tile_info.points)
                sprite_list.append(my_sprite)
            elif item != 0:
                print(f"Warning, could not find {item} image to load.")

    return sprite_list


file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

file_name = "examples/platform_tutorial/map2_level_1.tmx"
tile_map = pytiled_parser.parse_tile_map(file_name)

generate_sprites(tile_map, "Platforms")