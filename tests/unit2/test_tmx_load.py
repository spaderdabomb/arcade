import os
import pytiled_parser


def test_load():
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)

    file_name = "../../arcade/examples/platform_tutorial/map2_level_1.tmx"
    tile_map = pytiled_parser.parse_tile_map(file_name)

    assert isinstance(tile_map, pytiled_parser.objects.TileMap)
    assert tile_map.background_color.red == 68
    assert tile_map.background_color.green == 32
    assert tile_map.background_color.blue == 69
    assert tile_map.background_color.alpha == 255
    assert len(tile_map.layers) == 5
    assert tile_map.map_size == (40, 17)
    assert tile_map.render_order == 'right-down'
    assert tile_map.tile_size == (128, 128)

    print(tile_map.layers)
