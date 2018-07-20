import pytest
from pathlib import Path
import pyglet

if not pyglet.media.have_ffmpeg():
    pytest.skip("No FFmpeg binaries found.", allow_module_level=True)


@pytest.mark.not_ci
@pytest.mark.parametrize('sound_format', ('wav', 'mp3', 'ogg'))
def test_play_sound(sound_format):
    import arcade
    this_dir = Path(__file__).parent
    resources = this_dir / "../resources"
    sound_file = "laser1." + sound_format
    path = (resources / sound_file).resolve()
    sound = arcade.load_sound(path)
    p = sound.play()
    p.push_handlers(on_player_eos=arcade.exit)
    arcade.run()

    assert pyglet.media.Source._players == []
