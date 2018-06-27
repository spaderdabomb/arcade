import arcade

arcade.open_window(300, 300, "Sound Demo")
laser_sound = arcade.load_sound("sounds/laser1.wav")
laser_sound.play()
arcade.run()