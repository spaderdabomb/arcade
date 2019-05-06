import os
import pytiled_parser


def test_load():
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)

    file_name = "../../arcade/examples/platform_tutorial/test_map_1.tmx"
    tile_map = pytiled_parser.parse_tile_map(file_name)

    assert isinstance(tile_map, pytiled_parser.objects.TileMap)
    assert tile_map.background_color.red == 193
    assert tile_map.background_color.green == 236
    assert tile_map.background_color.blue == 255
    assert tile_map.background_color.alpha == 255
    assert len(tile_map.layers) == 2
    assert tile_map.map_size == (10, 10)
    assert tile_map.render_order == 'right-down'
    assert tile_map.tile_size == (128, 128)
