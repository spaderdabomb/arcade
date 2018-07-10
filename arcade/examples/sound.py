import arcade
from pathlib import Path

arcade.open_window(300, 300, "Sound Demo")
this_dir = Path(__file__).parent
laser_sound = arcade.load_sound(this_dir / "sounds/laser1.wav")
laser_sound.volume = 0.2
laser_sound.play()
arcade.run()