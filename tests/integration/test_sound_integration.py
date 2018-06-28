import pytest
import sys
import warnings
from pathlib import Path
import pyglet

with warnings.catch_warnings(record=True) as w:
    import arcade
    if sys.platform not in ('win32', 'cygwin', 'darwin'):
        assert len(w) == 1
        assert "FFmpeg binaries were not found on the system." in str(w[-1].message)
    else:
        assert len(w) == 0


@pytest.mark.not_ci
@pytest.mark.skipif(sys.platform not in ('win32', 'cygwin', 'darwin'),
                    reason="does not run on linux without installing FFmpeg.")
class TestSounds:

    @pytest.mark.parametrize('sound_format', ('wav', 'mp3', 'ogg'))
    def test_play_sound(self, sound_format):
        this_dir = Path(__file__).parent
        resources = this_dir / "../resources"
        sound_file = "laser1." + sound_format
        path = (resources / sound_file).resolve()
        sound = arcade.load_sound(path)
        p = sound.play()
        p.push_handlers(on_player_eos=arcade.exit)
        arcade.run()

        assert pyglet.media.Source._players == []
