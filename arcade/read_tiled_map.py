"""
Functions and classes for managing a map created in the "Tiled Map Editor"
"""

from arcade import Sprite
from arcade import SpriteList
import pytiled_parser


def read_tiled_map(tmx_file: str) -> pytiled_parser.objects.TileMap:
    """
    Given a tmx_file, this will read in a tiled map, and return
    a TiledMap object.

    Given a tsx_file, the map will use it as the tileset.
    If tsx_file is not specified, it will use the tileset specified
    within the tmx_file.

    Important: Tiles must be a "collection" of images.

    Hitboxes can be drawn around tiles in the tileset editor,
    but only polygons are supported.
    (This is a great area for PR's to improve things.)

    :param str tmx_file: String with name of our TMX file
    :param float scaling: Scaling factor. 0.5 will half all widths and heights
    :param str tsx_file: Tileset to use (can be specified in TMX file)

    :returns: Map
    :rtype: TiledMap
    """

    tile_map = pytiled_parser.parse_tile_map(tmx_file)

    return tile_map


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

            tmx_file = base_directory + tile.image.source

            my_sprite = Sprite(tmx_file, scaling)
            my_sprite.right = column_index * (map_object.tile_size[0] * scaling)
            my_sprite.top = (map_object.map_size.y - row_index) * (map_object.tile_size[1] * scaling)
            if tile.hit_box is not None:
                print("hi")
            # print(tile.image.source, my_sprite.center_x, my_sprite.center_y)
            # if tile_info.points is not None:
            #     my_sprite.set_points(tile_info.points)
            sprite_list.append(my_sprite)

    return sprite_list


