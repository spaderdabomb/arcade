import os
import pytiled_parser
import arcade


def test_load():
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)

    file_name = "test_data/test_map_1.tmx"
    tile_map = arcade.read_tiled_map(file_name)

    assert isinstance(tile_map, pytiled_parser.objects.TileMap)
    assert tile_map.background_color.red == 193
    assert tile_map.background_color.green == 236
    assert tile_map.background_color.blue == 255
    assert tile_map.background_color.alpha == 255
    assert len(tile_map.layers) == 2
    assert tile_map.map_size == (10, 10)
    assert tile_map.render_order == 'right-down'
    assert tile_map.tile_size == (128, 128)

    my_list = arcade.generate_sprites(tile_map, "Platforms", base_directory="../../arcade/examples/platform_tutorial/")
    assert isinstance(my_list, arcade.SpriteList)

    my_list = arcade.generate_sprites(tile_map, "Coins", base_directory="../../arcade/examples/platform_tutorial/")
    assert isinstance(my_list, arcade.SpriteList)
