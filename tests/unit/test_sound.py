import pytest
import sys
import warnings
from pathlib import Path
import pyglet

with warnings.catch_warnings(record=True) as w:
    import arcade
    if sys.platform not in ("win32", "cygwin", "darwin"):
        assert len(w) == 1
        assert "FFmpeg binaries were not found on the system." in str(w[-1].message)
    else:
        assert len(w) == 0


@pytest.mark.parametrize("path", [
    "path/to/dummy_file.mp3",
    Path("path/to/dummy_file.mp3"),
])
def test_load_sound(path, mocker):
    """Load sound either from a string or a pathlib.Path"""

    loader = mocker.patch("pyglet.media.load")
    loader.return_value = mocker.Mock(spec=pyglet.media.StaticSource, name="source")
    sound = arcade.load_sound(path)

    (actual_path, *_), kwargs = loader.call_args
    assert Path(actual_path) == Path("path/to/dummy_file.mp3")
    assert kwargs == dict(streaming=False)
    assert sound.volume == 1
    assert isinstance(sound, pyglet.media.StaticSource)


def test_play_sound(mocker):
    source = mocker.Mock(spec=pyglet.media.Source, name="source")
    source.play.return_value = mocker.Mock(spec=pyglet.media.Player, name="player")

    player = arcade.play_sound(source)
    source.play.assert_called_once()
    assert isinstance(player, pyglet.media.Player)
